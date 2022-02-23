import time 

start = time.time()
time.sleep(1)
end = time.time()
print(end - start)

start = time.perf_counter()
print(start)
time.sleep(1)
end = time.perf_counter()
print(end)
print(end - start)
