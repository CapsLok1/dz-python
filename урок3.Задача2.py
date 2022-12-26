# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


list1 = list(map(int,input().split()))
if len(list1)%2==0:
    for i in range(len(list1)//2):
        summ = int(list1[0])*int(list1[-1])
        print(summ, end=' ')
        del list1[0], list1[-1]
else:
    for i in range((len(list1)+1)//2):
        if len(list1)>1:
            summ = int(list1[0])*int(list1[-1])
            print(summ, end=' ')
            del list1[0], list1[-1]
        elif len(list1)==1:
            summ = list1[0]**2
            print(summ)