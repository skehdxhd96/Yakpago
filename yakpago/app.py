from flask import Flask, jsonify, render_template, request
from flask_bootstrap import Bootstrap
from db_model import postgresql
from model import model

app = Flask(__name__)
Bootstrap(app)

#단순히 psycopq2를 활용하여 DB 연동이 잘 됐는지 확인하기 위한 테스트코드. 
@app.route('/postgresql_test')
def postgresql_page():
    data = postgresql.postgresql_test()
    return jsonify(data)    #쿼리문으로 반환된 데이터를 json 포맷으로 해당 라우팅 경로에 출력

#입력값 받아와 model.py(모델링 코드 넣을 곳)로 넘겨줌. 확인을 위해 model.py에 printInputValue 함수를 만들어 출력해줌.
@app.route('/', methods = ['GET', 'POST'])
def main_page():
    if request.method=="GET":
        categories = postgresql.select_category()

        return render_template('index.html', categories=categories)
    if request.method=="POST":
        input_form = request.form
        pregnant = input_form.get('pregnant')
        if pregnant:
            pregnant = True 
        else:
            pregnant = False
        result = model.printInputValue(input_form['age'], input_form['weight'], input_form['disease'], pregnant, input_form['category'])
        print(result)
        
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)