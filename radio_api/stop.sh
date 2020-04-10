#!/usr/bin/env bash
# v0.5.0
# stop.sh - This script is called by the Colosseum to tell the radio the match is ending. 
# No input is accepted.
# STDOUT and STDERR may be logged, but the exit status is always checked.
# The script should return 0 to signify successful execution.

# ---Example Usage---
#check if there is an input argument
case $# in
     0)   #zero inputs
          #example radio stop:
          #python /path/to/radio/stop.py
          exit 0 #exit successfully
          ;;
     *)   #one or more input arguments (example error case)
          #example error exit code:
          exit 64 #exit with an error
          ;;
esac

# While this script can directly issue commands to the radio, 
# another use case may be to keep a radio control daemon running 
# and have this script interface with the daemon.
# The exact way this script stops the radio  is up
# to individual teams so long as the required outputs are returned.
