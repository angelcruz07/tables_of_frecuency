import math
from decimal import Decimal, DecimalException,  ROUND_HALF_UP

# Order List of numbers
def order_number(numbers):
  return print(sorted(numbers))

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

  intervals =[]

  lower_limit = min(data)

  for i in range(int(num_intervals)):
     upper_limit = lower_limit + amplitude
     upper_limit = round(upper_limit, 2)

     intervals.append((lower_limit, upper_limit))
        
     lower_limit = upper_limit
    
  return intervals

def defined_markofclass(data):
   limit_lower = min(data)
   limit_upper = max(data)

   mark_of_class = limit_lower + limit_upper / 2

   return mark_of_class
 
# def calculate_limits_reals(interval, next_interval):
#     lower_limit, upper_limit = interval
#     next_lower_limit, next_upper_limit = next_interval
#     real_lower = (next_lower_limit + lower_limit) / 2
#     real_upper = (next_upper_limit + upper_limit) / 2
#     return real_lower, real_upper


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



intervals = defined_intervals(data)
print("""
| Clase |   Numero de intervalos  |
-----------------------------------
|       |  Superior  |  Inferior  |
-----------------------------------""")
for i, interval in enumerate(intervals, start=1):
    print(
        f"| {i:<5} | {interval[0]:<10} | {interval[1]:<10} |"
    )