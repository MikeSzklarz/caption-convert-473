import re
import argparse
import os
import os.path

parser = argparse.ArgumentParser(
    description='Convert all .srt subtitle files in a folder to plain .txt transcripts.'
)
parser.add_argument(
    'input_path',
    help='Path to the input folder containing .srt files'
)
args = parser.parse_args()

input_path = args.input_path
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

timestamp_regex = re.compile(r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}')

def convert_srt_to_txt(input_file, output_file):
    main_transcript_blocks = []
    current_caption_lines = []
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                is_timestamp = timestamp_regex.match(line)
                is_number = line.isdigit()
                is_blank = not line
                if not is_timestamp and not is_number and not is_blank:
                    current_caption_lines.append(line)
                elif is_blank and current_caption_lines:
                    block_text = ' '.join(current_caption_lines)
                    main_transcript_blocks.append(block_text)
                    current_caption_lines = []
        if current_caption_lines:
            block_text = ' '.join(current_caption_lines)
            main_transcript_blocks.append(block_text)
        full_transcript = '\n'.join(main_transcript_blocks)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_transcript)
        print(f"Success! Transcript saved to {output_file}")
    except Exception as e:
        print(f"Error processing {input_file}: {e}")

for filename in os.listdir(input_path):
    if filename.lower().endswith('.srt'):
        input_file = os.path.join(input_path, filename)
        base_name = os.path.splitext(filename)[0]
        output_file = os.path.join(output_dir, f"{base_name}-transcript.txt")
        print(f"Converting {input_file}...")
        convert_srt_to_txt(input_file, output_file)