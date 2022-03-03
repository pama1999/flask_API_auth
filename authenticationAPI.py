from flask import Flask,request
import json
app = Flask(__name__)

@app.route('/api/v1/result', methods=['GET'])
def hello_world():
    with open('data.json', 'r') as database:
        data = json.loads(database.read())
    print(data)

    key = request.args.get('api')

    for user in data['users']:
        if key == user['key']:
            return "Access granted! your status is " + user['status']
        else:
            return "Sorry your status is not Active"

if __name__ == '__main__':
    app.run()
