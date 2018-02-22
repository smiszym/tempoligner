#!/usr/bin/env python3
#
# Automatic song tempo aligner
# Copyright (C) 2018, Michał Szymański
#

import argparse
from pydub import AudioSegment


parser = argparse.ArgumentParser(description='Automatic song tempo aligner')
parser.add_argument('--input', required=True, help='name of the input file')
parser.add_argument('--output', required=True, help='name of the output file (must be flac)')
parser.add_argument('--labels', required=True, help='name of the labels file')
parser.add_argument('--bpm', type=int, default=120,
                    help='desired beats per minute')
parser.add_argument('--bpf', type=int, default=8,
                    help='beats per fragment')
parser.add_argument('--crossfade-len', type=int, default=400,
                    help='crossfade length in milliseconds')

args = parser.parse_args()


fragment_len = float(60000) / args.bpm * args.bpf


def B(i):
    return i * fragment_len


song = AudioSegment.from_mp3(args.input)

with open(args.labels) as f:
    lines = [line.strip() for line in f]

b = []
for line in lines:
    s = line.split("\t")
    time = float(s[0]) * 1000
    b.append(time)

d = args.crossfade_len/2

output = song[:fragment_len+d]

print("crossfade length = %d ms" % args.crossfade_len)

local_bpm_sum = 0

for i in range(1, len(b)):
    fragment_offset = B(i) - b[i]
    fragment_start = i * fragment_len - fragment_offset
    fragment = song[fragment_start - d : fragment_start + fragment_len + d]
    output = output.append(fragment, crossfade=args.crossfade_len)
    expected_length = (1+i)*fragment_len+d
    actual_length = output.duration_seconds*1000
    local_bpm = 60000 * args.bpf / (b[i] - b[i-1])
    local_bpm_sum += local_bpm
    print("bar %d: drift %d ms, local bpm %d" \
            % (i, expected_length-actual_length, local_bpm))

average_bpm = local_bpm_sum / (len(b)-1)

print("average bpm: %d" % average_bpm)

output.export(args.output, format="flac")
