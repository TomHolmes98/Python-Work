def print_even_numbers(num_one, num_two):
    for number in range(num_one, num_two):
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

print(print_even_numbers(20, 40))