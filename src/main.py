from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/useless', methods=['POST', 'GET'])
def useless():
    if request.method == 'POST':
        processed_useless_input = request.form.get('useless_input')
        try:
            return redirect(url_for(processed_useless_input))
        except:
            return redirect('404')
    return render_template('useless.html')

@app.route('/secret')
def secret():
    return render_template('secret.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
