# Automatic song tempo aligner

The program aligns the tempo of a music file to match an ideal metronome.
Audio pitch is preserved.

The bpm value (beats per minute) should be set by the user, but the program
prints the average bpm it found in the original audio. Beats are recognized in
the audio file by importing labels from an Audacity project.

# Use cases

One can take an original recording and align the tempo, so that it can be
imported to a DAW (Digital Audio Workstation). This is an important feature
if one wants to record a cover of the recording with a metronome. Importing
the original directly would result in a misalignment, which would make it
inconvenient to work with.

# Usage

1. Create an Audacity project that contains the music file
2. While listening to the audio, place labels on every beat (or every 2nd,
or 4th beat) -- the default hotkey is Ctrl+M
3. Save the project
4. Invoke the program, passing the arguments: the audio file, Audacity project,
bpf (beats per fragment; fragment is the area from a label to the next),
bpm (beats per minute)

```
python3 tempoligner --input input.mp3 --output output.flac --aup project.aup --bpf 2 --bpm 100
```

The aligned song is written to `output.flac` in this example and is aligned
to an ideal 100 bpm metronome (but see Limitations below). It is assumed
that labels are placed in Audacity project each two beats (`--bpf` argument).

Note: currently only mp3 input is supported.

# Dependencies

The code is written in Python 3.

Use

```
pip install -r requirements.txt
```

to install the dependencies.

# Limitations

Actually, the output is not aligned to an ideal metronome, but will drift
slightly over time due to inexact segment durations. Typically the drift won't
exceed 100 ms over a 4 min audio file. There is a plan to remove the drift
and make the output ideally aligned.

There are slight signal distortions around labels. Depending on the type of
music this may or may not be a big issue. Just try and check if it's
acceptable for your use case.

# Author

Copyright (C) 2018, Michał Szymański
