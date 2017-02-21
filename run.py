import sched
import time
import psutil

s = sched.scheduler(time.time, time.sleep)
def set_affinity(sc): 
    all_id = psutil.pids()
    p3d_id = []
    for i in all_id:
        p = psutil.Process(i)
        if "Pf3dEngine" in p.name():
    #       print p.pid
    #       break
            p.cpu_affinity([])
            p.nice(psutil.HIGH_PRIORITY_CLASS)
            print str(p.pid)+" set"
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    s.enter(600, 1, set_affinity, (s,))

s.enter(1, 1, set_affinity, (s,))
s.run()
