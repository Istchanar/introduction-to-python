import math
import random
import sympy


def fixed_point_pi():
    print(round(math.pi, len(input('Enter the precision, for output pi (ex. 0.1 -> 3.4): ')) - 2))


def number_factorization():
    number = int(input('Enter number for factorization: '))
    prime_numbers = set()
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            prime_numbers.add(divisor)
            number //= divisor
        else:
            divisor += 1
    if number > 1:
        prime_numbers.add(number)
    print(prime_numbers)


def unique_values():
    random_list = [random.randint(1, 10) for i in range(0, 10)]
    print('Generated array to return unique values:\n', random_list)
    print('Unique values:', [number for number in random_list if (random_list.count(number) < 2)])


def polynomial_in_file():
    file_path = 'exercises/text_data/polynomial_string.txt'
    power = int(input(
        f'Enter degree of a polynomial for generate and output to file {file_path} (polynomial coefficients sets auto from 0 to 100): '))
    polynomial = ''
    while (power >= 0):
        number = random.randint(0, 100)
        if (number == 0):
            power -= 1
            continue
        if (power > 1):
            polynomial += f'{number}*x**{power} + '
        elif (power == 1):
            polynomial += f'{number}*x + '
        elif (power == 0):
            polynomial += f'{number} = 0'
        power -= 1
    with open(file_path, 'w') as polynomial_string:
        polynomial_string.write(polynomial)


def polynomials_sum_from_files():
    path_prefix = 'exercises/text_data/'
    print(f'Result of sum to polynomials from {path_prefix}polynomial_first.txt, {path_prefix}polynomial_second.txt: ')

    path_first = f'{path_prefix}polynomial_first.txt'
    with open(path_first, 'r') as polynomial_first:
        string_one = polynomial_first.read().split('=')[0]

    path_second = f'{path_prefix}polynomial_second.txt'
    with open(path_second, 'r') as polynomial_second:
        string_two = polynomial_second.read().split('=')[0]

    path_result = f'{path_prefix}polynomial_sum.txt'
    with open(path_result, 'w') as polynomial_sum:
        polynomial_sum.writelines(f'{str(sympy.powsimp(string_one + "+" + string_two))} = 0')
    print(f'{str(sympy.powsimp(string_one + "+" + string_two))} = 0')


exercise_4 = [fixed_point_pi, number_factorization, unique_values, polynomial_in_file, polynomials_sum_from_files]
