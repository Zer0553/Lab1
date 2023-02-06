start_num = ['1','3','5','7','9']
num = ['1','2','3','4','5','6','7','8','9','0']
lines = []
numbers = []


def number_to_words(n):
    f = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
    6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    return f.get(n)


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
    output = number_to_words(int(i[0]))
    for j in i:
        if int(j) % 2 == 0:
            output += '-' + number_to_words(int(j))
    print(output)
