from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route('/band')
def band():
    band_info = [
        {
            "band_img": "img/top/smachimg.jpg",
            "band_name": "Smach gank",
            "button": "BAND",
            "buttonlink": "https://~~",
            "genre": "4piac / Pank",
            "location": "Tokyo"
            "location_link": "https://~~",
            "introduction": "私たちは〇〇でXXXXなバンドです。私たちは〇〇でXXXXなバンドです。私たちは〇〇でXXXXなバンドです。よろしくお願いします"
        }
    ]
    return render_template('band.html',band_info=band_info)

@app.route('/band')
def band():
    news_list = [
        {
            "link": "https://~~",
            "date" : "2023-08-01",
            "title": "ここにニュースが入ります1",
        },
        {
            "link": "https://~~",
            "date" : "2023-08-01",
            "title": "ここにニュースが入ります2",
        },
        {
            "link": "https://~~",
            "date" : "2023-08-11",
            "title": "ここにニュースが入ります3",
        },
    ]
    return render_template('band.html',news_list=news_list)


@app.route('/band')
def biografy():
    biografy = [
        {
            "contents": "こんなバンドこんなバンドでこんなバンドこんなバンドでこんなバンドこんなバンドでこんなバンドこんなバンドでこんなバンド",
        },
    ]
    return render_template('band.html',biografy=biografy)

@app.route('/band')
def member():
    member = [
        {
            "member_img" : ,
            "biogtopti": "DJ / MC",
            "biogtoptxt": "JMUS 本田",
        },
        {
            "member_img" : ,
            "biogtopti": "DJ / MC",
            "biogtoptxt": "JMUS 本田",
        },
         {
            "member_img" : ,
            "biogtopti": "DJ / MC",
            "biogtoptxt": "JMUS 本田",
        },
    ]
    return render_template('band.html',member=member)
