# 데이터프레임 mysql로 보내기
### 필요 라이브러리 설치
pip install pymysql
pip install sqlalchemy

### 오류
버전오류 : pip install --upgrade sqlalchemy
pymysql.err.OperationalError - 1054 : if_exists='replace' - 테이블이 비어있거나 키값이 다를 때
sqlalchemy.exc.IntegrityError - 1217 : if_exists='append' - 온전한 테이블에 내용을 추가할 때