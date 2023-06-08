from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route('/band')
def band():
    band_info = {
        "band_img":"img/top/smachimg.jpg",
        "band_name": "Smach gank",
        "button": "BAND",
        "buttonlink": "https://~~",
        "genre": "4piac / Pank",
        "location": "Tokyo",
        "location_link": "https://~~",
        "introduction": "私たちは〇〇でXXXXなバンドです。私たちは〇〇でXXXXなバンドです。私たちは〇〇でXXXXなバンドです。よろしくお願いします"
    }

    news_list = [
        {
            "link": "https://~~",
            "date" : "2023-08-01",
            "title": "ここにニュースが入ります1",
            "icon": "img/common/icon_news01.svg",
        },
        {
            "link": "https://~~",
            "date" : "2023-08-01",
            "title": "ここにニュースが入ります2",
            "icon": "img/common/icon_news01.svg",
        },
        {
            "link": "https://~~",
            "date" : "2023-08-11",
            "title": "ここにニュースが入ります3",
            "icon": "img/common/icon_news01.svg",
        },
    ]

    biografy = {
        "contents": "こんなバンドこんなバンドでこんなバンドこんなバンドでこんなバンドこんなバンドでこんなバンドこんなバンドでこんなバンド",
        "member": [ 
            {
                "member_img" : "img/top/img_biogimg01.jpg",
                "biogtopti": "DJ / MC",
                "biogtoptxt": "JMUS 本田",
            },
            {
                "member_img" : "img/top/img_biogimg02.jpg",
                "biogtopti": "DJ / MC",
                "biogtoptxt": "JMUS 本田",
            },
            {
                "member_img" : "img/top/img_biogimg03.jpg",
                "biogtopti": "DJ / MC",
                "biogtoptxt": "JMUS 本田",
            },
            {
                "member_img" : "img/top/img_biogimg02.jpg",
                "biogtopti": "DJ / MC",
                "biogtoptxt": "JMUS 本田",
            },
            {
                "member_img" : "img/top/img_biogimg01.jpg",
                "biogtopti": "DJ / MC",
                "biogtoptxt": "JMUS 本田",
            },
        ] 
    }

    music_list = [
        {
            "img": "img/top/icon_works02.jpg",
            "title": "R.I.P",
            "bandname": "バンド1",
            "time": "4.57",
        },
        {
            "img": "img/top/icon_works02.jpg",
            "title": "R.I.P",
            "bandname": "バンド2",
            "time": "4.57",
        },
        {
            "img": "img/top/icon_works02.jpg",
            "title": "R.I.P",
            "bandname": "バンド3",
            "time": "4.57",
        },
        {
            "img": "img/top/icon_works02.jpg",
            "title": "R.I.P",
            "bandname": "バンド4",
            "time": "4.57",
        },
    ]

    movie_list = [
        {
            "videoimg": "img/top/img_movieimg01.jpg",
        },
        {
            "videoimg": "img/top/img_movieimg01.jpg",
        },
    ]

    photo_list = [
        {
            "img": "img/top/img_photo01.jpg",
        },
        {
            "img": "img/top/img_photo02.jpg",
        },
        {
            "img": "img/top/img_photo03.jpg",
        },
        {
            "img": "img/top/img_photo04.jpg",
        },
        {
            "img": "img/top/img_photo05.jpg",
        },
        {
            "img": "img/top/img_photo06.jpg",
        },
    ]

    return render_template('band.html',band_info=band_info, news_list=news_list, biografy=biografy, music_list=music_list, movie_list=movie_list, photo_list=photo_list)

