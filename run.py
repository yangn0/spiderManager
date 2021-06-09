from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

machine = {
    "X1": {
        "pcNum": "X1",
        "start": 1,  # -1 0 1
        "startTime": 46456213,
        "keyword": '''["壁灯", "吊灯", "吸顶灯", "落地灯", "吊扇灯", "客厅灯", "卧室灯", "LED灯", "照明灯", "灯罩灯", "台灯", "床头灯", "应急灯筒灯", "射灯", "天花灯", "厨卫灯", "节能灯","荧光灯", "白炽灯", "路灯", "水晶灯", "过道灯", "中式灯", "阳台灯", "美式灯", "日式灯", "欧式灯", "韩式灯", "地中海灯", "儿童灯", "轨道灯", "镜前灯", "杀菌灯", "麻将灯", "庭院灯", "卫浴灯", "浴霸灯"]''',
        "page": "100",
    },
}

statusDict = {"X1": {
    "pcNum": "X1",
    'nowPage': -1,
    'nowKeyword': -1,
    "lastTime": -1,
    "lastId": -1
},
}


@app.route('/', methods=["GET"])
def index():
    if request.method == 'GET':
        return render_template('index.html')


@app.route('/set', methods=["POST", "GET"])
def set():
    with open("set.json","r") as f:
        machine=json.load(f)
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        for key in data:
            if data[key] == '' or data[key]==None:
                continue
            if data['pcNum'] not in machine:
                machine[data['pcNum']]=dict()
            machine[data['pcNum']][key] = data[key]
        with open("set.json","w") as f:
            json.dump(machine,f)
        return jsonify({"code": 200, "msg": "ok"})

    if request.method == 'GET':
        return jsonify({"code": 200, "msg": "ok", "data": machine})


@app.route('/status', methods=["POST", "GET"])
def status():
    with open("status.json","r") as f:
        statusDict=json.load(f)
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        for key in data:
            if data[key] == '':
                continue
            if data['pcNum'] not in statusDict:
                statusDict[data['pcNum']]=dict()
            statusDict[data['pcNum']][key] = data[key]
        with open("status.json","w") as f:
            json.dump(statusDict,f)
        return jsonify({"code": 200, "msg": "ok"})

    if request.method == 'GET':
        return jsonify({"code": 200, "msg": "ok", "data": statusDict})


if __name__ == '__main__':
    app.run("0.0.0.0", "5000")
