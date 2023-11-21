import Connection

# Підключення до бази даних
connection = Connection.create_connection("postgres", "admin", "root", "localhost", "5432")
cursor = connection.cursor()

try:
    # Створення таблиці Студенти
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Students (
        student_code serial PRIMARY KEY,
        last_name varchar(255),
        first_name varchar(255),
        patronymic varchar(255),
        address varchar(255),
        phone_number varchar(13),
        course integer CHECK (course >= 1 AND course <= 4),
        faculty varchar(255) CHECK (faculty IN ('аграрного менеджменту', 'економіки', 'інформаційних технологій')),
        group_name varchar(255),
        is_head BOOLEAN
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
except Exception as e:
    print(f"Помилка при створенні таблиці Students: {e}")

try:
    # Створення таблиці Предмети
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Subjects (
        subject_code serial PRIMARY KEY,
        subject_name varchar(255),
        hours_per_semester integer,
        semesters_to_study integer
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
except Exception as e:
    print(f"Помилка при створенні таблиці Subjects: {e}")

try:
    # Створення таблиці Складання іспитів
    create_table_query = """
    CREATE TABLE IF NOT EXISTS ExamResults (
        exam_code serial PRIMARY KEY,
        exam_date DATE,
        student_code integer REFERENCES Students(student_code),
        subject_code integer REFERENCES Subjects(subject_code),
        grade integer CHECK (grade >= 2 AND grade <= 5)
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
except Exception as e:
    print(f"Помилка при створенні таблиці ExamResults: {e}")

cursor.close()
connection.close()
