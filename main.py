import functions
import random


print('Какой кейс сгенерировать?')
print('1. Успешный импорт тестов (разные кампании, без повторов одной кампании)')
print('2. Успешный импорт тестов (2 разных периода для кампании)')
print('3. Импорт дубликатов')
print('4. Тесты с пересекающимися периодами в одном файле')
print('5. Тесты с пересекающимися периодами в разных файлах')
print('5. Импорт теста с датой завершения раньше даты начала')
print('6. Импорт тестов с ошибками форматирования (в названии кампании или датах)')
print('0. Все кейсы (по 20 строк на кейс)')
print()
mode = int(input())


if mode == 1: # Успешный импорт тестов (разные кампании, без повторов одной кампании)
    print('Сколько строк сгенерировать?')
    row_number = int(input())
    functions.successful_import(row_number)

elif mode == 2: # Успешный импорт тестов (разные кампании и разные периоды для одной кампании)
    print('Сколько строк сгенерировать?')
    row_number = int(input())
    functions.successful_import_2_periods_per_campaign(row_number)

elif mode == 3: # Импорт дубликатов
    print('Сколько строк сгенерировать?')
    row_number = int(input())
    functions.duplicates(row_number)

elif mode == 4: # Импорт файла, в котором встречаются тесты для одной кампании с пересекающимися периодами
    print('Сколько строк сгенерировать?')
    row_number = int(input())
    functions.intersections_same_file(row_number)

elif mode == 5:
    print('Сколько строк сгенерировать?')
    row_number = int(input())
    functions.intersections_different_files(row_number)
