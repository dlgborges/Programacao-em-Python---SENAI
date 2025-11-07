#testing variable scope

name = 'Julia'

def print_name():
    # print(nome)
    name = 'Joao'
    print(name)

print(name)
print_name()
print(name)

# Lambda function
# Assign to x the result of the quick lambda function
x = lambda y : y * 20
print(x(10))
