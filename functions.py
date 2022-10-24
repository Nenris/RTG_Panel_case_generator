import constants
import random
import datetime
import csv


# Функции для получени параметров имени кампании и дат Reshuffle_date и Next_reshuffle_date
def get_campaign_type():
    return random.choice(constants.campaign_type)


def get_channel():
    return random.choice(constants.channel)


def get_app():
    return random.choice(constants.app)


def get_platform():
    return random.choice(constants.platform)


def get_geo(channel):
    if channel == 'RM':
        geo_id = random.randint(0,2)
        return constants.geo[geo_id]
    else:
        return random.choice(constants.geo)


def get_days_of_inactivity():
    return random.choice(constants.days_of_inactivity)


def get_payer_type():
    return random.choice(constants.payer_type)


def get_type():
    return random.choice(constants.rotation_type)


def get_opt():
    return random.choice(constants.opt)


def get_custom():
    return random.choice(constants.custom)


def get_creative_type(channel):
    if channel == 'FB':
        return random.choice(constants.creative_type)
    else:
        return ''


# Дата только для нейминга кампании, к reshuffle_date и next_reshuffle_date не имеет отношения
def get_date():
    month = random.choice(constants.month)
    if month == 'Feb':
        day = str(random.randint(1, 29))
    elif month in ('Apr', 'June', 'Sep', 'Nov'):
        day = str(random.randint(1, 30))
    else:
        day = str(random.randint(1, 31))
    campaign_date = month + day
    return campaign_date


# Собираем имя кампании из составляющих
def get_campaign_name():
    name = ''
    campaign_type = get_campaign_type()
    channel = get_channel()
    platform = get_platform()
    app = get_app() + '-' + platform
    geo = get_geo(channel)
    days_of_inactivity = get_days_of_inactivity()
    payer_type = get_payer_type()
    rotation_type = get_type()
    opt = get_opt()
    custom = get_custom()
    creative_type = get_creative_type(channel)
    campaign_date = get_date()

    name_parts = [campaign_type,'Ch-' + channel, 'App-' + app, 'Geo-' + geo, 'Payers-' + payer_type, 'Inactive-' + days_of_inactivity, 'Type-' + rotation_type, opt, custom, creative_type, 'Dt-' + campaign_date]
    for part in name_parts:
        name += part
        if name_parts.index(part) != len(name_parts) - 1 and part != '':
            name += '_'
    return name


# Reshuffle_date
def get_start_date(delta):
    today = datetime.date.today()
    start_date = (today + datetime.timedelta(days = delta)).strftime("%d.%m.%Y")
    return start_date


# Next_reshuffle_date
def get_end_date(start_date, delta):
    today = datetime.datetime.strptime(start_date, "%d.%m.%Y")
    end_date = (today + datetime.timedelta(days = delta)).strftime("%d.%m.%Y")
    return end_date


# Собираем имя кампании и даты начала и конца для последующей записи в файл
def create_row(name, start_date, end_date):
    row = [name, start_date, end_date]
    return row


# Создаем новый файл с кейсом
def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as result:
        writer = csv.writer(result)
        writer.writerow(('campaign_name', 'reshuffle_date', 'next_reshuffle_date'))
        result.close()


# Дописываем новые строки в существующий файл
def write_to_file(file_name, row):
    with open(file_name, 'a', encoding='utf-8', newline='') as result:
        writer = csv.writer(result)
        writer.writerow(row)
    result.close()


# Кейс 1. Тесты для успешного импорта
def successful_import(row_number):
    file_name = 'successful_import.csv'
    create_file(file_name)
    for _ in range(row_number):
        campaign_name = get_campaign_name()
        start_date = get_start_date(0)
        end_date = get_end_date(start_date, 1)
        row = create_row(campaign_name, start_date, end_date)
        write_to_file(file_name, row)


