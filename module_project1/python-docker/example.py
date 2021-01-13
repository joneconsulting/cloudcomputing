import pymysql

conn = pymysql.connect(host='172.17.0.2', user='root', password='', port=3306, db='mydb', charset='utf8')
print('Connection info: ', conn)
cursor = conn.cursor()

def main():
    _name = input('이름을 입력하세요. -> ')
    print("안녕하세요, {0}님".format(_name))
main()


