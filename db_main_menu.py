import db_function_menu as df
print('-- 장보기리스트 생성 시스템 --')
if df.db_connect() == False:
    exit(1)
while(True):
    try:
        print('1. 메뉴 조회\n2. 메뉴 선택 및 장보기 리스트 생성\n3. 프로그램 종료')
        try:
            action = int(input('실행할 메뉴 번호 입력>'))
        except ValueError:
            print('숫자 1~3를 입력하십시오')
            continue
        if action >= 1 and action <= 3:
            pass
        else:
            print('1 ~ 3 사이의 번호를 입력해주세요')

        if action == 1:
            print('메뉴 조회 화면')
            print(f'{"번호":^10} {"메뉴":^10}')
            df.show_menu()

        elif action == 2: #메뉴 선택 및 리스트 생성
            print(" 메뉴 선택 화면")
            df.get_ingred_total_list()



        elif action == 3:
            print('프로그램 종료')
            df.db_close()
            break
    except KeyboardInterrupt:
        print("Program을 종료합니다.")
        df.db_close()
        break