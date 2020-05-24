import requests

#ajax
#url, header, body
#Get: url, header
#post: url, header, 데이터 body

# headers = {
#     "Content-Type": application/json"
# }
# data = {


# }
# request. get('url'), headers={})
# request. post('url', headeers={}, data={})
r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()    #json 데이터를 자동으로 Python Dictionary로 변환

realtime_city_air = rjson["RealtimeCityAir"]
rows = realtime_city_air["row"] #리스트

for row in rows:
    gu_name = row["MSRSTE_NM"]
    mise_value = row["IDEX_MVL"]

    if mise_value < 100:
        print(gu_name, mise_value)
        


