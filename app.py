from flask import Flask, render_template, request, session, redirect, url_for
from db_utils import get_all, add, get, confirm, autoadd

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = b'_5#y2LF4T78Y8znxec%$'

@app.route('/')
def homepage():
    return render_template('parallax-template/index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['pass'] = request.form['password']
        return redirect(url_for('admin'))
    elif request.method == 'GET':
        return render_template('login.html')

@app.route('/invite/<id>', methods=['GET', 'POST'])
def invite(id):
    if id:
        invite_data = get(id)
    else:
        return render_template('non-existent.html')
    
    if not invite_data:
        return render_template('non-existent.html')
    
    if request.method == 'GET':
        return render_template('parallax-template/index.html', invite_data=invite_data, confirmed=False)
    elif request.method == 'POST':
        confirm(id, request.form.to_dict())
        return render_template('parallax-template/index.html', invite_data=invite_data, confirmed=True)
    
@app.route('/admin', methods=['POST', 'GET'])
def admin():
    if request.method == 'GET':
        try:
            if session['username'] != 'admin' and session['password'] != 'welcomezyd':
                return redirect(url_for('login'))
        except KeyError:
            return redirect(url_for('login'))
        
        data = get_all()
        totals = 

        return render_template('admin.html', data=data)
    
    elif request.method == 'POST':
        autoadd(request.form.to_dict())
        return redirect('admin')