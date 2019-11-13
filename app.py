from flask import Flask, render_template, request

app = Flask(__name__)
app.template_folder = 'templates'


@app.route('/sign')
def sign():
    return render_template("signup.html")


@app.route('/signup/', methods=['POST','GET'])
def signup():
    data = request.form
    username = data.get("username")
    if not(len(username) >=5 and len(username) <=10):#如果不满足5-10字符就会返回错误提示
        return "请输入正确的用户名，要求在5-10位字符"
    phone = data.get("phone")
    if not(len(phone) ==11):#如果不满足11字符就会返回错误提示
        return "请输入正确的手机号，要求在11位字符"
    password = data.get("password")
    if not(len(password) >=3 and len(password) <=10):#如果不满足3-10字符就会返回错误提示
        return "请输入正确的密码，要求在3-10位字符"

    return "username:{} phone:{} password:{} ".format(username, phone, password)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='6060')