# Кейс 2. Тесты успешно импортируются, в файле есть по 2 периода для каждой кампании
def successful_import_2_periods_per_campaign(row_number):
    file_name = 'successful_import_2_periods_per_campaign.csv'
    create_file(file_name)
    while row_number > 0:
        campaign_name = get_campaign_name()
        start_date = get_start_date(0)
        end_date = get_end_date(start_date, 1)
        row = create_row(campaign_name, start_date, end_date)
        write_to_file(file_name, row)
        row_number -= 1
        if row_number == 0:
            break
        start_date = get_start_date(2)
        end_date = get_end_date(start_date, 1)
        row = create_row(campaign_name, start_date, end_date)
        write_to_file(file_name, row)
        row_number -= 1


# Кейс 3. 2 файла, некоторый тесты из файла 1 повторяются в файле 2
def duplicates(row_number):
    duplicate_row = 1
    file_name_1 = 'duplicates_1.csv'
    file_name_2 = 'duplicates_2.csv'
    create_file(file_name_1)
    create_file(file_name_2)
    # Цикл создает набор случайных записей в два файла, при этом гарантированно копирует случайные строки из файла 1 в файл 2 (каждую n строку,
    # при этом n - случайное число в диапазоне от 2 до общего числа строк, или до 10 (смотря что меньше). Если в файле всего 1 строка, она будет скопирована)
    if row_number > 1 and row_number <= 10:
        duplicate_row = random.randint(2, row_number)
    elif row_number > 10:
        duplicate_row = random.randint(2, 10)
    counter = 0
    for _ in range(row_number):
        campaign_name = get_campaign_name()
        start_date = get_start_date(0)
        end_date = get_end_date(start_date, 1)
        row = create_row(campaign_name, start_date, end_date)
        write_to_file(file_name_1, row)
        counter += 1
        if counter % duplicate_row == 0:
            write_to_file(file_name_2, row)
        else:
            campaign_name = get_campaign_name()
            start_date = get_start_date(0)
            end_date = get_end_date(start_date, 1)
            row = create_row(campaign_name, start_date, end_date)
            write_to_file(file_name_2, row)


# Кейс 4. Импорт файла, в котором встречаются тесты для одной кампании с пересекающимися периодами
def intersections_same_file(row_number):
    file_name = 'intersections_same_file.csv'
    duplicate_row = 1
    if row_number > 1 and row_number <= 10:
        duplicate_row = random.randint(2, row_number)
    elif row_number > 5:
        duplicate_row = random.randint(2, 5)
    create_file(file_name)
    for counter in range(row_number):
        campaign_name = get_campaign_name()
        start_date = get_start_date(0)
        end_date = get_end_date(start_date, 3)
        row = create_row(campaign_name, start_date, end_date)
        write_to_file(file_name, row)
        counter += 1
        if counter % duplicate_row == 0 and counter < row_number:
            start_date = get_start_date(random.choice([i for i in range(-2, 2) if i != 0]))
            end_date = get_end_date(start_date, 3)
            row = create_row(campaign_name, start_date, end_date)
            write_to_file(file_name, row)
            counter += 1


# Кейс 5. Импорт двух файлов, в которых встречаются тесты для одной кампании с пересекающимися периодами
def intersections_different_files(row_number):
    file_name_1 = 'intersections_different_files_1.csv'
    file_name_2 = 'intersections_different_files_2.csv'
    duplicate_row = 1
    if row_number > 1 and row_number <= 10:
        duplicate_row = random.randint(2, row_number)
    elif row_number > 5:
        duplicate_row = random.randint(2, 5)
    create_file(file_name_1)
    create_file(file_name_2)
    for counter in range(row_number):
        campaign_name = get_campaign_name()
        start_date = get_start_date(0)
        end_date = get_end_date(start_date, 3)
        row = create_row(campaign_name, start_date, end_date)
        write_to_file(file_name_1, row)
        counter += 1
        if counter % duplicate_row == 0 and counter < row_number:
            start_date = get_start_date(random.choice([i for i in range(-2, 2) if i != 0]))
            end_date = get_end_date(start_date, 3)
            row = create_row(campaign_name, start_date, end_date)
            write_to_file(file_name_2, row)
            counter += 1
        else:
            campaign_name = get_campaign_name()
            start_date = get_start_date(random.choice([i for i in range(-2, 2) if i != 0]))
            end_date = get_end_date(start_date, 3)
            row = create_row(campaign_name, start_date, end_date)
            write_to_file(file_name_2, row)
            counter += 1
