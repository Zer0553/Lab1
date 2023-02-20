# Натуральные числа, начинающиеся с нечетной цифры и содержащие не более 2 четных цифр.
# Для каждого числа через тире вывести прописью первую цифру и четные цифры.

buffer_len = 1
work_buffer = ''
numbers = []
start_num = ['1', '3', '5', '7', '9']


def words(n):
    f = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
         6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    return f.get(n)


with open('test.txt', 'r') as f:
    buffer = f.read(buffer_len)
    if not buffer:
        print('Файл пуст, пожалуйста выберите другой файл')
    while buffer:
        while '0' <= buffer <= '9':
            if '0' <= buffer <= '9':
                work_buffer += buffer
            buffer = f.read(buffer_len)
        if len(work_buffer) > 0:
            if work_buffer[0] in start_num:
                if work_buffer[0] in start_num:
                    even = 0
                    for j in work_buffer:
                        if int(j) % 2 == 0:
                            even += 1
                    if even <= 2:
                        numbers.append(work_buffer)
        work_buffer = ''
        buffer = f.read(buffer_len)
    if not numbers:
        print('Нет подходящих чисел')
    else:
        print(numbers)
        for i in numbers:
            p = i + ' - ' + words(int(i[0])) + ' -'
            answer = []
            for j in i:
                if int(j) % 2 == 0:
                    if words(int(j)) not in answer:
                        answer.append(words(int(j)))
                        answer.append('-')
            try:
                answer[len(answer) - 1] = ''
            except IndexError:
                continue
            print(p, *answer)
