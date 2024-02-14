# Converts FLAC files to MP3 format using AudioSegment

import os
import tqdm
import ffmpeg

#  add paths here:
outputFolder = "ClassicalDataset"
inputFolder = "ClassicalMusic"

# add other parameters here
outBitRate = "96k"
verbose = True


# Create the output folder if it doesn't exist
if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

# stores a list of all files in the parent directory,
# assuming they're all flac files
files = [file for file in os.listdir(inputFolder)]

files_converted = 0


for file in tqdm.tqdm(files, desc="Converting", unit="file"):

    input_file = os.path.join(inputFolder, file)


    output_file = os.path.join(
        outputFolder, os.path.splitext(file)[0] + '.mp3')

    # Convert FLAC to MP3 using ffmpeg
    ffmpeg.input(input_file).output(output_file, bitrate=outBitRate, loglevel="info" if verbose else "quiet").run(overwrite_output=True)
    
    files_converted += 1

print(f"Conversion complete. {files_converted} files converted.")
