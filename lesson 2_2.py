#name = input('Введите ваше имя: ')
#if name == 'Niki':
#    print('Привет, админ. Что-то забыл?')
#else:
#    print("Привет", name)

#number = int(input("Введите число: "))  # Fizz, Buzz, FizzBuzz
# number % 3 == 0 and number % 5 == 0:
#    print('FizzBuzz')
#elif number % 3 == 0:
#    print('Fizz')
#elif number % 5 == 0:
#    print('Buzz')
#else:
#    print('Число не подходит')

# Домашняя работа "Условная конструкция. Операторы if, elif, else"
first = input('Введи первое число: ')
second = input('Введи второе число: ')
third = input('Введи третье число: ')
if first == second == third:
    print(3,'Все числа равны')
elif first == second or second == third or first == third:
    print(2,'Два числа равны')
else: print(0,'Равных нет')
