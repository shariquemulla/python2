import mysql.connector

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

word = input('Enter a word : ').lower()

cursor = con.cursor()

query = cursor.execute("SELECT * FROM Dictionary where expression = '{}'".format(word))
results = cursor.fetchall()

if results:
    for value in results:
        print(value[1])
else:
    print("Word not found! Please double check.")