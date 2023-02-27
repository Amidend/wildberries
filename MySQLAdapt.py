import mysql.connector
from mysql.connector import Error

class SQL:

    @staticmethod
    def create_connection(host_name, user_name, user_password):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password
            )
            print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")
    
    @staticmethod
    def ZAPROSTEST():
        connection = mysql.connector.connect(host='localhost',user='root',passwd='123456789',database='wb')
        # Создание объекта курсора для выполнения запросов
        mycursor = connection.cursor()
        
        # Выполнение запроса на извлечение всех полей из таблицы client
        mycursor.execute("SELECT * FROM client")
        
        # Получение результата запроса
        myresult = mycursor.fetchall()
        
        # Вывод результатов на консоль
        for row in myresult:
          print(row[1])
    
    @staticmethod
    def GetUser():
        connection = mysql.connector.connect(host='localhost',user='root',passwd='123456789',database='wb')
        mycursor = connection.cursor()
        mycursor.execute("SELECT client_fullname FROM client")
        res=mycursor.fetchall()
        return res

    @staticmethod
    def GetTovar():
        connection = mysql.connector.connect(host='localhost',user='root',passwd='123456789',database='wb')
        mycursor = connection.cursor()
        mycursor.execute("SELECT product_name FROM product")
        res=mycursor.fetchall()
        return res
    @staticmethod
    def GetALLTovar():
        connection = mysql.connector.connect(host='localhost',user='root',passwd='123456789',database='wb')
        mycursor = connection.cursor()
        mycursor.execute("SELECT * FROM product")
        res=mycursor.fetchall()
        return res
    @staticmethod
    def AddClient( fullname, date, status):
        # Получаем максимальный идентификатор клиента
        connection = mysql.connector.connect(host='localhost',user='root',passwd='123456789',database='wb')
        max_id = SQL.GetMaxClientId()

        # Создаем новую запись клиента с новым идентификатором
        client_id = max_id + 1
        cursor = connection.cursor()
        # Выполняем запрос на добавление нового клиента
        cursor.execute("INSERT INTO client (client_id, client_fullname, client_date, client_status) VALUES (%s, %s, %s, %s)", (max_id + 1, fullname, date, status))

        # Сохраняем изменения в базе данных
        connection.commit()

        # Закрываем курсор и соединение
        cursor.close()
        connection.close()
    
    @staticmethod
    def AddProduct(name,price, number, description):
        # Устанавливаем соединение с базой данных
        conn = mysql.connector.connect(host='localhost',user='root',passwd='123456789',database='wb')
        # Создаем курсор для выполнения запросов
        cursor = conn.cursor()

        # Получаем максимальный идентификатор продукта из таблицы
        max_id = SQL.GetMaxProductId()

        # Выполняем запрос на добавление нового продукта
        cursor.execute("INSERT INTO product (product_id, product_name,product_price, product_number, product_discription) VALUES (%s,%s, %s, %s, %s)", (max_id + 1, name,price, number, description))

        # Сохраняем изменения в базе данных
        conn.commit()

        # Закрываем курсор и соединение
        cursor.close()
        conn.close()    

    @staticmethod
    def GetMaxProductId():
        # Устанавливаем соединение с базой данных
        conn = mysql.connector.connect(host='localhost',user='root',passwd='123456789',database='wb')
        # Создаем курсор для выполнения запросов
        cursor = conn.cursor()

        # Выполняем запрос на получение максимального идентификатора продукта
        cursor.execute("SELECT MAX(product_id) FROM product")

        # Получаем результат запроса
        result = cursor.fetchone()

        # Закрываем курсор и соединение
        cursor.close()
        conn.close()

        # Возвращаем максимальный идентификатор или 0, если таблица пуста
        return result[0] if result[0] is not None else 0

    @staticmethod
    def delete_good(id):
        conn = mysql.connector.connect(host='localhost',user='root',passwd='123456789',database='wb')
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM product WHERE product_id='{id}'")
        conn.commit()
    @staticmethod
    def get_zakaz_data():
        # Подключение к базе данных MySQL
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='123456789',
            database='wb'
        )
        cursor = conn.cursor()

        # Получение данных из таблицы zakaz
        cursor.execute("SELECT order_date, SUM(order_numberOfGoods) FROM zakaz GROUP BY order_date")
        data = cursor.fetchall()

        # Закрытие соединения с базой данных
        cursor.close()
        conn.close()
        
        return data
    @staticmethod
    def GetMaxClientId():
        # Устанавливаем соединение с базой данных
        conn = mysql.connector.connect(host='localhost',user='root',passwd='123456789',database='wb')

        # Создаем курсор для выполнения запросов
        cursor = conn.cursor()

        # Выполняем запрос на получение максимального идентификатора клиента
        cursor.execute("SELECT MAX(client_id) FROM client")

        # Получаем результат выполнения запроса
        result = cursor.fetchone()

        # Закрываем курсор и соединение
        cursor.close()
        conn.close()

        # Возвращаем максимальный идентификатор клиента
        return result[0] if result[0] is not None else 0




if __name__ == "__main__":
    SQL.ZAPROSTEST()
