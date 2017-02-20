# Set_CPU_affinity_for_Perform_3d
## Link
https://github.com/LJYue/Set_affinity_for_Perform_3d
## Notice
This .py file set affinity to all threads for ALL PERFORM-3D engines every 20 minutes. This can be easily changed by modifying the file using any text editors, for instance, notepad.

It works only for 64 bit program, 32 bit is not yet supported due to lack of such program installed in my computer. (But who use 32 bit? 4GB RAM for PERFORM-3D? Are you kidding me?)
## Background
PERFORM-3D would atomatically set affinity for its engines, which can be of benefit, but the program can only detect cores of the CPU instead of threads. Let me illustrate better. 

If, for instance, the CPU has 2 cores (and 4 threads),  the engines would be assgined to CPU0 and CPU2, leaving CPU1 and CPU3 idle.  Since there are four threads, the computer can support four engines running.  One may be able to set affinity for engines to all threads (CPU0, CPU1, CPU2 and CPU3 in this case) manually, but notice that an engine process is created for one load case only. After the completion of that load case, another engine process is created to run the folloiwing load case, and unfortunately, affinity is automatically assigned to CPU0 and CPU2 by default. Now one would  have to manually set affinity once again! Let alone the computer might have multiple engines runing simultaneously.

Being fed up with, one turns to python and leaves such cumbersomeness to computer. Ha, is not it what computers are created for?
