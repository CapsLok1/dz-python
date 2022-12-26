# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
def fibonacci(n): # ф-ция чисел фибоначи
    if n in (1, 2):
        return 1
    if n == 0:
        return 0
    return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Введите число"))
lst = [fibonacci(i) for i in range(0, n+1)] # создаем список из чисел фибоначи
lst = lst[::-1] + lst[1:] # создается список из самого себя(сначала с последнего до первого эл)
                            # потом со второго(т.к. индексация с 0) по последний

for i in range(len(lst)): #добавляем в нужные места ' - '
    if i <=len(lst)//2+1 and i%2==0:
        lst[i]*=-1

print(lst, '\n')
