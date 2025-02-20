from flask import Flask, render_template
from routes import setup_routes
from docx import Document

def read_word_as_html(file_path):
    """ 讀取 Word 檔案，轉換為 HTML 格式 """
    doc = Document(file_path)
    html_content = ""

    for para in doc.paragraphs:
        # 取得段落文字
        paragraph_text = ""

        # 逐一處理每個段落內的文字樣式
        for run in para.runs:
            text = run.text
            if run.bold:
                text = f"<b>{text}</b>"  # 加粗
            if run.italic:
                text = f"<i>{text}</i>"  # 斜體
            if run.font.size:
                font_size = int(run.font.size.pt)  # 取得字體大小（pt）
                text = f'<span style="font-size:{font_size}px;">{text}</span>'
            if run.font.color and run.font.color.rgb:
                color = run.font.color.rgb  # 取得顏色 (RGB)
                text = f'<span style="color:#{color};">{text}</span>'
            
            paragraph_text += text
        
        # 保留換行
        html_content += f"<p>{paragraph_text}</p>"
    return html_content


app = Flask(__name__)
setup_routes(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    word_file = "static/about/about.docx"  # 指定 Word 檔案
    about_html = read_word_as_html(word_file)  # 轉換為 HTML
    return render_template('about.html', about_html=about_html)

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

if __name__ == '__main__':
    app.run(debug=True)

