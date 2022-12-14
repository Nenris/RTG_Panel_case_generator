from functions import (
    successful_import,
    successful_import_2_periods_per_campaign,
    duplicates,
    intersections_same_file,
    intersections_different_files,
    end_date_before_start_date,
    test_with_typo,
)


print("Какой кейс сгенерировать?")
print("1. Успешный импорт тестов (разные кампании, без повторов одной кампании)")
print("2. Успешный импорт тестов (2 разных периода для кампании)")
print("3. Импорт дубликатов")
print("4. Тесты с пересекающимися периодами в одном файле")
print("5. Тесты с пересекающимися периодами в разных файлах")
print("6. Импорт теста с датой завершения раньше даты начала")
print("7. Импорт тестов с ошибками форматирования (в названии кампании или датах)")
print("0. Все кейсы (по 20 строк на кейс)")
mode = int(input())


if mode == 1:  # Успешный импорт тестов (разные кампании, без повторов одной кампании)
    print("Сколько строк сгенерировать?")
    row_number = int(input())
    successful_import(row_number)
elif mode == 2:  # Успешный импорт тестов (разные кампании и разные периоды для одной кампании)
    print("Сколько строк сгенерировать?")
    row_number = int(input())
    successful_import_2_periods_per_campaign(row_number)
elif mode == 3:  # Импорт дубликатов
    print("Сколько строк сгенерировать?")
    row_number = int(input())
    duplicates(row_number)
elif mode == 4:  # Импорт файла, в котором встречаются тесты для одной кампании с пересекающимися периодами
    print("Сколько строк сгенерировать?")
    row_number = int(input())
    intersections_same_file(row_number)
elif mode == 5:  # Импорт файлов, в которых встречаются тесты для одной кампании с пересекающимися периодами
    print("Сколько строк сгенерировать?")
    row_number = int(input())
    intersections_different_files(row_number)
elif mode == 6:  # Импорт теста с датой завершения раньше даты началаи
    print("Сколько строк сгенерировать?")
    row_number = int(input())
    end_date_before_start_date(row_number)
elif mode == 7:  # Импорт теста с опечаткой
    print("Сколько строк сгенерировать?")
    row_number = int(input())
    test_with_typo(row_number)
elif mode == 0:  # Создание всех кейсов
    row_number = 20
    successful_import(row_number)
    successful_import_2_periods_per_campaign(row_number)
    duplicates(row_number)
    intersections_same_file(row_number)
    intersections_different_files(row_number)
    end_date_before_start_date(row_number)
    test_with_typo(row_number)
