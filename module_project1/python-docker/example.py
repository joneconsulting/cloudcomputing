import pymysql

conn = pymysql.connect(host='172.17.0.2', user='root', password='', port=3306, db='mydb', charset='utf8')
print('Connection info: ', conn)
cursor = conn.cursor()

def main():
    _id = input('아이디를 입력하세요. -> ')
    _pwd = input('비밀번호를 입력하세요. -> ')
    _name = input('이름을 입력하세요. -> ')
    print("안녕하세요, {0}님 회원가입을 축합니다.".format(_name))

    sql = "INSERT INTO member VALUES(%s, %s, %s);"
    cursor.execute(sql, (_id, _pwd, _name))
    conn.commit()

    sql = "SELECT * FROM member"
    cursor.execute(sql)
    list = cursor.fetchall()
    for row in list:
        print(row)
    
    cursor.close()
    conn.close()
main()


