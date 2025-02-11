# import petl as etl
import csv
import pandas as pd
import sqlalchemy as db


def safe_open():
    tmp_file = open("tmp", "w")
    with open("data.csv", "r", newline="") as csvfile:
        for row in csvfile:
            row = row[1:-1]
            # row = row.replace()  If data correction needed
            tmp_file.write(row + "\n")
        tmp_file.close()
    df_new = pd.read_csv("tmp")
    return df_new


# csv_file = pd.read_csv("data.csv")


def injection(csv_file):
    connection = db.create_engine("postgresql://myuser:mypassword@localhost:5432/mydb")
    csv_file.to_sql(
        "HRDB",
        connection,
        index=False,
        if_exists="replace",
        dtype={
            "Name": db.VARCHAR(255),
            "City": db.VARCHAR(255),
            "Age": db.Integer(),
        },
    )


injection(safe_open)
