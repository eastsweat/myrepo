import pymysql
conn = 0
curs = 0
menu_list=[]
total_list=[]

# print(pymysql)
def db_connect():
    global conn, curs
    try:
        conn = pymysql.connect(host='34.146.115.147', user='SBA_07', password='123qwe', db='SBA_07',port=3306)
        print(conn)
    except:
        print('DB연동 실패')
        return False
    curs = conn.cursor(pymysql.cursors.DictCursor)
    return True
def db_close():
    curs.close();
    conn.close();

def show_menu(): #문제없
    sql=f'select Menu.id, Menu.food_name from Menu'
    curs.execute(sql)
    rows = curs.fetchall()
    for row in rows:
        print(row['id'], row['food_name'])

def get_ingred_total_list():

    for i in range(1,4):
        print(i, "번째 선택 : 다음의 목록 중 메뉴를 선택하여 주세요")
        show_menu()
        id=int(input('번호>'))
        food_name=input('메뉴이름>')

        if check_menu(id, food_name)==False:
            return None
            continue

        else:
            print(i,"번째 메뉴 선택이 완료되었습니다")
            menu_list.append(food_name)
            sql = f'select * from Prod where Prod.id={id}'
            curs.execute(sql)
            rows = curs.fetchall()
            for row in rows:
                print(row['ingred'])
            print(menu_list)
            total_list.append(row['ingred'])
    print(set(total_list))


def check_menu(id, food_name):
    sql = f'select food_name from Menu where id = {id}'
    curs.execute(sql)
    row = curs.fetchone()
    if row['food_name']==food_name:
        return True
    else:
        return False

if __name__ == '__main__':
    if db_connect() == False:
        exit(1)
    db_close()