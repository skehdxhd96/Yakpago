from flask import Flask, jsonify, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from db_model import postgresql
from model import model

app = Flask(__name__)
Bootstrap(app)

#입력값 받아와 model.py(모델링 코드 넣을 곳)로 넘겨줌. 확인을 위해 model.py에 printInputValue 함수를 만들어 출력해줌.
@app.route('/', methods = ['GET', 'POST'])
def main_page():
    categories = postgresql.select_category()

    if request.method=="POST":
        input_form = request.form
        result = model.printInputValue(input_form)
        print(result)
        
    return render_template('main.html', categories=categories)

#입력값 Dynamic Select Box 구현을 위해 필요한 라우팅 경로.
@app.route('/subcategory/<category>')
def subcategory(category):
    subcategories = postgresql.select_subcategory(category)
    subcategoriesArray = []

    for id, subcategory in enumerate(subcategories):
        subcategoryObj = {}
        subcategoryObj['id'] = id+1
        subcategoryObj['subcategory'] = subcategory
        subcategoriesArray.append(subcategoryObj)

    return jsonify(subcategoriesArray)

if __name__ == "__main__":
    app.run(debug=True)