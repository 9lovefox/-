from pymongo import MongoClient

client= MongoClient('localhost', 27017)
db = client.dbsparta
# 데이터베이스 하나를 생성하는데 그 이름이 dbsparta

# 데이터 넣기(insert) #내컴퓨터는 명령프롬프트 닫으면 몽고 DB 실행 안됨
# db.users.insert_one(
#     {
#         "name":"Bob",
#         "age":"20"

#     }
# )
# #데이터 조회
db.users.delete_many({})
#create retreive update Delete CRUD 
