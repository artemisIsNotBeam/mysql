import mysql.connector

def main():
    print("checking if data base exists")

def makeConnection():
    myexample_db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="MTG=Awes0me",
        datatbase="niceDatabase"
    )
    mycursor = myexample_db.cursor()

    return [mycursor, myexample_db]

def check():
    try:
        myexample_db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="MTG=Awes0me",
        )
    except:
        print("error")

def createDB(mycursor):
    mycursor.execute("CREATE DATABASE niceDatabase")

def createTable(mycursor):
    mycursor.execute('''CREATE TABLE IF NOT EXISTS students(id INT AUT_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)''')

def addPeople(age, name, mycursor, db):
    sql = 'INSERT INTO students (name, age) VALUES (%s, %s)'
    value = (name,age)
    mycursor.execute(sql, value)

    db.commit()