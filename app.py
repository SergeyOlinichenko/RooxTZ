from flask import Flask
from flask import request
import json
from Users import Users


app = Flask(__name__)


@app.route('/user', methods=['GET'])
def getUserNameById():
    id = request.args.get('id')
    for user in Users.userlist:
        if id == None:
            return "Id is none"
        elif id == "":
            return "Id is empty"
        elif id == user.id:
            return json.dumps(user.__dict__)
    return "Id is not found"


if __name__ == '__main__':
    app.run(debug=False)
