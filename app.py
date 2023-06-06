from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    news_list = [
        {
            "link": "https://~~",
            "date" : "2023-02-02",
            "title": "記事1",
            "img": "~~1.jpg",
        },
        {
            "link": "https://~~",
            "date" : "2023-02-02",
            "title": "記事2",
            "img": "~~2.jpg",
        },
        {
            "link": "https://~~",
            "date" : "2023-02-02",
            "title": "記事3",
            "img": "~~3.jpg",
        },
    ]
    return render_template('band2.html',news_list=news_list)
