from flask import Blueprint, render_template, request, jsonify
from models import get_user_by_credentials

routes = Blueprint('routes',__name__)

TEST = 'jquery' #'jquery'  #'vue'

@routes.route('/', methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template(f'login_{TEST}.html')

    data = request.get_json() if TEST == 'vue' else request.form
    username = data.get('username')
    password = data.get('password')

    # Kiểm tra thông tin đăng nhập trong MySQL thông qua model
    user = get_user_by_credentials(username, password)
    if user:
        return jsonify({"success": True, "message": "Đăng nhập thành công!"})
    else:
        return jsonify({"success": False, "message": "Tài khoản hoặc mật khẩu không chính xác."})
