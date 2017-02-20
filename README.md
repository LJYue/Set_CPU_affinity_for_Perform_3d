# change_affinity
## Notice
This .py file set CPU affinity to all for ALL PERFORM-3D engines every 20 minutes. This can be easily changed by modifying the file using any text editors, for instance, notepad.
## Background
PERFORM-3D would atomatically set CPU affinity for its engines, but the program can only detect cores of the cpu but not threads. It is, however, able to set CPU affinity to all manually, but an engine is only created for one load case only. 

Therefore, it is most annoying that one have to manaully set CPU affinity after each load case is completed. And let alone one may have multiple engines runing at the same time. 

Being fed up with, one turn to python and leave such cumbersomeness to the computer. Ha, is not it what computers are invented for?
