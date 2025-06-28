from decouple import config
import mysql.connector
from mysql.connector import Error

from create_bot import db_url


# после нужно сделать подтяжку из бд
async def cheak_lawyer(tg_id):
    try:
        # Подключение к MySQL (замените параметры на свои)
        connection = mysql.connector.connect(
            host="localhost",      # или IP-адрес сервера
            database="lawyer",
            user="root",
            password=""
        )

        cursor = connection.cursor(dictionary=True)  # Для возврата данных в виде словаря

        # SQL-запрос с защитой от инъекций
        query = "SELECT role FROM lawyer WHERE tg_id = %s"
        cursor.execute(query, (tg_id,))
        
        result = cursor.fetchone()  # Получаем одну запись

        # Закрываем соединение
        cursor.close()
        connection.close()

        # Проверяем, есть ли результат и role == 1
        if result and result['role'] == 1:
            return True
        return False

    except Error as e:
        print(f"Ошибка MySQL: {e}")
        return False



