# Caption Convert 473

## Overview
This project provides a tool for converting subtitle files (in `.srt` format) into plain text transcripts. It is designed to batch process multiple subtitle files and output corresponding transcript files for each input. This is specifically used for converting captions from coastal.yuja videos. The videos are downloaded using a specific enpoint found in the network tab of the browser's developer tools while playing the video. Kind of a pain but it works.

## Features
- Converts `.srt` subtitle files to plain text transcripts
- Batch processing: handles multiple files at once
- Input and output directories for easy organization

## Directory Structure
```
convert.py
input/
    subtitle1.srt
    subtitle2.srt
    ...
output/
    subtitle1-transcript.txt
    subtitle2-transcript.txt
    ...
```
- `convert.py`: Main script for conversion
- `input/`: Place your `.srt` subtitle files here
- `output/`: Converted transcript files will be saved here

## Usage
1. Place your `.srt` files in the `input/` directory.
2. Run the `convert.py` script:
   ```bash
   python convert.py
   ```
3. The converted transcript files will appear in the `output/` directory, named according to the input files.

## Requirements
- Python 3.x

## How It Works
The script reads each `.srt` file in the `input/` directory, extracts the spoken text, and writes it to a corresponding `.txt` file in the `output/` directory. Timing and subtitle numbers are removed, leaving only the transcript.