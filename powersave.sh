#!/bin/bash

# root *only*

# maximum powersave
echo 5 > /proc/sys/vm/laptop_mode

# low cpufreq
echo "conservative" > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
echo "conservative" > /sys/devices/system/cpu/cpu1/cpufreq/scaling_governor

# cpu balance
echo 1 > /sys/devices/system/cpu/sched_smt_power_savings

# sound powersave
echo 10 > /sys/module/snd_hda_intel/parameters/power_save

# turn off camera
modprobe -r uvcvideo

# HDD-memory swap
echo 90 > /proc/sys/vm/dirty_ratio
echo 1 > /proc/sys/vm/dirty_background_ratio
echo 6000 > /proc/sys/vm/dirty_writeback_centisecs
