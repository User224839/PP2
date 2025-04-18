import psycopg2
import csv

# Подключение к базе
conn = psycopg2.connect(
    host="localhost",
    port=1234,
    database="postgres",  # Поменяй на свою базу если нужно
    user="postgres",
    password="simplenurik"
)
cur = conn.cursor()

# 1. Создание таблицы
cur.execute('''
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        phone VARCHAR(20) NOT NULL
    )
''')
conn.commit()

# 2. Загрузка данных из CSV
def load_from_csv(path):
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
                (row['username'], row['phone'])
            )
    conn.commit()

# 3. Добавление вручную
def add_user():
    username = input("Enter username: ")
    phone = input("Enter phone: ")
    cur.execute(
        "INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
        (username, phone)
    )
    conn.commit()

# 4. Обновление данных
def update_user():
    old_name = input("Enter username you want to update: ")
    new_name = input("Enter new username: ")
    new_phone = input("Enter new phone: ")
    cur.execute(
        "UPDATE phonebook SET username = %s, phone = %s WHERE username = %s",
        (new_name, new_phone, old_name)
    )
    conn.commit()

# 5. Поиск
def search_users():
    pattern = input("Enter search pattern (part of name or phone): ")
    cur.execute(
        "SELECT * FROM phonebook WHERE username ILIKE %s OR phone ILIKE %s",
        (f"%{pattern}%", f"%{pattern}%")
    )
    results = cur.fetchall()
    for row in results:
        print(row)

# 6. Удаление
def delete_user():
    username = input("Enter username to delete: ")
    cur.execute("DELETE FROM phonebook WHERE username = %s", (username,))
    conn.commit()

# Главное меню
def main():
    while True:
        print("\nPhoneBook Manager")
        print("1. Load from CSV")
        print("2. Add user")
        print("3. Update user")
        print("4. Search users")
        print("5. Delete user")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            path = input("Enter path to CSV: ")
            load_from_csv(path)
        elif choice == '2':
            add_user()
        elif choice == '3':
            update_user()
        elif choice == '4':
            search_users()
        elif choice == '5':
            delete_user()
        elif choice == '6':
            break
        else:
            print("Invalid choice")

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
