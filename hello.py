from flask import Flask
import mysql.connector
app = Flask(__name__)
@app.route("/")
def home():
    try:
        db = mysql.connector.connect(
            host="db",
            user="myuser",
            password="mypass",
            database="myapp"
        )
        return "Flask connected to MySQL!"
    except:
        return "Flask running but database not ready"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

