from flask import Flask, jsonify
from db_model import postgresql

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>This is Yakpago project!</h1>"

#단순히 psycopq2를 활용하여 DB 연동이 잘 됐는지 확인하기 위한 테스트코드. 
@app.route('/postgresql_test')
def postgresql_page():
    data = postgresql.postgresql_test()
    return jsonify(data)    #쿼리문으로 반환된 데이터를 json 포맷으로 해당 라우팅 경로에 출력

if __name__ == "__main__":
    app.run(debug=True);