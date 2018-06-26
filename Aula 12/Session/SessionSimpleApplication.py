from flask import Flask, render_template, session, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/visit-counter/')
def visits():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # reading and updating session data
    else:
        session['visits'] = 1 # setting session data
    return render_template('visit-counter.html', count=session.get('visits'))

@app.route('/deletedvisit')
def delete_visits():
    session.pop('visits', None) # delete visits
    return render_template('deletedvisit.html')

if __name__ == '__main__':
    app.secret_key = "My secret key"
    app.run(debug = True)