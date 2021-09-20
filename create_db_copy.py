import json
import sys
import uuid
import time

# optimize db by encoding content

# def create_dict ():
#     d = {}

#     with open("events_copy.json") as in_:
#         for line in in_:
#             record = json.loads(line)
#             key = str(uuid.UUID(record["key"]))
#             value = str(uuid.UUID(record["value"]))
#             # print("key: ", key, "value: ", value )
#             if key in d.keys():
#                 d[key].append(value)
#             else:
#                 d[key] = [value]

#     with open("db.txt", "w") as out:
#         out.write(json.dumps(d))

#     for key in d.keys():
#         print(key, d[key], len(d[key]))

from collections import defaultdict

d = defaultdict(list)

def create_dict ():
    with open("db.json", "w") as out:
        with open("events.json") as in_:
            for line in in_:
                record = json.loads(line)
                key = str(uuid.UUID(record["key"]))
                value = str(uuid.UUID(record["value"]))
                # print("key: ", key, "value: ", value )
                d[key].append(value)
    
        out.write(json.dumps(d))

    # for key in d.keys():
    #     print(key, d[key], len(d[key]))
    return d

start_time = time.time()

create_dict ()

print("--- %s seconds ---" % (time.time() - start_time))
