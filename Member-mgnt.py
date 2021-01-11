import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='', port=13306, db='mydb', charset='utf8')
# cursor = conn.cursot() # Array based Cursor
cursor = conn.cursor(pymysql.cursors.DictCursor) # Dictionary based Cursor

def displayMember():
    # DB 조회
    rows = selectList()
    for row in rows:
        print("{0}\t{1}\t{2}\t{3}".format(row['id'], row['name'], row['pwd'], row['reg_date']))

def selectList():
    selectSql = '''SELECT id, name, pwd, reg_date FROM member'''
    cursor.execute(selectSql)

    return cursor.fetchall()

def deleteMember(userId:str):
    deleteSql = '''DELETE FROM member WHERE id=%s'''
    cursor.execute(deleteSql, (userId,))
    conn.commit()
    print('회원이 삭제 되었습니다.')

def main():
    print('#' * 50)
    print('# 회원 관리 프로그램 ver 0.1')
    print('#' * 50)

    while True:
        try:
            cmd = int(input('1) 회원목록 2) 회원검색 3) 회원추가 4) 회원삭제 5) 종료  (1~5) -> '))
        except ValueError:
            print('1~5 사이의 명령어를 선택해 주세요.')
            continue
        
        if cmd == 1:
            print("<회원 목록>")
            displayMember()        
        elif cmd == 2:
            print("회원 검색 입니다.")
        elif cmd == 3:
            print("회원 추가 입니다.")
        elif cmd == 4:
            print("<회원 삭제>")
            userId = input("삭제할 멤버의 아이디를 입력하세요 -> ")
            deleteMember(userId)
        elif cmd == 5:
            cursor.close()
            conn.close()
            quit()
        else:
            print("잘못 된 명령어 입니다. 다시 입력해 주세요.")
            continue

main()