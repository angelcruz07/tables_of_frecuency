import math
import textwrap
import statistics

# Order List of numbers
def order_numbers(numbers):
  return sorted(numbers)

# Class
def calculate_number_class(data):
   n = len(data)
   k = 1 + math.log2(n)
   if round(k) % 2 == 0:
        k += 1
   return  int(round(k))

# Range
def calculate_range(data):
   if len(data) == 0:
    return None
   else:
        return round(max(data) - min(data), 2)

# Amplitude
def calculate_amplitude(data):
   range_number =calculate_range(data)
   count_class = calculate_number_class(data)
   return round(range_number / count_class, 2)

# Interval of class
def defined_intervals(data, decimal_places = 2):
    num_intervals = calculate_number_class(data)
    amplitude = calculate_amplitude(data)
    intervals = []

    lower_limit = min(data)

    for i in range(num_intervals):
         upper_limit = round(lower_limit + amplitude, decimal_places)

        # Redondear el límite superior hacia arriba
         if decimal_places == 2 and lower_limit > 1:
            upper_limit = math.ceil(upper_limit)

         intervals.append((lower_limit, upper_limit))
         lower_limit = upper_limit + 1  # Añadido un pequeño margen entre intervalos

    return intervals

# Mark of class
def defined_markofclass(data):
   intervals = defined_intervals(data)
   mark_of_class_list = []
   
   for interval in intervals:
      lower_limit, upper_limit = interval
      mark_of_class = (lower_limit + upper_limit) / 2
      mark_of_class = round(mark_of_class, 2)
      mark_of_class_list.append(mark_of_class)
    
   return mark_of_class_list

# Absolute frequency
def calculate_absolute_frequency(data):
    intervals = defined_intervals(data)
    absolute_frequency = []

    for interval in intervals:
        limit_lower, limit_upper = interval
        count = sum(limit_lower <= number <= limit_upper for number in data)
        absolute_frequency.append(count)

    return absolute_frequency


# cumulative frequency  
def calculate_cumulative_frequency(data):
   absolute_frequency = calculate_absolute_frequency(data)
   cumulative_frequency = [sum(absolute_frequency[:i+1]) for i in range(len(absolute_frequency))]
   return cumulative_frequency

# Complementary frequency
def calculate_complementary_frequency(data):
   total_observations = len(data)
   cumulative_frequency = calculate_cumulative_frequency(data)
   complementary_frequency =[total_observations - freq for freq in cumulative_frequency]
   return complementary_frequency

# Real limits function 
def real_limits(data, gap):
    intervals = defined_intervals(data)
    real_limits = []

    for i in range(len(intervals)):
        lower_limit, upper_limit = intervals[i]
        real_lower_limit = lower_limit - gap / 2
        real_upper_limit = upper_limit + gap / 2
        real_limits.append((round(real_lower_limit, 3), round(real_upper_limit, 3)))

    return real_limits


def print_table():
   print("""
                                                      Tabla de frecuencia
----------------------------------------------------------------------------------------------------------------------------------------------------
| Clase |   Numero de intervalos  | Intervalos  reales       | Marca    |  Frecuencia absoluta  | Frecuencia acumulada  | Frecuencia complementaria |
|       |-------------------------|--------------------------|   de     |-----------------------|-----------------------|---------------------------|
|       |  Inferior  |  Superior  | Inferior    | Superior   |  clase   |  Simple  |  Relativa  | Simple   | Relativa   |    Simple   |   Relativa  |   
----------------------------------------------------------------------------------------------------------------------------------------------------""")



# Write your details here (numbers)
# data  =  [
# 	0.06, 0.9, 0.08, 0.65, 0.07, 0.17, 0.28, 0.72, 0.78, 0.51, 0.61, 0.86, 0.6,
# 	0.76, 0.53, 0.16, 0.88, 0.68, 0.96, 0.77, 0.41, 0.74, 0.08, 0.67, 0.46, 0.37,
# 	0.47, 0.86, 0.45, 0.06, 0.82, 0.81, 0.45, 0.41, 0.21, 0.52, 0.59, 0.6, 0.96,
# 	0.55, 0.87, 0.99, 0.07, 0.17, 0.45, 0.59, 0.52, 0.61, 0.17, 0.62, 0.35, 0.38,
# 	0.28, 0.45, 0.46, 0.53, 0.16, 0.57, 0.2, 0.82, 0.65, 0.72,0.99,0.2
# ]

# data = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65]

# data = [ 
#    1,  47, 91, 47, 61, 41, 58, 90,
#    53, 1 , 94, 83, 86, 23, 84, 19,
#    50, 88, 53, 85, 49, 78, 12, 72,
#    99, 85, 86, 30, 80, 72, 66, 29,
#    91, 53, 19, 47, 68, 72, 87, 79,
#    43, 66, 53, 61, 23, 37, 31, 34
#    ]

# data = [
#    35,42,35,36,33,23,24,33,28,21,21,21,37,29,13,11,6,32,23,14,
#    18,17,24,19,28,21,31,13,12,38,14,23,45,19,33,34,28,25,26,7,
#    29,11,22,9,43,36,10,4,43,30,43,29,24,29,19,18,9,36,35,10
# ]

data = [1.7, 1.6, 1.9, 1.8 ,1.9 , 1.7 , 1.8, 1.6, 1.9, 1.7, 1.9, 1.8, 1.9, 1.8 , 1.6 , 1.8, 1.9 ,1.7, 1.9 ,1.8 ]

intervals = defined_intervals(data, decimal_places=2)
real_limits_values = real_limits(data, gap=0.5)
marks_of_class = defined_markofclass(data)
absolute_frequency = calculate_absolute_frequency(data)
cumulative_frequency = calculate_cumulative_frequency(data)
complementary_frequency = calculate_complementary_frequency(data)

print_table()

for i, ( interval, mark_of_class, freq_abs, cumulative_frequency, complementary_frequency, real_limits_values) in enumerate(zip(intervals, marks_of_class, absolute_frequency, cumulative_frequency, complementary_frequency, real_limits_values), start=1):
    real_limit_lower, real_limit_upper = real_limits_values
    print(
        f"| {i:<5} | {interval[0]:<10} |  {interval[1]:<10} | {real_limit_lower:<10} | {real_limit_upper:<10} | {mark_of_class:<8} | {freq_abs:<8} | {'{:0.2%}'.format(freq_abs / len(data)):<10} | {cumulative_frequency:<8} | {round(cumulative_frequency / len(data) * 100):<10} | {complementary_frequency:<11} | {round(complementary_frequency / len(data) * 100, 2):<11} |")
    
# Data 
print("Total de números:", len(data))
print("Rango:", calculate_range(data))
print("Amplitud:", calculate_amplitude(data))

result = order_numbers(data)
columns = 5
wrapped_result = textwrap.wrap(', '.join(map(str, result)), width=columns*6)

print("Números ordenados:")
for row in wrapped_result:
    print(row)