#!/bin/bash

killall -q polybar
echo "---" | tee -a /tmp/polybar1.log
polybar foobar 2>&1 | tee -a /tmp/polybar1.log & disown
echo "Polybar launched..."
