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
### Создайте функцию fib(n), генерирующую n чисел Фибоначчи с минимальными затратами ресурсов. Для реализации этой функции потребуется обратиться к инструкции yield (Она не сохраняет в оперативной памяти огромную последовательность, а дает возможность “доставать” промежуточные результаты по одному). Результатом решения задачи будет листинг кода и вывод в консоль с числом Фибоначчи от 200

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

Функция fib — это генератор, который выдаёт нужное количество чисел Фибоначчи по одному, используя yield
В памяти хранятся только два числа, поэтому даже при больших n расход памяти минимальный
Мы получили 200-е число, просто взяв последний элемент из списка 200 чисел

## Самостоятельная работа №2
### К коду предыдущей задачи добавьте запоминание каждого числа Фибоначчи в файл “fib.txt”, при этом каждое число должно находиться на отдельной строчке. Результатом выполнения задачи будет листинг кода и скриншот получившегося файла

```
def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

with open("fib.txt", "w", encoding="utf-8") as файл:
    for число in fib(200):
        файл.write(str(число) + "\n")

print("200:", list(fib(200))[-1])

```
### Результат.
![Меню](https://github.com/trueformalucard/-_7/blob/main/sam2.jpg)

## Выводы
open("expenses.txt", "a") - открытие файла для добавления данных
file.write() - запись данных в файл
file.readlines() - чтение всех строк из файлаю

## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит статистику по тексту: количество букв латинского алфавита; число слов; число строк

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
![Меню](https://github.com/trueformalucard/Program_Inj/blob/Theme_11/samrab2.png)
![Меню](https://github.com/trueformalucard/Program_Inj/blob/Theme_11/samrab2.1.png)

## Выводы
Функция fib — это генератор, который выдаёт нужное количество чисел Фибоначчи по одному с помощью yield
В памяти хранятся только два числа, поэтому расход ресурсов остаётся минимальным даже при больших значениях n
Все 200 чисел последовательно записаны в файл fib.txt — каждое на отдельной строке
200-е число Фибоначчи равно 280571172992510140037611932413038677189525

## Лабораторная работа №1
### Простой итератор, но у него нет гибкой настройки, например его нельзя развернуть. Он работает просто как next(), но нет prev()

```
numbers = [0,1,2,3,4,5]
for item in numbers:
    print(item)
```
### Результат.
![Меню](https://github.com/trueformalucard/Program_Inj/blob/Theme_11/test1.png)

## Лабораторная работа №2
### Класс итератор с гибкой настройкой и удобными применением

```
class CountDown:
    def __init__(self,start):
        self.count = start + 1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.count -= 1
        if self.count < 0:
            raise StopIteration
        return self.count
    

if __name__ == '__main__':
    counter = CountDown(5)
    for i in counter:
        print(i)
        

```
### Результат.
![Меню](https://github.com/trueformalucard/Program_Inj/blob/Theme_11/test2.png)

## Выводы
Метод __init__ задаёт начальное значение счётчика
Метод __iter__ возвращает сам объект (self), благодаря чему класс становится итерируемым
Метод __next__ содержит основную логику: уменьшает счётчик, возвращает текущее значение и выбрасывает StopIteration, когда доходим до 0 — именно это останавливает цикл for автоматически

## Лабораторная работа №3
### Генератор списка
```
a = [i ** 2 for i in range(1, 5)]

print('a - ', a)
for i in a:
    print(i)

print('inter(a) - ', iter(a))
for i in a:
    print(i)

```
### Результат.
![Меню](https://github.com/trueformalucard/Program_Inj/blob/Theme_11/test3.png)

## Выводы
a = [i ** 2 for i in range(1, 5)] создаёт список квадратов чисел — сам список является итерируемым объектом
Функция iter(a) возвращает отдельный объект-итератор (типа list_iterator), который «помнит» своё текущее положение при проходе по элементам
Циклы for i in a: используют этот механизм автоматически: Python внутри вызывает iter(a), а затем многократно вызывает __next__() у полученного итератора, пока не получит StopIteration

## Лабораторная работа №4
### Выражения генераторы

```
b = (i ** 2 for i in range(1, 5))
print(b)
print('first')
for i in b:
    print(i)
print('second')
for i in b:
    print(i)
```
### Результат.
![Меню](https://github.com/trueformalucard/Program_Inj/blob/Theme_11/test4.png)

## Выводы
b = (i ** 2 for i in range(1, 5)) создаёт генератор
first — выводит квадраты
second — пустой, потому что генератор уже исчерпан

## Лабораторная работа №5
### Такой же счетчик, как и в первом задании, только это генератор и использует yield
```
def countdown(count):
    while count >= 0:
        yield count
        count -= 1


if __name__ == '__main__':
    counter = countdown(5)
    for i in counter:
        print(i)
```
### Результат.
![Меню](https://github.com/trueformalucard/Program_Inj/blob/Theme_11/test5.png)

## Выводы
Функция countdown реализована как генератор с помощью yield
В цикле while count > 0 она по одному выдаёт числа от заданного значения до 1, а затем 0
Благодаря yield функция не создаёт список в памяти, а генерирует значения «на лету» — это экономит память и делает код лаконичным
При запуске через for i in counter: цикл автоматически получает значения по одному, пока генератор не завершится
