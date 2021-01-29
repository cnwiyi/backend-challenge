AdGear Backend Coding Challenge
===============================

  This is the interview challenge for AdGear's Backend Team (aka Systems Team). It's a
  simplification of a kind of problem that we often have to tackle: querying a key/value store
  very quickly.

  Your challenge: to improve upon the query performance of the naive demo while retaining
  correctness. Write a new version of create_db and query_db — in Python or another language of
  your choice — that reduces the time that it takes to execute a query. (N.B.: duplicating the naive
  approach in a compiled language is *not* considered a solution.)

  You should focus on correctness and performance: your solution should give the same result as the
  naive version, but do it faster.

  For this challenge, you don't have to concern yourself with providing a friendly and robust user
  interface or with giving the user a lot of flexibility: stack traces are acceptable error messages
  and hard-coded paths are fine.

  You can use third-party libraries for parsing JSON and UUIDs, however we ask that you code the
  storage and retrieval parts yourself (i.e., don't just SQLite or LLDB).


How to run the demo
-------------------

  To run the demo, you will need an installation of Python 3.
  Once you have that, there are three commands to run:

  - generate_events.py creates a file, `events.json`, that contains raw events in JSON.
  - create_db.py reads `events.json` and creates `db.bin`
  - query_db.py accepts UUIDs on the command lines, searches in `db.bin`, and reports how many values are associated with each UUID.


```python
    $ python3 generate_events.py              # Creates events.json
    $ python3 create_db.py                    # Creates db.bin
    $ python3 query_db.py <UUID1> <UUID2> ... # Queries db.bin
```

  (To get some UUIDs to pass to query_db, look in the events.json file.)
