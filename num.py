import math
import textwrap

def order_numbers(numbers):
    return sorted(numbers)

def calculate_number_class(data):
    n = len(data)
    k = 1 + math.log2(n)
    if round(k) % 2 == 0:
        k += 1
    return  int(round(k))

def calculate_range(data):
    if len(data) == 0:
        return None
    else:
        return round(max(data) - min(data), 2)

def calculate_amplitude(data):
    range_number = calculate_range(data)
    count_class = calculate_number_class(data)
    return round(range_number / count_class, 2)

def defined_intervals(data, decimal_places=2):
    num_intervals = calculate_number_class(data)
    amplitude = calculate_amplitude(data)
    intervals = []

    lower_limit = min(data)

    for i in range(num_intervals):
        upper_limit = round(lower_limit + amplitude, decimal_places)

        if decimal_places == 2 and lower_limit > 1:
            upper_limit = math.ceil(upper_limit)

        intervals.append((lower_limit, upper_limit))
        lower_limit = upper_limit + 0.01  # Añadido un pequeño margen entre intervalos

    return intervals

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
    intervals = defined_intervals(data)
    absolute_frequency = []

    for interval in intervals:
        limit_lower, limit_upper = interval
        count = sum(limit_lower <= number <= limit_upper for number in data)
        absolute_frequency.append(count)

    return absolute_frequency

def calculate_cumulative_frequency(data):
    absolute_frequency = calculate_absolute_frequency(data)
    cumulative_frequency = [sum(absolute_frequency[:i+1]) for i in range(len(absolute_frequency))]
    return cumulative_frequency

def calculate_complementary_frequency(data):
    total_observations = len(data)
    cumulative_frequency = calculate_cumulative_frequency(data)
    complementary_frequency = [total_observations - freq for freq in cumulative_frequency]
    return complementary_frequency

def real_limits(data, gap):
    intervals = defined_intervals(data)
    real_limits = []

    for i in range(len(intervals)):
        lower_limit, upper_limit = intervals[i]
        real_lower_limit = lower_limit - gap / 2
        real_upper_limit = upper_limit + gap / 2
        real_limits.append((round(real_lower_limit, 3), round(real_upper_limit, 3)))

    return real_limits

def print_table(data):
    print("Tabla de frecuencia")
    print("--------------------------------------------------------------------------------------------------------------------")
    print("| Clase |  Número de Intervalos | Intervalos Reales  | Marca de Clase | Frecuencia Absoluta | Frecuencia Acumulada |")
    print("--------------------------------------------------------------------------------------------------------------------")

    intervals = defined_intervals(data)
    marks_of_class = defined_markofclass(data)
    absolute_frequency = calculate_absolute_frequency(data)
    cumulative_frequency = calculate_cumulative_frequency(data)

    for i, (interval, mark_of_class, freq_abs, cumulative_freq) in enumerate(zip(intervals, marks_of_class, absolute_frequency, cumulative_frequency), start=1):
        print(f"| {i:<5} | {interval} | {mark_of_class:<15} | {freq_abs:<20} | {cumulative_freq:<20} |")
    print("--------------------------------------------------------------------------------------------------------------------")

# Ejemplo de uso
data = [
    35, 42, 35, 36, 33, 23, 24, 33, 28, 21, 21, 21, 37, 29, 13, 11, 6, 32, 23, 14,
    18, 17, 24, 19, 28, 21, 31, 13, 12, 38, 14, 23, 45, 19, 33, 34, 28, 25, 26, 7,
    29, 11, 22, 9, 43, 36, 10, 4, 43, 30, 43, 29, 24, 29, 19, 18, 9, 36, 35, 10
]

print("Total de números:", len(data))
print("Rango:", calculate_range(data))
print("Amplitud:", calculate_amplitude(data))

result = order_numbers(data)
columns = 5
wrapped_result = textwrap.wrap(', '.join(map(str, result)), width=columns*6)

print("Números ordenados:")
for row in wrapped_result:
    print(row)

print_table(data)
