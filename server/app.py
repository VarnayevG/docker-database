from flask import Flask
from flask import jsonify, render_template
from sqlalchemy import create_engine
import pandas as pd
import json

app = Flask(__name__)


@app.route('/')
def get_data():
    engine = create_engine("postgresql://postgres@db:5432/postgres")
    data = pd.read_sql_query("select * from sample", con=engine)
    json_data = json.loads(data.to_json(index=False, orient='split'))
    return json_data


@app.route('/health')
def get_health():
    return jsonify(success=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0')