# task1/1. Реализуйте функцию, которая возвращает список из N уникальных случайных чисел в диапазоне от 1 до 1,000,000.

# task2/2. Есть строка в формате camelCase, например, «helloWorld». Нужно написать функцию, которая разобьет строку на слова, используя пробел.
Пример:
"helloWorld" => "hello World" 

# task3/3. Реализуйте функцию unique_in_order, которая принимает в качестве аргумента последовательность и возвращает список элементов без повторяющихся элементов, идущих подряд, сохраняя при этом исходный порядок элементов.
Примеры:
unique_in_order('AAAABBBCCDAABBB') должно вернуть ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD') должно вернуть ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3]) должно вернуть [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3)) должно вернуть [1, 2, 3]

# task4/4. Напишите функцию persistence, которая принимает положительный параметр num и возвращает его мультипликативную устойчивость, то есть количество раз, которое нужно умножить цифры в num, пока не получится однозначное число.
Примеры:
    • persistence(39) должно вернуть 3, потому что 39 = 27, 27 = 14, 1*4 = 4 и 4 - это однозначное число.
    • persistence(999) должно вернуть 4, потому что 999 = 729, 729 = 126, 126 = 12, и наконец 1*2 = 2.
    • persistence(4) должно вернуть 0, потому что 4 уже является однозначным числом.
