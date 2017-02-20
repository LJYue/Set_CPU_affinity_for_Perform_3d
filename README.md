# Set_CPU_affinity_for_Perform_3d
## Link
https://github.com/LJYue/Set_CPU_affinity_for_Perform_3d
## Notice
This .py file set CPU affinity to all for ALL PERFORM-3D engines every 20 minutes. This can be easily changed by modifying the file using any text editors, for instance, notepad.

It works only for 64 bit program, 32 bit is not yet supported due to lack of such program installed in my computer. (But who use 32 bit? 4GB RAM for PERFORM-3D? Are you kidding me?)
## Background
PERFORM-3D would atomatically set CPU affinity for its engines, but the program can only detect cores of the cpu instead of threads. It is, however, able to set CPU affinity to all manually, but an engine is only created for one load case only. 

Therefore, it is most annoying that one have to manaully set CPU affinity after each load case is completed. And let alone one might have multiple engines runing simultaneously. 

Being fed up with, one turns to python and leaves such cumbersomeness to the computer. Ha, is not it what computers are invented for?
