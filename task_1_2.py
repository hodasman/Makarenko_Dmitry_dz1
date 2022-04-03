list = []
list_sum = []
for number in range(1, 1000, 2):
    number = number**3
    list.append (number)
for number in list:
     sum = 0
     number1 = number
     while number1 > 0:
         digit = number1 % 10
         sum = sum + digit
         number1 = number1 // 10
     if sum % 7 == 0:
         list_sum.append(number)
a = 0
for x in list_sum:
    a += x
print(a) # Первый ответ

list_b = []
list_sum_b = []
for number in list:
    number_b = number + 17
    list_b.append(number_b)
for number in list_b:
     sum = 0
     number1 = number
     while number1 > 0:
         digit = number1 % 10
         sum = sum + digit
         number1 = number1 // 10
     if sum % 7 == 0:
         list_sum_b.append(number)
b = 0
for x in list_sum_b:
    b += x
print(b) # Второй ответ

