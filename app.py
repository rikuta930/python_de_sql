import sqlite3


def find_all_users():
    connection = sqlite3.connect('camp.db')
    cursor = connection.cursor()
    sql = f"SELECT * FROM users"
    users = cursor.execute(sql).fetchall()
    connection.close()
    return users


def delete_user(name):
    connection = sqlite3.connect('camp.db')
    cursor = connection.cursor()
    sql = f"DELETE FROM users WHERE name = :who"
    cursor.execute(sql, {"who": name})
    connection.commit()
    connection.close()


def main():
    name = 'tom'
    age = '20'
    #
    # register_user(name, age)

    # users = find_all_users()
    #
    # print(users)
    #
    # for user in users:
    #     print(f"Name: {user[0]}, Age: {user[1]}")

    delete_user(name)



def register_user(name, age):
    connection = sqlite3.connect('camp.db')
    cursor = connection.cursor()
    sql = f"INSERT INTO users (name, age) VALUES(?, ?)"
    cursor.execute(sql, (name, age))
    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()
