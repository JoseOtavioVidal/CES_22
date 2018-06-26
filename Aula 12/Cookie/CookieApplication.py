from flask import Flask, render_template, request, url_for, make_response

app = Flask(__name__)



@app.route('/')
def index():
   return render_template('index.html')

@app.route('/setfont', methods = ['GET', 'POST'])
def setfont():
    if request.method == 'POST':
        font = request.form['nm']
        resp = make_response(render_template('index.html'))
        resp.set_cookie('font', font)

        return resp
    return render_template('setfont.html')

@app.route('/article', methods = ['GET', 'POST'])
def article():
    if request.method == 'POST':
        print(request.form)
        res = make_response("")
        res.set_cookie("font", request.form.get('font'))
        res.headers['location'] = url_for('article')
        return res, 302

    return render_template('article.html')

if __name__ == '__main__':
    app.run(debug=True)