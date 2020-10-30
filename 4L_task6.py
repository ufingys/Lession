import itertools
import sys


name_script, start = sys.argv
count = 0
start = int(start)
for x in itertools.count(start):
    if count > 10:
        break
    print(x, end=' ')
    count += 1
print()
count = 0
for sym in itertools.cycle(name_script):
    if count > 20:
        break
    print(sym, end=' ')
    count += 1