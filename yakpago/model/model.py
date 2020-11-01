#입력값을 모델에 넘기기 전 예외처리 후 딕셔너리 형태로 입력값 변환 후 리턴.
def printInputValue(form):
    select_query = "SELECT * FROM medicineinfo"
    form_dict = form.to_dict()

    if (form_dict['category']!="category_all"):
        select_query += " WHERE category='"+form_dict['category']+"'"
        if (form_dict['subcategory']!="subcategory_all"):
            select_query += " and sub_category='"+form_dict['subcategory']+"'"
    
    form_dict['age'] = int(form_dict['age'])
    form_dict['weight'] = int(form_dict['weight'])

    if ('pregnant' in form_dict)==False:
        form_dict['pregnant'] = False

    return form_dict