import my_module as mod

def market():
    name = input('Welcome! How can we call you? ')
    list_produtos = ['','a','b', 'c', 'd', 'e']
    values = [0, 55.0, 60.8, 12.88, 9.52, 5.44]
    mod.market_(list_produtos, values)
    list_pay = ['', '1 - PIX', '2 - CC', '3 - CD']
    mod.payments(list_pay)
    print(mod.farewell(name))

market()