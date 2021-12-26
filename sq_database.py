import sqlite3


class SQ:

    def __init__(self, database_file):
        # Подкючаемся к БД и сохраняем курсор соединения:
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def get_subs(self, status=True):
        # Получаем активных подписчиков:
        with self.connection:
            return self.cursor.execute("SELECT * FROM `subs` WHERE `status` = ?", (status,)).fetchall()

    def subs_exist(self, user_id):
        # Проверям есть ли пользователь в базе:
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `subs` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))

    def add_subs(self, user_id, status=True):
        # Добавляем новых подписчиков:
        with self.connection:
            return self.cursor.execute("INSERT INTO `subs` (`user_id`, `status`) VALUES (?, ?)", (user_id, status))

    def update_subs(self, user_id, status):
        # Обновляем статус подписки:
        return self.cursor.execute("UPDATE `subs` SET `status` = ? WHERE `user_id` = ?", (status, user_id))

    def close(self):
        self.connection.close()
