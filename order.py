import math
import textwrap

# Order List of numbers
def order_numbers(numbers):
  return sorted(numbers)

# Class
def calculate_number_class(data):
   n = len(data)
   k = 1 + math.log2(n)
   if round(k) % 2 == 0:
        k += 1
   return  k

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
def defined_intervals(data, decimal_places = 2):
    num_intervals = calculate_number_class(data)
    amplitude = calculate_amplitude(data)

    intervals = []

    lower_limit = min(data)

    for i in range(int(num_intervals)):
        upper_limit = lower_limit + amplitude
        upper_limit = round(upper_limit, decimal_places)

        # Redondear el límite superior hacia arriba
        if decimal_places == 2  and lower_limit > 1:
         upper_limit = math.ceil(upper_limit)

        intervals.append((lower_limit, upper_limit ))
# Todo: check the param sum 0.01
        lower_limit = upper_limit + 0.01

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
# Todo: Check the result
def calculate_cumulative_frequency(data):
   absolute_frequency = calculate_absolute_frequency(data)

   cumulative_frequency = []
   cumulative_sum = 0

   for freq in absolute_frequency:
      cumulative_sum += freq
      cumulative_frequency.append(cumulative_sum)
  
   return cumulative_frequency


def calculate_complementary_frequency(data):
   total_observations = len(data)
   cumulative_frequency = calculate_cumulative_frequency(data)
   
   complementary_frequency =[total_observations - freq for freq in cumulative_frequency]

   return complementary_frequency


# Write your details here (numbers)
data  =  [
	0.06, 0.9, 0.08, 0.65, 0.07, 0.17, 0.28, 0.72, 0.78, 0.51, 0.61, 0.86, 0.6,
	0.76, 0.53, 0.16, 0.88, 0.68, 0.96, 0.77, 0.41, 0.74, 0.08, 0.67, 0.46, 0.37,
	0.47, 0.86, 0.45, 0.06, 0.82, 0.81, 0.45, 0.41, 0.21, 0.52, 0.59, 0.6, 0.96,
	0.55, 0.87, 0.99, 0.07, 0.17, 0.45, 0.59, 0.52, 0.61, 0.17, 0.62, 0.35, 0.38,
	0.28, 0.45, 0.46, 0.53, 0.16, 0.57, 0.2, 0.82, 0.65, 0.72,0.99,0.2
]

# data = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65]

print("Rango: ", calculate_range(data))

print("Amplitud: ", calculate_amplitude(data))


result = order_numbers(data)
columns = 5
wrapped_result = textwrap.wrap(', '.join(map(str, result)), width=columns*6)  # Asumiendo que cada número ocupa al menos 10 caracteres

print("Numeros ordenados:")
for row in wrapped_result:
    print(row)


intervals = defined_intervals(data, decimal_places=2)
marks_of_class = defined_markofclass(data)
absolute_frequency = calculate_absolute_frequency(data)
cumulative_frequency = calculate_cumulative_frequency(data)
complementary_frequency = calculate_complementary_frequency(data)

print("""
                                                Tabla de frecuencia
--------------------------------------------------------------------------------------------------------------------------
| Clase |   Numero de intervalos  |  Marca   |  Frecuencia absoluta  | Frecuencia acumulada  | Frecuencia complementaria |
|       |-------------------------|    de    |-----------------------|-----------------------|---------------------------|
|       |  Superior  |  Inferior  |  clase   |  Simple  |  Relativa  | Simple   | Relativa   |    Simple   |   Relativa  |   
--------------------------------------------------------------------------------------------------------------------------""")

for i, ( interval, mark_of_class, freq_abs, cumulative_frequency, complementary_frequency) in enumerate(zip(intervals, marks_of_class, absolute_frequency, cumulative_frequency, complementary_frequency), start=1):
    print(
        f"| {i:<5} | {interval[0]:<10} | {interval[1]:<10} | {mark_of_class:<8} | {freq_abs:<8} | {'{:0.2%}'.format(freq_abs / len(data)):<10} | {cumulative_frequency:<8} | {round(cumulative_frequency / len(data) * 100):<10} | {complementary_frequency:<11} | {round(complementary_frequency / len(data) * 100, 2):<11} |")