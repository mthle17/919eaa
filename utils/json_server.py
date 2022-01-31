import os, platform, socket, re, uuid
from flask import Flask, json, jsonify

from apparel.apparel import Apparel
from apparel.apparel_routes import api_apparel
from user.user import User
from user.user_routes import api_user

# Chdir to current path
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Load data
Apparel.load_items('products')
User.load_items('users')

api = Flask(__name__)

def getSystemInfo():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        return json.dumps(info)
    except Exception as e:
        print(e)

@api.route('/', methods=['GET'])
def get_root():
    return getSystemInfo()

api.register_blueprint(api_apparel)
api.register_blueprint(api_user)

if __name__ == '__main__':
    api.run(port=8888)
