from datetime import datetime
import time


t = time.time()
time.sleep(1)

print((time.time()-t)>2)