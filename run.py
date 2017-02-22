import sched
import time
import psutil

def main():
    s = sched.scheduler(time.time, time.sleep)
    def set_affinity(sc): 
        all_id = psutil.pids()
        for i in all_id:
            p = psutil.Process(i)
            if "Pf3dEngine" in p.name()or "Perform-3D" in p.name():
        #       print p.pid
        #       break
                p.cpu_affinity([])
                p.nice(psutil.HIGH_PRIORITY_CLASS)
                print str(p.pid)+" set"
        print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        s.enter(600, 1, set_affinity, (s,))

    s.enter(1, 1, set_affinity, (s,))
    s.run()

if __name__ == "__main__":
    main()