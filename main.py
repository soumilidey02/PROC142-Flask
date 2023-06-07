from flask import Flask, jsonify, request
import csv
all_articles= []
with open('articles.csv',encoding="utf8")as f:
    reader= csv.reader(f)
    data=list(reader)
    all_articles= data[1:]

liked_articles=[]
not_liked_articles=[]

#initialising api
app=Flask(__name__)

#1st api to get articles
@app.route("/get-articles")
def get_articles():
    return jsonify({
        "data": all_articles[0],
        "Status": "Success"
    })

#2nd api
@app.route("/")
def show():
    return(
         "Hello"
    )

#api for like
@app.route("/liked-articles", methods=["POST"])
def liked_articles():
    articles= all_articles[0]
    all_articles=all_articles[1:]
    liked_articles.append(articles)
    return jsonify({
        "status": "success"
    }),201

#api for dislike
@app.route("/disliked-articles", methods=["POST"])
def disliked_articles():
    articlea= all_articles[0]
    all_articles= all_articles[1:]
    disliked_articles.append(articlea)
    return jsonify({
        "status": "success"
    }),201
    
#execute api
if __name__ == "__main__":
    app.run()