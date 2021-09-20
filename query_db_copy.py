import sys
import uuid
import json
import time

def get_count (key):
    with open("db.json", "rb") as f:
        data = f.read()
        js = json.loads(data)

    # print(js[key])
    return len(js[key])

start_time = time.time()

for key in sys.argv[1:]:
    print("{}: {}".format(key, get_count(key)))

print("--- %s seconds ---" % (time.time() - start_time))
