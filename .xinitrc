#!/bin/sh

# Note: only works on debian
# set resolution, depends on monitor
xrandr --newmode "1920x1080_60.00"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync
xrandr --addmode DP-1 "1920x1080_60.00"
xrandr --output DP-1 --mode "1920x1080_60.00"

. /etc/X11/Xsession &
exec bspwm
