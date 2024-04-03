# 使用官方 Python 运行时作为父镜像
FROM python:3.10.9

# 设置工作目录为 /app
WORKDIR /app

# 将当前目录内容复制到位于 /app 中的容器中
COPY . /app

# 安装 requirements.txt 中指定的所有必需包
RUN pip install --no-cache-dir -r requirements.txt

# 使端口 8080 可供此容器外的环境使用
EXPOSE 8080

# # 定义环境变量
# ENV FLASK_APP=app.py
# ENV FLASK_RUN_HOST=0.0.0.0

# 运行 Flask 应用
CMD ["python", "app.py"]

