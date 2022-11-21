from mysql.connector import connect, Error


def database_request(request): 

    try:
        with connect(
            host="localhost",
            user="root",
            password="-",
            database="-",
        ) as connection:
            with connection.cursor() as cursor:

                cursor.execute(request)
                connection.commit()
                data = cursor.fetchall()
                print(data)
                
            connection.close()

    except Error as e:
        print(e)

    return data