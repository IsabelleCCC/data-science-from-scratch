from collections import Counter
import matplotlib.pyplot as plt

num_friends = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10 	,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title('Histogram of Friends Counts')
plt.xlabel('# of friends')
plt.ylabel('# of people')
# plt.show()

num_points = len(num_friends)

assert num_points == 204

largest_value = max(num_friends)
lowest_value = min(num_friends)

assert largest_value == 100
assert lowest_value == 1

sorted_values = sorted(num_friends)
smallest_value = sorted_values[0] # 1

from typing import List

def mean(xs: List[float]) -> float:
    return (sum(xs)/len(xs))

assert 7.3333 < mean(num_friends) < 7.333334

def _median_odd(xs: List[float]) -> float:
        ''' If len(xs) is even, it's the average of the middle two elements '''
        return sorted(xs)[len(xs) // 2]

def _median_even(xs: List[float]) -> float:
      ''' If len(xs) is even, it's the average of the middle two elements '''
      sorted_xs = sorted(xs)
      hi_midpoint = len(xs) // 2
      return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2

def median(v: List[float]) -> float:
      return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)

assert median([1, 10, 2, 9, 5]) == 5
assert median([1, 9, 2, 10]) == (2 + 9) / 2

print(median(num_friends))

def quantile(xs: List[float], p: float) -> float:
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]

assert quantile(num_friends, 0.10) == 1
assert quantile(num_friends, 0.25) == 3
assert quantile(num_friends, 0.75) == 9
assert quantile(num_friends, 0.90) == 13

def mode(x: List[float]) -> List[float]:
      ''' Cálculo de moda. Retorna o número amigos mais frequente. '''
      count_friends = Counter(x)
      max_count = max(count_friends.values())
      return [x_i for x_i, count in count_friends.items() if count == max_count]

assert mode(num_friends) == [6,1]  

def data_range(xs: List[float]) -> float:
      ''' Cálculo da amplitude '''
      return max(xs) - min(xs)

assert data_range(num_friends) == 99