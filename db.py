import sqlite3
import os

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("dnd_games_script.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS current_game 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         name TEXT NOT NULL, 
                         ImageData BLOB NOT NULL, 
                         next_id INTEGER)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS games 
                       (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       name TEXT NOT NULL, 
                       game_id INTEGER, 
                       count INTEGER NOT NULL,
                       FOREIGN KEY (game_id) REFERENCES current_game (id))''')

    def convert_to_binary_data(self, filename):
        # Преобразование данных в двоичный формат
        with open(filename, 'rb') as file:
            blob_data = file.read()
        return blob_data

    def insert_blob(self, name, photo):
        try:
            cursor = self.connection.cursor()
            sqlite_insert_blob_query = '''INSERT INTO current_game 
            (name, ImageData, next_id) VALUES(?,?,?)
            '''
            emp_photo = self.convert_to_binary_data(photo)
            # Преобразование данных в формат кортежа
            data_tuple = (name, emp_photo, 0)
            self.cursor.execute(sqlite_insert_blob_query, data_tuple)
            self.connection.commit()
            print("Изображение и файл успешно вставлены как BLOB в таблиу")
            self.cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if self.connection:
                self.connection.close()
                print("Соединение с SQLite закрыто")

    def write_to_file(self, data, filename):
        # Преобразование двоичных данных в нужный формат
        with open(filename, 'wb') as file:
            file.write(data)
        print("Данный из blob сохранены в: ", filename, "\n")

    def read_blob_data(self, emp_id):
        try:
            cursor = self.connection.cursor()
            print("Подключен к SQLite")

            sql_fetch_blob_query = """SELECT * from new_employee where id = ?"""
            cursor.execute(sql_fetch_blob_query, (emp_id,))
            record = cursor.fetchall()
            for row in record:
                print("Id = ", row[0], "Name = ", row[1])
                name = row[1]
                photo = row[2]

                photo_path = os.path.join("db_data", name + ".jpg")
                self.write_to_file(photo, photo_path)

            self.cursor.close()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)

    def update_next_id(self, prev_id, next_id):
        try:
            self.cursor = self.connection.cursor()
            command_update = '''UPDATE current_game SET next_id = ? WHERE id = ?'''
            data = (prev_id, next_id)
            self.cursor.execute(command_update, data)
            self.connection.commit()
            self.cursor.close()
        except:
            pass
