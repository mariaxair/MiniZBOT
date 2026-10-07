#!/usr/bin/env bash
# Rebuild assets/demo/demo.mp4 (12 s, 1600x1000) from the ZAD Train screen recordings.
# Usage: ./build-demo.sh <untitled_design.mp4> <download_6.mp4> <download_4.mp4>
# Cuts follow the three demo sentences; crossfades land on the step boundaries (2.7 s, 6.3 s).
set -euo pipefail
UD="$1"; D6="$2"; D4="$3"
S="scale=1600:1000:flags=lanczos,fps=30,format=yuv420p,setsar=1"
ffmpeg -loglevel error -y \
  -ss 0.9   -t 1.25 -i "$UD" \
  -ss 12.05 -t 1.9  -i "$UD" \
  -ss 4.45  -t 2.0  -i "$D6" \
  -ss 12.95 -t 1.45 -i "$D6" \
  -ss 2.3   -t 1.65 -i "$D4" \
  -ss 6.4   -t 3.6  -i "$D4" \
  -filter_complex "\
[0:v]crop=1328:830:296:85,$S,trim=duration=1.25,setpts=PTS-STARTPTS[a];\
[1:v]crop=1456:910:240:150,$S,trim=duration=1.9,setpts=PTS-STARTPTS[b];\
[2:v]crop=1728:1080:0:0,$S,tpad=stop_mode=clone:stop_duration=0.1,trim=duration=2.1,setpts=PTS-STARTPTS[c];\
[3:v]crop=1600:1000:160:25,$S,tpad=stop_mode=clone:stop_duration=0.65,trim=duration=2.1,setpts=PTS-STARTPTS[d];\
[4:v]crop=1440:900:480:180,$S,tpad=stop_mode=clone:stop_duration=0.25,trim=duration=1.9,setpts=PTS-STARTPTS[e];\
[5:v]crop=1728:1080:150:0,$S,tpad=stop_mode=clone:stop_duration=0.65,trim=duration=4.25,setpts=PTS-STARTPTS[f];\
[a][b]xfade=transition=fade:duration=0.3:offset=0.95[ab];\
[ab][c]xfade=transition=fade:duration=0.3:offset=2.55[abc];\
[abc][d]xfade=transition=fade:duration=0.3:offset=4.35[abcd];\
[abcd][e]xfade=transition=fade:duration=0.3:offset=6.15[abcde];\
[abcde][f]xfade=transition=fade:duration=0.3:offset=7.75,trim=duration=12,setpts=PTS-STARTPTS[v]" \
  -map "[v]" -an -c:v libx264 -crf 17 -g 30 -keyint_min 30 -pix_fmt yuv420p -movflags +faststart \
  "$(dirname "$0")/assets/demo/demo.mp4"
