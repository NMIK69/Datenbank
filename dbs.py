from mysql.connector import connect, Error

create_stock_table = """
CREATE TABLE stocks(    
    year INT NOT NULL,
    month INT NOT NULL,
    company varchar(100) NOT NULL,
    open DOUBLE,
    high DOUBLE,
    low DOUBLE,
    close DOUBLE,
    volume INT
);"""




def database_interact(request): 

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
                
            connection.close()

    except Error as e:
        print(e)
