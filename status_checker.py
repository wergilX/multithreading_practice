import threading
import time
import requests

# Shared memory
counter = 0
results = []
lock = threading.Lock()

urls = ["https://google.com", "https://github.com", "https://python.org", "https://stackowerflow.com"] * 5

def check_url(url):
    global counter
    try:
        responce = requests.get(url, timeout=5)
        status = responce.status_code()
    except:
        status = "Error"
    # Critical section!
    lock.acquire()
    try:
        counter += 1
        results.append(f"Site {url}: {status}")
        print(f"Checked {counter}/{len(urls)}")
    finally:
        lock.release()

# Run threads
threads = []
for url in urls:
    t = threading.Thread(target=check_url, args=(url,))
    threads.append(t)
    t.start()

# Wait all threads
for t in threads:
    t.join()

# Show result
print(f"\n result {len(results)} refferences")