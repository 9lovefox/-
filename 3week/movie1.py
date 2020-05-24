from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta
metrics_movie = list(db.movies.find({'title': '매트릭스'}))
metrics_star = metrics_movie[0]["star"]
print(metrics_star)

same_movies = list(db.movies.find({'star': metrics_star}))
for movie in same_movies:
    movie_title = movie["title"]
    print(movie_title)

db.movies.update_many(
    {'star': metrics_star},
    {'$set': {'star': 0}}
)