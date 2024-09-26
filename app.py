from flask import Flask
from config import Config
from scripts.create_tables import create_tables
from scripts.fetch_denormalized_data import fetch_denormalized_data
from scripts.insert_data import insert_normalized_data

app = Flask(__name__)
app.config.from_object(Config)


data = fetch_denormalized_data()
create_tables()
insert_normalized_data(data)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
