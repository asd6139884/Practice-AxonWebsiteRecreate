from docx import Document

def read_word_as_html(file_path):
    """ 讀取 Word 檔案，轉換為 HTML 格式 """
    doc = Document(file_path)
    html_content = ""

    for para in doc.paragraphs:
        paragraph_text = ""
        for run in para.runs:
            text = run.text
            if run.bold:
                text = f"<b>{text}</b>"
            if run.italic:
                text = f"<i>{text}</i>"
            if run.font.size:
                font_size = int(run.font.size.pt)
                text = f'<span style="font-size:{font_size}px;">{text}</span>'
            if run.font.color and run.font.color.rgb:
                color = run.font.color.rgb
                text = f'<span style="color:#{color};">{text}</span>'
            
            paragraph_text += text
        
        html_content += f"<p>{paragraph_text}</p>"
    return html_content
