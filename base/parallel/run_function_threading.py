import time
import threading


def method(day):
    time.sleep(5)
    print(f"{day}")


start = time.time()
threads = []
for i in range(1, 10):
    t = threading.Thread(target=method, args=[i])
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()
print(f"Ran {end - start} s")
