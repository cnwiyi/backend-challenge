import sys
import uuid
import time

start_time = time.time()

counts = dict((uuid.UUID(key), 0) for key in sys.argv[1:])

with open("db.bin", "rb") as f:
    try:
        while True:
            key = uuid.UUID(bytes=f.read(16))
            value = uuid.UUID(bytes=f.read(16))
            if key in counts:
                counts[key] += 1
    except:
        pass

for key, count in counts.items():
    print("{}: {}".format(key, count))

print("--- %s seconds ---" % (time.time() - start_time))
