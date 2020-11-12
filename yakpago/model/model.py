from db_model import postgresql

#입력값을 모델에 넘기기 전 예외처리 후 딕셔너리 형태로 입력값 변환 후 리턴.
def printInputValue(form):
    select_query = "SELECT * FROM medicineinfo"
    form_dict = form.to_dict()
    ingredient_list = []

    if (form_dict['category']!="category_all"):
        select_query += " WHERE category='"+form_dict['category']+"'"
        if (form_dict['subcategory']!="subcategory_all"):
            select_query += " and sub_category='"+form_dict['subcategory']+"'"
    
    form_dict['weight'] = int(form_dict['weight'])

    if ('pregnant' in form_dict)==False:
        form_dict['pregnant'] = False

    form_dict['ingredients'] = list(form_dict['ingredients'].split(','))
    for medicine in form_dict['ingredients']:
        ingredient_list = postgresql.select_ingredients(medicine, ingredient_list)
    form_dict['ingredients'] = list(set(ingredient_list))

    return [200301554, 200600089, 201100204, 201801991, 201905618, 202005904, 201004450, 200608043, 201706903, 200500986]