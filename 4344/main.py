# 4344

import sys
#f = sys.stdin

f = open('data.txt', 'r')
C = int(f.readline().rstrip())

for i in range(C):
  data = list(map(int, f.readline().split()))
  N, scores = data[0], data[1:]
  sum = 0

  for score in scores:
    sum += score

  average = sum / len(scores)
  member = 0
  for score in scores:
    if score > average:
      member += 1

  good_rate = member / len(scores)
  print ('{0:.3%}'.format(good_rate))