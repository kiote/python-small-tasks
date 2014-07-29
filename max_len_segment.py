import numpy.random as nprnd
from collections import namedtuple

SIZE = 10
MAX_VAL = 10
MIN_VAL = -10

def same_sign(a, b):
  return a * b >= 0

# our array
ar = nprnd.randint(MIN_VAL, MAX_VAL, size = SIZE)

pre_sums = []
sums = []
Accum = namedtuple('Accum', ['sum', 'begin', 'end'])

pre_sums.append(Accum(ar[0], 0, 0))

# creating some pre-summing
for i, elem in enumerate(ar):
  if i == 0: continue
  if same_sign(ar[i-1], ar[i]):
    elem = pre_sums[len(sums)-1]
    summ = elem.sum + ar[i]
    begin = elem.begin
    end = i
    pre_sums[len(sums)-1] = Accum(summ, begin, end)
  else:
    pre_sums.append(Accum(ar[i], i, i))

sums.append(pre_sums[0])

# and one more summing
for i, elem in enumerate(pre_sums):
  if i == 0: continue
  if pre_sums[i-1].sum + pre_sums[i].sum > 0:
    sums.append(Accum(pre_sums[i-1].sum + pre_sums[i].sum, pre_sums[i-1].begin, pre_sums[i].end))
  else:
    sums.append(pre_sums[i])

max_sum = sums[0].sum
max_ind = 0
for i, s in enumerate(sums):
  if s.sum > max_sum:
    max_sum = s.sum
    max_ind = i

print "We have %r" % ar
print "We made %r" % sums

rs = sums[max_ind]
print "Max sum is %d with begin: %d and end: %d" % (rs.sum, rs.begin, rs.end)
