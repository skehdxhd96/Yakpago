#psycopq2 라이브러리를 활용하여 DB 연동하기
import psycopg2

#연동하기 위한 DB 정보 입력
conn = psycopg2.connect(
    host='yakpago-db-instance.ce3s5gihh4zd.ap-northeast-2.rds.amazonaws.com', 
    dbname='medicine', 
    user='yakpago', 
    password='yakpago723', 
    port='5432')

curl = conn.cursor()

def postgresql_test():
    curl.execute("SELECT * FROM medicineinfo WHERE item_seq=201907113;")    #쿼리문 작성
    return curl.fetchall()  #fetchall()은 해당 쿼리문에 대한 모든 내용을 반환, fetchone()은 해당 쿼리문에 대한 맨 첫번째 데이터만 반환.

#일반의약품 카테고리 항목을 select 해오는 함수 - 카테고리 대분류를 html파일에 표현하기 위해
def select_category():
    curl.execute("select distinct(category) from medicineinfo where etc_otc_code='일반의약품';") 
    results = curl.fetchall()
    categories = [result[0] for result in results[1:]]
    return sorted(categories)

def select_subcategory(sub_category="all"):
    if sub_category=="all":
        curl.execute("select distinct(sub_category) from medicineinfo where etc_otc_code='일반의약품';") 
    else:
        curl.execute("select distinct(sub_category) from medicineinfo where category='"+sub_category+"' and etc_otc_code='일반의약품';") 
    results = curl.fetchall()
    subcategories = [result[0] for result in results if result[0] is not None]
    return sorted(subcategories)

#입력 페이지에서 약품 성분 데이터를 가져오기 위해 약품명을 검색하고, 검색한 약품명과 일치하거나 포함되어 있는 약품을 select 하는 함수
def select_medicinename(input_name):
    query = "select item_name from medicineinfo where item_name like '%" + input_name + "%';"
    curl.execute(query)
    results = curl.fetchall()

    results = [result[0] for result in results if result[0] is not None]
    return results

def select_ingredients(item_name, ingredient_list):
    query = "select ingredient from main_ingredient where item_seq = (select item_seq from medicineinfo where item_name = '" + item_name + "')"
    curl.execute(query)
    results = curl.fetchall()
    for result in results:
        ingredient_list.append(result[0])
    
    return ingredient_list

def select_item_names(item_seqs):
    results = {}
    for item_seq in item_seqs:
        query = "select item_name from medicineinfo where item_seq = " + str(item_seq)
        curl.execute(query)
        results[item_seq] = curl.fetchone()[0]
    return results