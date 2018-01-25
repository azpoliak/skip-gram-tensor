import sys
import random

f = open(sys.argv[1], "rb")

for line in f.readlines():
  print(line.strip() + ' ' + str(int(random.random() * 1)))
  print(line.strip() + '_REL1')

