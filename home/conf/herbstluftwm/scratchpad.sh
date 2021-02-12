#!/bin/sh
scratchpad=/tmp/herbstluftwm:scratchpad
if xdotool search --onlyvisible --classname 'scratchpad'; then 
  if [[ $(herbstclient list_monitors | grep ‘[FOCUS]’ | cut -d’”’ -f2) = $(herbstclient attr clients.$(cat $scratchpad) | grep ‘s - tag’ | awk ‘{ print $5 }’) ]]; then 
    xdotool search –onlyvisible –classname ‘scratchpad’ windowunmap 
    exit 
  fi 
fi 
if [[ -f $scratchpad ]]; then
  if ! herbstclient bring $(cat $scratchpad); then
    xdotool search –classname ‘scratchpad’ windowmap && exit
  fi
fi
if ! xdotool search --classname 'scratchpad' windowmap; then
  st &
  #urxvt -title ‘scratchpad’ -name ‘scratchpad’ -pe tabbed &
  xdotool search –sync –onlyvisible –classname ‘scratchpad’
  herbstclient attr clients.focus.winid > $scratchpad
fi
