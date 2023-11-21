import Connection

#Подключение к базе данных
connection = Connection.create_connection("postgres", "admin", "root", "localhost", "5432")
cursor = connection.cursor()

try:


    # Додавання локомотивів
    locomotives_data = [
        ("00001", "Фастів", "вантажний", 2000),
        ("00002", "Козятин", "пасажирський", 2005),
        ("00003", "П’ятихатки", "вантажний", 2010),
        ("00004", "Фастів", "пасажирський", 2001),
        ("00005", "Козятин", "вантажний", 2010),
        ("00006", "П’ятихатки", "пасажирський", 2011),
        ("00007", "Фастів", "вантажний", 2004),
        ("00008", "Козятин", "пасажирський", 2002),
        ("00009", "П’ятихатки", "вантажний", 2007),
    ]

    insert_query = """
    INSERT INTO Locomotives (registration_number, registration_place, type, year_of_production)
    VALUES (%s, %s, %s, %s)
    ON CONFLICT (registration_number) DO NOTHING
    """

    for record in locomotives_data:
        cursor.execute(insert_query, record)

    connection.commit()

except Exception as e:
    print(f"Помилка при додаванні даних до таблиці Locomotives: {e}")

try:

    # Додавання бригад
    brigades_data = [
        ("1", "+380967638188"),
        ("2", "+380912123856"),
        ("3", "+380920627602")
    ]

    insert_query = """
    INSERT INTO Brigades (brigade_number, phone_number)
    VALUES (%s, %s)
    ON CONFLICT (brigade_number) DO NOTHING
    """

    for record in brigades_data:
        cursor.execute(insert_query, record)

    connection.commit()

except Exception as e:
    print(f"Помилка при додаванні даних до таблиці Brigades: {e}")

try:

    # Додавання робітників
    workers_data = [
        (1, 'Саченко', 'Едуард', 'Тихонович', 1, True, '1990-01-01'),
        (2, 'Петрук', 'Назар', 'Денисович', 1, False, '1991-02-02'),
        (3, 'Безкровний', 'Ілля', 'Валентинович', 1, False, '1992-03-03'),
        (4, 'Васильєв', 'Вадим', 'Миколайович', 2, False, '1993-04-11'),
        (5, 'Павлюк', 'Леонід', 'Сергійович', 2, False, '1994-02-02'),
        (6, 'Іванченко', 'Дмитро', 'Тарасович', 2, True, '1995-01-21'),
        (7, 'Шевченко', 'Артем', 'Олексійович', 3, False, '1996-07-02'),
        (8, 'Кравчук', 'Ігор', 'Михайлович', 3, True, '1997-01-08'),
        (9, 'Мельниченко', 'Михайло', 'Євгенович', 3, False, '1997-02-02')
    ]

    insert_query = """
    INSERT INTO Workers (worker_id, surname, name, patronymic, brigade_number, is_brigadier, birth_date)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (worker_id) DO NOTHING
    """

    for record in workers_data:
        cursor.execute(insert_query, record)

    connection.commit()

except Exception as e:
    print(f"Помилка при додаванні даних до таблиці Workers: {e}")

try:
    # Додавання даних для таблиці "Repairs"
    repairs_data = [
        (1, "поточний", "2023-01-15",10, 1000, 1),
        (2, "технічне обслуговування", "2023-02-20", 20, 1500, 2),
        (3, "позаплановий", "2023-03-25",15, 1200, 3),
        (4, "поточний", "2023-01-15",10, 1000, 1),
        (5, "технічне обслуговування", "2023-02-20", 30, 1500, 2),
        (6, "позаплановий", "2023-03-25", 15, 1200, 3),
        (7, "поточний", "2023-01-15",20, 1000, 1),
        (8, "позаплановий", "2023-02-20", 10, 1500, 2),
        (9, "поточний", "2023-03-25",30, 1200, 3),
        (1, "технічне обслуговування", "2023-01-15", 20, 1000, 1),
        (2, "поточний", "2023-02-20",15, 1500, 2),
    ]

    insert_query = """
    INSERT INTO Repairs (registration_number, type_of_repair, date_of_start, day_until_the_end, repair_cost, brigade_number)
    VALUES (%s, %s, %s, %s, %s, %s)
    ON CONFLICT (repair_id) DO NOTHING
    """

    for record in repairs_data:
        cursor.execute(insert_query, record)

    connection.commit()

except Exception as e:
    print(f"Помилка при додаванні даних до таблиці Repairs: {e}")

cursor.close()
connection.close()
