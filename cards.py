from random import shuffle
import copy

a = ["T", 2, 3, 4, 5, 6, 7, 8, 9, 10, "V", "D", "K"]

first_hand = copy.copy(a)

iterations = 100000

avg = 0

for i in range(iterations):
  shuffle(a)
  match = 0
  for j in range(10):
    if a[j] == first_hand[j]:
      match += 1
  
  print(match),
  avg += match
  
print avg/iterations  
