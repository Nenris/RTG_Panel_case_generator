import functions


print('Какой кейс сгенерировать?')
print('1. Успешный импорт тестов (разные кампании, без повторов одной кампании)')
print('2. Успешный импорт тестов (2 разных периода для кампании)')
print('3. Импорт дубликатов')
print('4. Тесты с пересекающимися периодами в одном файле')
print('5. Тесты с пересекающимися периодами в разных файлах')
print('6. Импорт теста с датой завершения раньше даты начала')
print('7. Импорт тестов с ошибками форматирования (в названии кампании или датах)')
print('9. Ссылка на документацию')
print('0. Все кейсы (по 20 строк на кейс)')
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

elif mode == 5: # Импорт файлов, в которых встречаются тесты для одной кампании с пересекающимися периодами
    print('Сколько строк сгенерировать?')
    row_number = int(input())
    functions.intersections_different_files(row_number)

elif mode == 6:  # Импорт теста с датой завершения раньше даты началаи
    print('Сколько строк сгенерировать?')
    row_number = int(input())
    functions.end_date_before_start_date(row_number)

elif mode == 7:  # Импорт теста с опечаткой
    print('Сколько строк сгенерировать?')
    row_number = int(input())
    functions.test_with_typo(row_number)

elif mode == 9:
    print('Структура наименования кампании: https://docs.google.com/spreadsheets/d/1aHG5jvSKhzxiozg1-p9P5fgxw_dliEL00v2VEr9DcAA/edit#gid=1913779860')
    print()
    print('ТЗ на разработку RTG Panel: https://knowledge.playrix.com/pages/viewpage.action?pageId=197891928')
    input()

elif mode == 0:
    row_number = 20
    functions.successful_import(row_number)
    functions.successful_import_2_periods_per_campaign(row_number)
    functions.duplicates(row_number)
    functions.intersections_same_file(row_number)
    functions.intersections_different_files(row_number)
    functions.end_date_before_start_date(row_number)
    functions.test_with_typo(row_number)