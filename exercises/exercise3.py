import random


def create_rundom_array(size: int, min: int, max: int) -> list:
    numbers = [i for i in range(random.randint(1, size))]
    return list(map(lambda: random.randint(min, max), numbers))


def sum_odd_indexes():
    print('Array created programmatically, sum of odd indexes: ')
    numbers = create_rundom_array(10, -10, 10)
    print('Generated array: ', numbers)
    odd_sum = 0
    for i, number in enumerate(numbers):
        if (i % 2 != 0):
            odd_sum += number
    print(odd_sum)


def sum_of_pairs():
    print('Array created programmatically, returns an array sums of pairs of elements (first and last, second and last - 1, etc.): ')
    numbers = create_rundom_array(10, -10, 10)
    print('Generated array: ', numbers)
    sum_of_pairs = []
    i, j = 0, len(numbers) - 1
    while (i <= j):
        sum_of_pairs.append(numbers[i] + numbers[j])
        i, j = i + 1, j - 1
    print(sum_of_pairs)


def fractional_part_difference():
    print('Array of real numbers created programmatically, return the difference of two numbers fractional part (min, max): ')
    numbers = [i for i in range(random.randint(1, 10))]
    generate_numbers = list(map(lambda: round(random.random()*10, 2), numbers))
    print('Generated array: ', generate_numbers)
    fractional_part = sorted(list(map(lambda value: round(value % 1, 2), generate_numbers)))
    print('Fractional parts:    ', fractional_part)
    print(round(fractional_part[-1] - fractional_part[0], 2))


def number_in_binarry():
    print(bin(int(input('Enter number for converting to binary form: '))).replace("0b", ""))


def fibonacci_list():
    number = int(input('Enter number N for get fibonacci sequence in (-N, N): '))

    def fibonacci(n):
        if (n in {0, 1}):
            return n
        elif (n == -1):
            return 1
        elif (n > 0):
            return fibonacci(n - 1) + fibonacci(n - 2)
        else:
            return fibonacci(n + 2) - fibonacci(n + 1)

    print([fibonacci(n) for n in range(number * -1, number + 1)])


exercise_3 = [sum_odd_indexes, sum_of_pairs, fractional_part_difference, number_in_binarry, fibonacci_list]
