import json
import sys
import uuid
import time

start_time = time.time()

with open("db.bin", "wb") as out:
    with open("events.json") as in_:
        for line in in_:
            record = json.loads(line)
            key = uuid.UUID(record["key"])
            value = uuid.UUID(record["value"])

            out.write(key.bytes)
            out.write(value.bytes)

print("--- %s seconds ---" % (time.time() - start_time))
