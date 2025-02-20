from flask import render_template

def setup_routes(app):
    @app.route('/about')
    def about():
        # 關於我們的HTML內容
        about_html = """
        <h1>關於勤工</h1>
        <p>勤工成立於1996年，從事叉車零件、耗材及其配件等產品的銷售，
        秉持著「用腦運搬」的精神，提供客戶最佳的搬運解決方案。</p>
        """

        # 時間軸資料結構
        timeline_items = [
            {
                'year': '1996',
                'top_image': 'static/about/history/axon_established.png',
                'top_alt': 'Axon Established',
                'bottom_text': '勤工成立'
            },
            {
                'year': '1999',
                'top_text': '成為加拿大貨叉品牌 Kenhar 台灣總代理',
                'bottom_image': 'static/about/history/kenhar.png',
                'bottom_alt': 'Kenhar'
            },
            {
                'year': '2000',
                'bottom_text': '成為全球前三大特殊配備品牌 Cascade 台灣總經銷'
            },
            {
                'year': '2002',
                'top_text': '引進德國 Hoesch 型鋼用於棧槓製造',
                'bottom_image': 'static/about/history/hoesch.png',
                'bottom_alt': 'Hoesch'
            },
            {
                'year': '2013',
                'top_image': 'static/about/history/bendi.png',
                'top_alt': 'Bendi',
                'bottom_text': 'OEM 英國品牌 Bendi 窄通道式堆高機之棧槓'
            },
            {
                'year': '2014',
                'bottom_text': '開發出四節式特殊型棧槓'
            },
            {
                'year': '2017',
                'top_image': 'static/about/history/liugong.png',
                'top_alt': 'LiuGong',
                'bottom_text': '柳工堆高機台灣總代理'
            },
            {
                'year': '2017',
                'top_image': 'static/about/history/axon.png',
                'top_alt': 'AXON',
                'bottom_text': '成立 AXON 品牌'
            }
        ]

        # 輪播圖資料
        slideshow_data = {
            'images': [
                {
                    'src': 'static/loop/loop1.jpg',
                    'alt': '輪播圖1'
                },
                {
                    'src': 'static/loop/loop2.jpg',
                    'alt': '輪播圖2'
                },
                {
                    'src': 'static/loop/loop3.jpg',
                    'alt': '輪播圖3'
                }
            ],
            'slogans': ['用腦運搬的專家', '專業搬運設備', '客製化解決方案'],
            'contents': ['提供最佳搬運方案', '多樣化產品選擇', '滿足您的特殊需求']
        }

        return render_template(
            'about.html',
            about_html=about_html,
            timeline_items=timeline_items,
            slideshow_data=slideshow_data
        )