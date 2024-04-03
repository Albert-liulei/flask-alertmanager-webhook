from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'

@app.route('/alert', methods=['POST'])
def alert():
    # 获取当前时间
    current_time = datetime.datetime.now()
    # 格式化时间为 '年-月-日 时:分:秒' 的格式
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    # 解析 JSON 数据
    data = request.get_json()
    print("Received alert " + formatted_time + ":", data)

    # 做一些处理，比如发送邮件、短信等
    # process_alert(data)

    # 返回成功响应
    return jsonify(status="success", message="Alert received")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

