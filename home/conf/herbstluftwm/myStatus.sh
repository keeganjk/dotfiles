#!/usr/bin/env bash

#xpos=0
#ypos=0
#width=640
#height=24
fgcolor="#c0b18b"
bgcolor="#111111"
font="Terminus"

parameters=" -p "
#parameters+=" -x $xpos -y $ypos -w $width -h $height"
parameters+=" -fn $font"
parameters+=" -ta -c -bg $bgcolor -fg $fgcolor"

updateStatusbarOutput() {
    echo "$1" | dzen2 $parameters
}

updates() {
    UPD="$(checkupdates+aur | wc -l)"
    #echo -n "$UPD"
    echo -n "[UPDATES: $UPD]"
}

memory_percentage() {
    MEM_TOTAL="$(head -n1 /proc/meminfo | sed 's/MemTotal:\s*//;s/\s*kB//')"
    MEM_FREE="$(grep -i -m1 free /proc/meminfo | sed 's/MemFree:\s*//;s/\s*kB//')"
    MEM_BUFFER="$(grep -i -m1 buffers /proc/meminfo | sed 's/Buffers:\s*//;s/\s*kB//')"
    MEM_CACHE="$(grep -i -m1 cached /proc/meminfo | sed 's/Cached:\s*//;s/\s*kB//')"
    MEM_USED=$(echo "$MEM_TOTAL-$MEM_FREE-$MEM_BUFFER-$MEM_CACHE" | bc)
    MEM_PERCENTAGE=$(echo "scale=1; 100*$MEM_USED/$MEM_TOTAL" | bc)
    MEM_PERCENTAGE=$(echo "$MEM_PERCENTAGE" | bc)
    MEM_PERCENTAGE=$(printf "%.1f\n" $MEM_PERCENTAGE)
    #echo -n "$MEM_PERCENTAGE%"
    echo -n "[MEMORY: $MEM_PERCENTAGE%]"
}

cpu_percentage() {
    set -- $(mpstat -P 0 | sed '$!d;s/\S*\s\SM//')
    #CPU=$2
    CPU=$(printf "%.1f\n" $2)
    #echo -n "$CPU%"
    echo -n "[CPU: $CPU]"
}

date_and_time() {
    DAT="$(date '+%Y.%m.%d %H:%M')"
    #echo -n "$DAT"
    echo -n "[TIME: $DAT]"
}

local_ip() {
    set -- $(ip a | grep inet | grep -v 127.0.0.1 | grep -v inet6)
    LOCAL_IP=$(echo $2 | sed 's/\/\S*//')
    echo -n "[$LOCAL_IP]"
}

tags() {
    TAG="$(herbstclient tag_status | sed 's/\t/ /g')"
    echo -n "[$TAG]"
}

while true; do
    echo "$(tags &) $(local_ip &) $(updates &) $(memory_percentage &) $(cpu_percentage &) $(date_and_time &)" 
    sleep .1
done | dzen2 $parameters
