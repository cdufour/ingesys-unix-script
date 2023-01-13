from flask import Flask, render_template, request
import hashlib
import os
import mysql.connector as database

app = Flask(__name__)

SAVE_DB = os.environ.get('SAVE_DB')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_NAME = os.environ.get('DB_NAME')

print("ENV VAR SAVE_DB: ", SAVE_DB)
print("ENV VAR DB_HOST: ", DB_HOST)
print("ENV VAR DB_PORT: ", DB_PORT)
print("ENV VAR DB_USER: ", DB_USER)
print("ENV VAR DB_PASS: ", DB_PASS)
print("ENV VAR DB_NAME: ", DB_NAME)

if not DB_HOST:
    DB_HOST = 'localhost'

if not DB_PORT:
    DB_PORT = 3306

if SAVE_DB == "True":
    connection = database.connect(
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME)

    cursor = connection.cursor()

def save_data(clearTxt, hashTxt, hashFn):
    try:
        statement = "INSERT INTO hashes (clearTxt,hashTxt,hashFn) VALUES (%s, %s, %s)"
        data = (clearTxt, hashTxt, hashFn)
        cursor.execute(statement, data)
        connection.commit()
        print("Successfully added entry to database")
    except database.Error as e:
        print(f"Error adding entry to database: {e}")


# @app.route('/')
# def hello():
#     return 'Hello, World!'

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        clearTxt = request.form['clearTxt']
        hashFn = request.form['hashFn']
        # b = bytes(clearTxt, 'utf-8')
        if hashFn == 'md5':
            hashTxt = hashlib.md5(clearTxt.encode(encoding = 'UTF-8')).hexdigest()
        elif hashFn == 'sha256':
            hashTxt = hashlib.sha256(clearTxt.encode(encoding = 'UTF-8')).hexdigest()
        else:
            return ':-(((('

        if SAVE_DB == "True":
            save_data(clearTxt, hashTxt, hashFn)

        return hashTxt
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)