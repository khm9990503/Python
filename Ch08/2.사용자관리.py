"""
날짜 : 2023/01/13
이름 : 구홍모
내용 : 파이썬 사용자관리 실습하기

"""

import pymysql

# DB 접속
conn = pymysql.connect(host='127.0.0.1',
                        user='root',
                        password='1234',
                        db='java1db',
                        charset='utf8')
cur = conn.cursor()
while True:
    print('0 : 종료, 1 : 등록, 2 : 조회, 3 : 수정, 4 : 삭제')
    answer = 0
    try:
        answer = int(input('선택 : '))
    except Exception  as e:
        print('다시 입력하세요. ',e)
        continue
    if answer == 0:
        break
    elif answer == 1:
        # dateset = list(input(아이디, 비번, 이름, 휴대폰, 나이, 순으로 입력 : ).split)
        print('등록할 데이터를 입력해주세요.')
        u = input('아이디 : ')
        p = input('비밀번호 : ')
        n = input('이름 : ')
        h = input('휴대폰 : ')
        a = input('나이 : ')
        # SQL 실행
        sql = "insert into `user1` values ('"+u+"','"+p+"','"+n+"','"+h+"','"+a+"');"
        cur.execute(sql)
        conn.commit()
        print('등록 완료...')
        continue
    elif answer == 2:
        print('1: uid 검색 조회, 2: 전체 조회')
        req = int(input('선택 : '))
        if req == 1:
            uid = input('uid : ')
            sql = "select * from `user1` where `uid`='"+uid+"';"
        else:
            # SQL 실행
            sql = "select * from `user1`;"
        cur.execute(sql)
        conn.commit()
        for row in cur.fetchall():
            print('--------------')
            print('아이디 : ',row[0])
            print('비밀번호 : ',row[1])
            print('이름 : ',row[2])
            print('휴대폰 : ',row[3])
            print('나이 : ',row[4])
        continue
    elif answer == 3:
        print('수정할 아이디를 입력해주세요.')
        u = input('아이디 : ')
        p = input('비밀번호 : ')
        n = input('이름 : ')
        h = input('휴대폰 : ')
        a = input('나이 : ')
        # SQL 실행
        sql = "update `user1` set "
        sql += "`name`='"+n+"', "
        sql += "`pass`='"+p+"', "
        sql += "`hp`='"+h+"', "
        sql += "`age`='"+a+"' "
        sql += "where `uid`='"+u+"';"
        cur.execute(sql)
        conn.commit()
        print('수정 완료..')
    elif answer == 4:
        print('삭제할 아이디을 입력해주세요.')
        u = input('아이디 : ')
        # SQL
        sql = "delete from `user1` where `uid`='"+u+"';"
        cur.execute(sql)
        conn.commit()
        print('삭제 완료..')
    else:
        print('0~4 중에서 입력하세요.')
        
# DB 종료
conn.close()
print('프로그램 종료')