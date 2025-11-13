import code_blocks_aux as cod

print('Creating a random number from 5 to 10:', cod.random_number_range(5,10))

print('Creating 3 random numbers:', cod.random_number(3))

print('Creating a random number from 10 to 30:', cod.random_number_range(10, 30))

countdown_text = 'Counting down from 10 until Fire: '
print(countdown_text, end='')
cod.countdown(10, 0,-1)

range = int(input('Enter the number range to sum: '))
print(f'Printing the sum of the even numbers within the chosen range ({range}):', cod.sum_pairs(range))

number_to_mutiply = int(input('Please, enter the number to display the multiplication table: '))
print(f'Printing the multiplication table for {number_to_mutiply}:')
cod.multiplication_table(number_to_mutiply)