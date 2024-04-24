
#импорт библиотек
import psycopg2
import csv
import os

#задаем переменные со списками имен таблиц БД и файлов данных
sql_bd_names = ['employees', 'customers', 'orders']
data_file_names = ['employees_data.csv', 'customers_data.csv', 'orders_data.csv']

#задаём параметры для подключения к БД postgres
conn_params = {
  "host": "localhost",
  "database": "north",
  "user": "postgres",
  "password": "post13"
}

def add_sql_bd(file, bd):
    """Скрипт для заполнения данными таблиц в БД Postgres."""
    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            for i in range(len(file)):
                with open(os.path.join('north_data', file[i]), 'r') as file_csv:
                    heders = next(file_csv)
                    filecsv = csv.reader(file_csv)
                    print(heders)
                    for rot in filecsv:
                        values = '%s, ' * len(rot)
                        cur.execute(f"INSERT INTO {bd[i]} VALUES ({values[:-2]})", rot)
                    conn.commit()
    conn.close()


if __name__ == '__main__':
    add_sql_bd(data_file_names, sql_bd_names)
    print()