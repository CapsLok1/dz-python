# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.\

num = int(input("Введиет число"))
list1 = []
while num!=0:
    for i in range(2,num+1):
        if num%i==0:
            list1.append(i)
            break
    num//=list1[-1]
print(list1)