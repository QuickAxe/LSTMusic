# LSTMusic
Learning more about LSTMs and generating music using them
The sample rate of the music read is 22050Hz, hence, to get a 1s window, windows of length 22050 shall be used to train the lstm model.

### Log date[ 24-07-2024] : 
    Giving up on the above approach, due to the following reasons: 
    1) The combined dataset consisted of a numpy array about 4.3GB big, leading to huge preprocessing times, and running out of memory (16GB)
    2) MIDI might be the better way to go forward, due to MUCH smaller file sizes 
    Will use MIDI datasets henceforth. All old code files will be in the oldCode folder.