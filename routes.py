from flask import render_template
from utils import read_word_as_html
from config import TIMELINE_ITEMS, SLIDESHOW_DATA

def setup_routes(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/about')
    def about():
        word_file = "static/about/about.docx"
        about_html = read_word_as_html(word_file)
        
        return render_template(
            'about.html',
            about_html=about_html,
            timeline_items=TIMELINE_ITEMS,
            slideshow_data=SLIDESHOW_DATA
        )

    @app.route('/products')
    def products():
        return render_template('products.html')

    @app.route('/rent')
    def rent():
        return render_template('rent.html')

    @app.route('/solutions')
    def solutions():
        return render_template('solutions.html')

    @app.route('/contact')
    def contact():
        return render_template('contact.html')

    @app.route('/news')
    def news():
        return render_template('news.html')