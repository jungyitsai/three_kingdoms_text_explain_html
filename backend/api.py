from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/query")
def query():

    args = request.args

    if 'keyword' in args:
        print(args['keyword'])

        # 找到包含關鍵字的書籍名稱
        # 放進去 list
        # 回傳回來

    return "No result", 200


@app.route("/load")
def load():

    args = request.args

    if 'bookname' in args:
        print(args['bookname'])

        # 找到對應的白話文書籍名稱
        # 回傳回來

    return "No result", 200


app.run(debug=True)
