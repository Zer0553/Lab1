#Натуральные числа, начинающиеся с нечетной цифры и содержащие не более 2 четных цифр.
#Для каждого числа через тире вывести прописью первую цифру и четные цифры.
start_num = ['1','3','5','7','9']
num = ['1','2','3','4','5','6','7','8','9','0']
lines = []
numbers = []


def words(n):
    f = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
         6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    return f.get(n)


with open('NaL.txt') as f:
    file = f.read()
    for line in file.split('\n'):
        lines.append(line)

for line in lines:
    h = 0
    for i in range(len(line)):
        if h > 0:
            h -= 1
            break
        else:
            if line[i] in start_num:
                number = line[i]
                h = 1
                while True:
                    try:
                        if line[i + h] in num:
                            number += line[i + h]
                        if line[i + h] not in num:
                            break
                        h += 1
                    except IndexError:
                        break
                numbers.append(number)
                
nnumbers = []

for i in numbers:
    even = 0
    for j in i:
        if int(j) % 2 == 0:
            even += 1
    if even == 2:
        nnumbers.append(i)


for i in nnumbers:
    output = str(i) + ' - ' + words(int(i[0]))
    for j in i:
        if int(j) % 2 == 0:
            output += ' ' + words(int(j))
    print(output)
