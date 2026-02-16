import requests
import time

url = "http://127.0.0.1:5000/login"

for i in range(15):
    try:
        r = requests.get(url)
        print("Attempt", i + 1, "Status:", r.status_code)
    except:
        print("Connection error")

    time.sleep(0.5)
