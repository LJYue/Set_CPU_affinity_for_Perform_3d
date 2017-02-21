# Readme
## Link
https://github.com/LJYue/Set_affinity_for_Perform_3d
## Notice
This .py file set affinity to all threads for ALL PERFORM-3D engines every 20 minutes. This can be easily changed by modifying the file using any text editors, for instance, notepad.

It works only for 64 bit program; 32 bit is supported in thoeary. 

## Background
PERFORM-3D would atomatically set affinity for all of its engines, which can be of benefit, but the program can only detect cores of the CPU instead of threads. Let me illustrate better. 

If, for instance, the CPU has 2 cores (and 4 threads),  the engines would be assgined to only two threads namely CPU0 and CPU2, leaving CPU1 and CPU3 idle.  Since there are four threads, the computer can support four engines running in full capacity. One may want to set affinity for engines to all threads (CPU0, CPU1, CPU2 and CPU3 in this case) manually, so that the computer can run four engines simultaneously without jamming each other in only two of the four threads. But notice that an engine process is created for one load case only, after the completion of that load case, another engine process is created to run the folloiwing load case. Unfortunately, its affinity is automatically set to CPU0 and CPU2 by default. Now one would have to manually set affinity once again to reach full capacity! 

Being fed up with, one turns to python and leaves such cumbersomeness to computer. Ha, isn't it what computers are created for?
