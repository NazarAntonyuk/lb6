import Connection
from prettytable import PrettyTable

try:
    # Підключення до бази даних
    connection = Connection.create_connection("postgres", "admin", "root", "localhost", "5432")
    cursor = connection.cursor()

    def print_table(name_table):
        cursor.execute("SELECT * FROM " + name_table)
        data = cursor.fetchall()
        table = PrettyTable()
        table.field_names = [description[0] for description in cursor.description]
        for row in data:
            table.add_row(row)
        print(table)

    print_table("Students")
    print_table("Subjects")
    print_table("ExamResults")

except Exception as e:
    print(f"Помилка при виводі таблиць в консоль: {e}")

finally:
    # Закриття з'єднання
    cursor.close()
    connection.close()

