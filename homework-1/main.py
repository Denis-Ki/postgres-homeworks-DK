"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv
import os

sql_bd_names = ['employees', 'customers', 'orders']
data_file_names = ['employees', 'customers', 'orders']

