import math

# Order List of numbers
def order_numbers(numbers):
  return sorted(numbers)

# Class
def calculate_number_class(data):
   n = len(data)
   k = 1 + math.log2(n)
   return  round(k, 2)

# Range
def calculate_range(data):
   if len(data) == 0:
    return None
   else:
        maximum = max(data)
        minimum = min(data)
        range_data = maximum - minimum 
        return round(range_data, 2)

# Amplitude
def calculate_amplitude(data):
   range_number =calculate_range(data)
   count_class = calculate_number_class(data)

   amplitude = range_number / count_class 
   return round(amplitude, 2)


# Interval of class
def defined_intervals(data):
  num_intervals = calculate_number_class(data)
  amplitude = calculate_amplitude(data)

  intervals = []

  lower_limit = min(data)

  for i in range(int(num_intervals)):
     upper_limit = lower_limit + amplitude
     upper_limit = round(upper_limit, 2)

     intervals.append((lower_limit, upper_limit))
        
     lower_limit = upper_limit
    
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

def calculate_absolute_frequency(data):
    numbers = sorted(data)
    intervals = defined_intervals(data)

    absolute_frequency = []

    for interval in intervals:
       limit_lower, limit_upper = interval
       count = sum(limit_lower <= num < limit_upper for num in numbers )
       absolute_frequency.append(count)

    return absolute_frequency 

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
       
def calculate_cumulative_frequency(data):
   absolute_frequency = calculate_absolute_frequency(data)

   cumulative_frequency = []
   cumulative_sum = 0

   for freq in absolute_frequency:
      cumulative_sum += freq
      cumulative_frequency.append(cumulative_sum)
  
   return cumulative_frequency
   

# Write your details here (numbers)
data  =  [
	0.06, 0.9, 0.08, 0.65, 0.07, 0.17, 0.28, 0.72, 0.78, 0.51, 0.61, 0.86, 0.6,
	0.76, 0.53, 0.16, 0.88, 0.68, 0.96, 0.77, 0.41, 0.74, 0.08, 0.67, 0.46, 0.37,
	0.47, 0.86, 0.45, 0.06, 0.82, 0.81, 0.45, 0.41, 0.21, 0.52, 0.59, 0.6, 0.96,
	0.55, 0.87, 0.99, 0.07, 0.17, 0.45, 0.59, 0.52, 0.61, 0.17, 0.62, 0.35, 0.38,
	0.28, 0.45, 0.46, 0.53, 0.16, 0.57, 0.2, 0.82, 0.65, 0.72,0.99,0.2
]


print("Rango: ", calculate_range(data))
print("Amplitud: ", calculate_amplitude(data))
print("Marca de clase", defined_markofclass(data))
print(order_numbers(data))
print("frec abs",calculate_absolute_frequency(data))
print(calculate_cumulative_frequency(data))


intervals = defined_intervals(data)
marks_of_class = defined_markofclass(data) 
absolute_frequency = calculate_absolute_frequency(data)  
real_limits_values = real_limits(data, gap=0.005)
 



print("""
| Clase |   Numero de intervalos  | Limite real         |  Marca de clase  |  Frecuencia absoluta  | Frecuencia acumulada |
|       |-------------------------|---------------------|                  |-----------------------|----------------------|
|       |  Superior  |  Inferior  | Superior | Inferior |                  |  Simple  |  Relativa  | Simple | Relativa    |   
-------------------------------------------------------------------------------------------------------------""")
for i, (interval, mark_of_class, freq_abs, real_limit) in enumerate(zip(intervals, marks_of_class, absolute_frequency, real_limits_values), start=1):
    real_limit_lower, real_limit_upper = real_limit
    print(
        f"| {i:<5} | {interval[0]:<10} | {interval[1]:<10} | {real_limit_lower:<10} | {real_limit_upper:<10} | {mark_of_class:<16} | {freq_abs:<8} | {'{:0.2%}'.format(freq_abs / len(data)):<10} |"
    )