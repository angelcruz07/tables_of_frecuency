# Sum a range the numbers sin usar el metodo sum()
def sum_numbers(data):
  numbers = len(data)
  sum = 0
  for i in range(numbers):
    sum += data[i]
    
  return round(sum, 2)


# data = [1.7, 1.6, 1.9, 1.8 ,1.9 , 1.7 , 1.8, 1.6, 1.9, 1.7, 1.9, 1.8, 1.9, 1.8 , 1.6 , 1.8, 1.9 ,1.7, 1.9 ,1.8 ]
# data = [
# 	119, 109, 124, 119, 106, 112, 112, 112, 112, 109, 112, 124, 109, 109, 109,
# 	106, 124, 112, 112, 106
# ]
# data = [ 3, 3, 3 ,1]

data = [3.2, 3.1, 2.4, 4.0, 3.5 , 3.0, 3.5, 3.8, 4.2 , 4.9]
print(sum_numbers(data))