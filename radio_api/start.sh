#!/usr/bin/env bash
# v0.5.0
# start.sh - This script is called by the Colosseum to tell the radio the match is starting. 
# No input is accepted.
# STDOUT and STDERR may be logged, but the exit status is always checked.
# The script should return 0 to signify successful execution.

# ---Example Usage---
#check if there is an input argument for radio configuration
case $# in
     0)   #zero inputs
          #example default radio start:
          exit 0 #exit successfully
          ;;
     1)   #one input argument
          #example using input as radio config specifier:
          #/path/to/radio/main /path/to/radio/configs/$1
          exit 64 #exit with an error - should not have gotten input
          ;;
     *)   #more than one input argument (example error case)
          #example error exit code:
          exit 64 #exit with an error
          ;;
esac

# While this script can directly issue commands to the radio, 
# another use case may be to keep a radio control daemon running 
# and have this script interface with the daemon.
# The exact way this script puts the radio in operation is up
# to individual teams so long as the required outputs are returned.
