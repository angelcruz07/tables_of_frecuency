# Calculate mean , median, mode in ungrouped data
import statistics

def order_numbers(numbers):
  return sorted(numbers)

def calculate_promedio(data):
   numbers = order_numbers(data)
   media = statistics.mean(numbers)
   return round(media, 2)

def calculate_median(data):
   numbers = order_numbers(data)
   median = statistics.median(numbers)
   return median


def calculate_mode(data):
   numbers = order_numbers(data)
   mode = statistics.mode(numbers)
   return mode



# data =  [12, 15, 13, 17, 15, 18, 15, 13, 17]
# data = [4, 6, 5, 5, 3, 3, 6, 4, 3, 6, 2, 6, 6, 7, 3, 3]

# Tarea 
# Ejercicio 1
# data = [1.7, 1.6, 1.9, 1.8 ,1.9 , 1.7 , 1.8, 1.6, 1.9, 1.7, 1.9, 1.8, 1.9, 1.8 , 1.6 , 1.8, 1.9 ,1.7, 1.9 ,1.8 ]
# Ejercicio 2
# data = [119, 109, 124, 119, 106, 112,112, 112,112, 109, 112, 124, 109, 109, 109 ,106, 124, 112, 112, 106]
# Ejercicio 3
# data = [24, 20 , 22, 19, 18, 27, 25, 19, 27, 18, 21, 22, 23, 21, 19, 22, 27, 29, 23, 20]
# Ejercicio 4
data = [3.2, 3.1, 2.4, 4.0, 3.5 , 3.0, 3.5, 3.8, 4.2 , 4.9]

print("La media es igual a", calculate_promedio(data))
print("La mediana es igual a", calculate_median(data))
print("La moda es igual a", calculate_mode(data))
print("Total de numeros", len(data))
print(order_numbers(data))
print(round(sum(data), 2))
