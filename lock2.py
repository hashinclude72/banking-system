from lockfile import LockFile
import time
t = 30
username = "z"
sender_lock = "users/" + username +"/file.lock"
lock = LockFile(sender_lock)
# lock.break_lock()
try:
    print(lock)
    lock.acquire(timeout=10)
    print('wait')
    time.sleep(t)
    lock.release()
except:
    print("lock failed")
