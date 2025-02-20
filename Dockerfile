# 使用 Python 3.11 作為基礎映像
FROM python:3.11

# 設定工作目錄
WORKDIR /app

# 複製應用程式程式碼
COPY app.py .
COPY requirements.txt .

# 安裝依賴套件
RUN pip install --no-cache-dir -r requirements.txt || true

# 讓 Flask 在 Docker 內部監聽所有 IP
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# 容器啟動時執行 Flask 應用
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000", "--reload"]