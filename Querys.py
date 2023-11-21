import Connection

# Підключення до бази даних
connection = Connection.create_connection("postgres", "admin", "root", "localhost", "5432")
cursor = connection.cursor()

def run_query(sql_query, params=None, comment=None):
    # Подключення к базе даних и выполнение запроса
    try:
        if comment:
            print(comment)  # Друкуємо коментар перед виконанням запиту
        cursor.execute(sql_query, params)

        # Получение результатов запроса
        records = cursor.fetchall()

        # Вывод результатов
        for record in records:
            print(record)

    except Exception as e:
        print(f"Помилка виконання запиту: {e}")

try:
    # Запит 1: Відобразити всіх студентів, які є старостами, відсортувати прізвища за алфавітом
    sql_query = """
    SELECT Students.student_code, Students.last_name, Students.first_name, Students.patronymic
    FROM Students
    WHERE Students.is_head = True
    ORDER BY Students.last_name;
    """
    run_query(sql_query, comment="Запит 1: Відобразити старост студентів (відсортовано за прізвищем)")

    # Запит 2: Порахувати середній бал для кожного студента (підсумковий запит)
    sql_query = """
    SELECT Students.student_code, Students.last_name, Students.first_name, Students.patronymic,
           AVG(ExamResults.grade) AS average_grade
    FROM Students
    LEFT JOIN ExamResults ON Students.student_code = ExamResults.student_code
    GROUP BY Students.student_code, Students.last_name, Students.first_name, Students.patronymic;
    """
    run_query(sql_query, comment="Запит 2: Середній бал для кожного студента")

    # Запит 3: Для кожного предмета порахувати загальну кількість годин, протягом яких він вивчається
    sql_query = """
    SELECT Subjects.subject_name, SUM(Subjects.hours_per_semester) AS total_hours
    FROM Subjects
    GROUP BY Subjects.subject_name;
    """
    run_query(sql_query, comment="Запит 3: Загальна кількість годин для кожного предмета")

    # Запит 4: Відобразити успішність студентів по обраному предмету (запит з параметром)
    subject_code = "101"  # Замініть це на код обраного предмету
    sql_query = """
    SELECT Students.student_code, Students.last_name, Students.first_name, Students.patronymic, ExamResults.grade
    FROM Students
    LEFT JOIN ExamResults ON Students.student_code = ExamResults.student_code
    WHERE ExamResults.subject_code = %s;
    """
    run_query(sql_query, (subject_code,), comment=f"Запит 4: Успішність студентів по предмету з кодом {subject_code}")

    # Запит 5: Порахувати кількість студентів на кожному факультеті (підсумковий запит)
    sql_query = """
    SELECT Students.faculty, COUNT(Students.student_code) AS student_count
    FROM Students
    GROUP BY Students.faculty;
    """
    run_query(sql_query, comment="Запит 5: Кількість студентів на кожному факультеті")

    # Запит 6: Відобразити оцінки кожного студента по кожному предмету (перехресний запит)
    sql_query = """
    SELECT Students.student_code, Students.last_name, Students.first_name, Students.patronymic, 
           Subjects.subject_name, ExamResults.grade
    FROM Students
    LEFT JOIN ExamResults ON Students.student_code = ExamResults.student_code
    LEFT JOIN Subjects ON ExamResults.subject_code = Subjects.subject_code
    ORDER BY Students.student_code, Subjects.subject_name;
    """
    run_query(sql_query, comment="Запит 6: Оцінки кожного студента по кожному предмету")

except Exception as e:
    print(f"Помилка виконання запиту: {e}")

# Закриття підключення
cursor.close()
connection.close()
