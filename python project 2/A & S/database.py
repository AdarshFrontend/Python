import sqlite3


# For creating the database and the table
def Database():
    connectn = sqlite3.connect("contactdata.db")
    cursor = connectn.cursor()
    cursor.execute("CREATE  contactinformation (id INTEGER  AUTOINCREMENT, first_name varchar(23), middle_name varchar(23), last_name varchar(23), gender varchar(23), age varchar(23), home_address varchar(23), phone_number varchar(23))")
    cursor.close()
    connectn.close()