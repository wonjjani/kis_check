from flask import Flask, render_template, request
import kis_api

app = Flask(__name__)

@app.route("/")
@app.route("/inf_send")
def send_inf():
    return render_template('inf_send.html')

@app.route('/inf_recv', methods=['POST'])
def inf_recv():
    if request.method == 'POST':
        app_secret = request.form.get('app_secret')
        app_key = request.form.get('app_key')
        acc_no = request.form.get('acc_no')
        operation = request.form.get('operation')

        

        if operation == "get_token":
            token = kis_api.get_token(app_key=app_key, app_secret=app_secret)
            if token:
                data = token

            else:
                data = {
                    "error" : "token error"
                }

        if operation == "mesoo" or operation == "medo":
            stock_code = request.form.get('stock_code')
            quantity = request.form.get('quantity')

            if operation == "mesoo":
                mesoo_response = kis_api.mesoo(app_key=app_key, app_secret=app_secret, acc_no=acc_no, stock_code=stock_code, quantity=quantity)
                data = mesoo_response

            if operation == "medo":
                medo_response = kis_api.medo(app_key=app_key, app_secret=app_secret, acc_no=acc_no, stock_code=stock_code, quantity=quantity)
                data = medo_response

    else:
        data = {"method_error": "method_error"}

    return render_template('inf_recv.html', data=data)


if __name__ == '__main__':
    app.run(debug=True) 
