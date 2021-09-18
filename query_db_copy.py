import sys
import uuid
import json

def get_count (key):
    with open("db.txt", "rb") as f:
        data = f.read()
        js = json.loads(data)

    # print(js[key])
    return len(js[key])

for key in sys.argv[1:]:
    print("{}: {}".format(key, get_count(key)))
