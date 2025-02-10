import petl as etl
import csv
import pandas as pd
import sqlalchemy as db

def safe_open():
    tmp_file = open('tmp', 'w')
    with open("Bакансии2022.csv", 'r', newline='') as csvfile:
        for row in csvfile:
            row = row[1:-1]
            # row = row.replace()
            tmp_file.write(row + '\n')
        tmp_file.close()
    df_new = pd.read_csv('tmp')



def injection(csv_file):
    connection = db.create_engine('postgresql://myuser:mypassword@localhost:5432/mydb')

    csv_file.to_sql('HRDB', connection, index=False, if_exists='replace', dtype={
        "ПоисковыйКлюч": db.VARCHAR(50),
        "ВалютаНаименование": db.VARCHAR(255),
        "ВакансияКлюч": db.Integer(),
        'published_at': db.Date(),
        'created_at': db.Date(),
        '__KEY_items': db.VARCHAR(255),
        'ВакансияТребования': db.Text(),
    })


'''
    connection = db.create_engine('postgresql://demo: demo@localhost:5432/demo')
    csv_file.to_sql('HRDB', connection, index=False, if_exists='replace', dtype={
        "ПоисковыйКлюч": db.VARCHAR(50),
        "ВалютаНаименование": db.VARCHAR(255),
        "ВакансияКлюч": db.Integer(),
        'published_at': db.Date(),
        'created_at': db.Date(),
        '__KEY_items': db.VARCHAR(255),
        'ВакансияТребования': db.Text(),
    })'''
