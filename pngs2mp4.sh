#!/bin/bash

j=0
for i in *.png; do `printf "mv %s %06d.png\n" $i $j`; j=$((j+1)); done
/usr/bin/ffmpeg -start_number 0 -i "%6d.png" -c:v libx264 -vf fps=30 -pix_fmt yuv420p out.mp4
