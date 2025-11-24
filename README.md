# Тема 11.
Отчет по Теме #11 выполнил(а):
- Улыбышев Артемий Александрович
- ИВТ-23-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | +  | + |
| Задание 2 | +  | + |
| Задание 3 | +  |   |
| Задание 4 | +  |   |
| Задание 5 | +  |   |


знак "+" - задание выполнено; знак "-" - задание не выполнено;

## Самостоятельная работа №1
### Создайте функцию fib(n), генерирующую n чисел Фибоначчи с минимальными затратами ресурсов. Для реализации этой функции потребуется обратиться к инструкции yield (Она не сохраняет в оперативной памяти огромную последовательность, а дает возможность “доставать” промежуточные результаты по одному). Результатом решения задачи будет листинг кода и вывод в консоль с числом Фибоначчи от 200.

```
def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

f200 = list(fib(200))[-1]

for i, num in enumerate(fib(10), 1):
    print(f"{i:2}: {num}")

print("\n200:")
print(f200)

```
### Результат.
![Меню](https://github.com/trueformalucard/Program_Inj/blob/Theme_11/samrab1.png)

## Выводы

with open() - открытие и автоматическое закрытие файла
text.split() - разделение текста на слова
max(word_count, key=word_count.get) - поиск самого частого слова

## Самостоятельная работа №2
### Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль.

```
def add_expense():
    amount = input("Введите сумму расхода: ")
    category = input("Введите категорию расхода: ")
    
    with open("expenses.txt", "a", encoding="utf-8") as file:
        file.write(f"{amount} - {category}\n")

def show_expenses():
    try:
        with open("expenses.txt", "r", encoding="utf-8") as file:
            expenses = file.readlines()
            
        if not expenses:
            print("Расходы отсутствуют")
            return
            
        print("Список расходов:")
        for expense in expenses:
            print(expense.strip())
    except FileNotFoundError:
        print("Файл с расходами не найден")

while True:
    print("\n1 - Добавить расход")
    print("2 - Показать расходы")
    print("3 - Выйти")
    
    choice = input("Выберите действие: ")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        break

```
### Результат.
![Меню](https://github.com/trueformalucard/-_7/blob/main/sam2.jpg)

## Выводы
open("expenses.txt", "a") - открытие файла для добавления данных
file.write() - запись данных в файл
file.readlines() - чтение всех строк из файлаю

## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит статистику по тексту: количество букв латинского алфавита; число слов; число строк.

```
with open("input.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

letter_count = 0
word_count = 0
line_count = len(lines)

for line in lines:
    for char in line:
        if char.isalpha() and char.isascii():
            letter_count += 1
    
    words = line.split()
    word_count += len(words)

print(f"Input file contains:")
print(f"{letter_count} letters")
print(f"{word_count} words")
print(f"{line_count} lines")


```
### Результат.
![Меню](https://github.com/trueformalucard/-_7/blob/main/sam3.jpg)

## Выводы
file.readlines() - чтение всех строк файла
char.isalpha() - проверка является ли символ буквой
line.split() - разделение строки на слова

## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками.

```
with open("input.txt", "r", encoding="utf-8") as file:
    banned_words = file.read().split()


text = "Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!!"


for banned_word in banned_words:
    start = 0
    while start < len(text):

        index = text.lower().find(banned_word.lower(), start)
        if index == -1:
            break

        stars = '*' * len(banned_word)
        text = text[:index] + stars + text[index + len(banned_word):]
        start = index + len(stars)

print("Результат:")
print(text)


```
### Результат.
![Меню](https://github.com/trueformalucard/-_7/blob/main/sam4.jpg)

## Выводы
file.read().split() - чтение запрещенных слов из файла в список
text.lower().find() - поиск слова в тексте без учета регистра
'*' * len(banned_word) - создание строки из звездочек одинаковой длины со словом

## Самостоятельная работа №5
### Напиши программу "Секретный дневник", которая позволяет записывать секретные сообщения в файл и читать их. Все сообщения хранятся в зашифрованном виде - каждая буква заменяется на следующую в алфавите.

```
def write_secret():
    message = input("Введите секретное сообщение: ")

    secret = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                secret += chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
            else:
                secret += chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
        else:
            secret += char

    with open("diary.txt", "a", encoding="utf-8") as file:
        file.write(secret + "\n")
    print("Сообщение записано в дневник!")


def read_secrets():
    try:
        with open("diary.txt", "r", encoding="utf-8") as file:
            secrets = file.readlines()

        if not secrets:
            print("Дневник пустой")
            return

        print("\nСекретные сообщения:")
        for i, secret in enumerate(secrets, 1):
            message = ""
            for char in secret.strip():
                if char.isalpha():
                    if char.islower():
                        message += chr((ord(char) - ord('a') - 1) % 26 + ord('a'))
                    else:
                        message += chr((ord(char) - ord('A') - 1) % 26 + ord('A'))
                else:
                    message += char
            print(f"{i}. {message}")
    except FileNotFoundError:
        print("Дневник не найден")


while True:
    print("\n1 - Записать секрет")
    print("2 - Прочитать секреты")
    print("3 - Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        write_secret()
    elif choice == "2":
        read_secrets()
    elif choice == "3":
        break


```
### Результат.
![Меню](https://github.com/trueformalucard/-_7/blob/main/sam5.jpg)

## Выводы
ord(char) - получение кода символа для шифрования
chr(code) - преобразование кода обратно в символ
open("diary.txt", "a") - добавление новых сообщений в файл

## Лабораторная работа №1
### Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк.

```

```
### Результат.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/Тема_7/lab1.jpg)



## Лабораторная работа №2
### Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().

```
file = open("input.txt", "r", encoding="utf-8")
first_line = file.readline()
print(first_line)
file.close()

```
### Результат.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/Тема_7/lab2.jpg)

## Выводы
open("myfile.txt", "r") - открытие файла для чтения
file.readline() - чтение первой строки
file.close() - закрытие файла

## Лабораторная работа №3
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().

```
file = open("input.txt", "r", encoding="utf-8")
lines = file.readlines()
print(lines)
file.close()

```
### Результат.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/Тема_7/lab3.jpg)

## Выводы
file.readlines() - чтение всех строк в список
print(lines) - вывод списка строк
file.close() - закрытие файла

## Лабораторная работа №4
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().

```
with open("input.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    print(lines)


```
### Результат.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/Тема_7/lab4.jpg)

## Выводы
with open() - автоматическое закрытие файла
file.readlines() - чтение всех строк
Автоматическое управление ресурсами

## Лабораторная работа №5
### Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().
```
with open("input.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())


```
### Результат.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/Тема_7/lab5.jpg)

## Выводы
for line in file: - построчное чтение файла
line.strip() - удаление символов перевода строки

## Лабораторная работа №6
### Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль.
```
with open("input.txt", "a", encoding="utf-8") as file:
    file.write("Новая добавленная строка\n")

with open("input.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)


```
### Результат.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/Тема_7/lab6.jpg)

## Выводы
open("myfile.txt", "a") - добавление данных в файл
file.write() - запись новой строки
file.read() - чтение всего содержимого

## Лабораторная работа №7
### Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого.
```
lines = ['one', 'two', 'three']
with open('myfile.txt', 'w', encoding="utf-8") as file:
    for line in lines:
        file.write('Cycle run ' + line + '\n')

with open('myfile.txt', 'r', encoding="utf-8") as file:
    print(file.read())


```
### Результат.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/Тема_7/lab7.jpg)

## Выводы
open("myfile.txt", "w") - перезапись файла
цикл for для записи списка
file.read() - проверка результата

## Лабораторная работа №8
### Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).
```
import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит:')
        print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
        print(f'Файлы: {", ".join([file for file in catalog[2]])}')
        print('.' * 40)

print_docs('C:/Users/GPC/Desktop')


```
### Результат.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/Тема_7/lab8.jpg)

## Выводы
os.walk(directory) - обход всех папок и файлов
catalog[1] - список поддиректорий
catalog[2] - список файлов в директории

## Лабораторная работа №9
### Реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько).
```
def find_longest_words():
    with open("input.txt", "r", encoding="utf-8") as file:
        words = file.read().split()

    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]

    print("Слова с максимальной длиной:")
    for word in longest_words:
        print(word)


find_longest_words()



```
### Результат.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/Тема_7/lab9.jpg)

## Выводы
file.read().split() - чтение и разделение на слова
max(len(word)) - поиск максимальной длины
Списочное выражение для фильтрации слов

## Лабораторная работа №10
### Создать csv-файл «rows_300.csv» со столбцами: №, Секунда, Микросекунда.
```
import csv
import datetime
import time

with open('rows_300.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['№', 'Секунда', 'Микросекунда'])

    for i in range(1, 301):
        writer.writerow([i, datetime.datetime.now().second, datetime.datetime.now().microsecond])
        time.sleep(0.01)


```
### Результат.
![Меню](https://github.com/paiNy66/proggramnaya-injeneriya/blob/Тема_7/lab10.jpg)

## Выводы
csv.writer() - создание writer для CSV
datetime.datetime.now() - получение текущего времени
time.sleep(0.01) - искусственная задержка
