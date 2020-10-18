#psycopq2 라이브러리를 활용하여 DB 연동하기
import psycopg2

#연동하기 위한 DB 정보 입력
conn = psycopg2.connect(
    host='yakpago-db-instance.ce3s5gihh4zd.ap-northeast-2.rds.amazonaws.com', 
    dbname='medicine', 
    user='yakpago', 
    password='yakpago723', 
    port='5432')

cur1 = conn.cursor()

def postgresql_test():
    cur1.execute("SELECT * FROM medicineinfo WHERE item_seq=201907113;")    #쿼리문 작성
    return cur1.fetchall()  #fetchall()은 해당 쿼리문에 대한 모든 내용을 반환, fetchone()은 해당 쿼리문에 대한 맨 첫번째 데이터만 반환.