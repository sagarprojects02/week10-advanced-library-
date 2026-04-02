import time

start = time.time()
sum(range(1000000))
print("Time:", time.time() - start)
