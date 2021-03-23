from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route("/query")
def query():

    args = request.args

    if 'keyword' in args:
        print(args['keyword'])
        keyword = args['keyword']

        result = ['吳書十三', '吳書十', '吳書三']        
        # 找到包含關鍵字的書籍名稱
        # 放進去 list
        # 回傳回來

    return jsonify(result), 200


@app.route("/load")
def load():

    args = request.args

    if 'bookname' in args:
        print(args['bookname'])

        # 找到對應的白話文書籍名稱
        # 回傳回來
        bookname = args['bookname']
        mapping_file_name = find_mapping_file(bookname)


    return mapping_file_name, 200



def find_mapping_file(bookname):
  """
  Args:
    bookname (str): 
  
  Returns:
    mapping_file_name (str):
  """
  mapping_df = pd.read_csv('三國志對照表.csv', encoding='utf-8')  
  mapping_file_name_list = mapping_df[mapping_df["傳記 + 書籍對應"] == bookname]['白話文章節名稱'].values  
  if len(mapping_file_name_list) > 0:
      return mapping_file_name_list[0]
  else:
      return 'no result'

app.config['JSON_AS_ASCII'] = False
app.run(debug=True)
