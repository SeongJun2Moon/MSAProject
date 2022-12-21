import string
import random
from sqlalchemy import create_engine
import pymysql
import pandas as pd


class UserService:
    def __init__(self):
        self.df = None

    def get_df(self):
        # 아이디, 비밀번호 리스트 생성
        _LENGTH = 10  # 10자리
        string_pool = string.ascii_letters  # 대소문자
        id_lst = list(i for i in range(100))
        nickname_lst = list()
        email_lst = list()
        pw_lst = list(1 for i in range(100))
        for i in range(100):
            result = ""  # 결과 값
            for j in range(_LENGTH):
                result += random.choice(string_pool)  # 랜덤한 문자열 하나 선택
            nickname_lst.append(result)
            email_lst.append(f"{result}@gmail.com")
        df = pd.DataFrame(zip(id_lst,email_lst,nickname_lst,pw_lst), index=[i for i in range(len(nickname_lst))]
                          ,columns=["blog_id", "email", "nickname", "password"])
        self.df = df
        print(df)

        # 데이터베이스 연결
        db_connection_str = 'mysql+pymysql://root:root@localhost:3306/mydb'
        db_connection = create_engine(db_connection_str)
        conn = db_connection.connect()

        # mysql에 저장
        self.df.to_sql(name='blog_busers', con=conn, if_exists='replace', index=False)


if __name__ == '__main__':
    UserService().get_df()