'main.py' записывает данные в xlsx, затем конвертирует в csv
'sql_inject.py' берёт данные из csv, может обработать, если нужно что-то поменять в форматировании данных, затем делает inject  в sql-таблицу
```sql
SELECT * FROM "HRDB" LIMIT 10;
   Name   | Age |  City
----------+-----+---------
 Oleg     |  27 | Omsk
 Gennadiy |  29 | Moscow
 Oleg     |  24 | Saratov
 Elena    |  24 | Moscow
 Ivan     |  30 | Omsk
 Oksana   |  25 | Omsk
 Gennadiy |  23 | Omsk
 Oleg     |  22 | Omsk
 Ivan     |  30 | Omsk
 Olga     |  20 | Saratov
(10 rows)
```
