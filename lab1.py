#Натуральные числа, начинающиеся с нечетной цифры и содержащие не более 2 четных цифр.
#Для каждого числа через тире вывести прописью первую цифру и четные цифры.
start_num = ['1','3','5','7','9']
num = ['1','2','3','4','5','6','7','8','9','0']
lines = []
numbers = []

with open('NaL.txt') as f:
    file = f.read()
    for i in file.split():
        lines.append(i)

for line in lines:
    for i in range(len(line)):
        if line[i] in start_num:
            number = line[i]
            even = 0
            while even < 2:
                try:
                    if line[i + 1] in num:
                        if int(line[i + 1]) % 2 == 0:
                            even += 1
                            if even == 2:
                                number += line[i + 1]
                                break
                            else:
                                number += line[i + 1]
                    if line[i + 1] not in num:
                        break
                    i += 1
                except IndexError:
                    break
            if even in [1, 2]:
                numbers.append(number)

for i in numbers:
    output = str(i) + ' - '
    for j in i:
        if int(j) % 2 == 0:
            output += j
    print(output)
