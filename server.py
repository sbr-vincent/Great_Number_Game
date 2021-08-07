from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)    
app.secret_key = 'Mellon'


@app.route('/')  
def index():
    if 'rand_num' not in session:
        session['rand_num'] = random.randint(1, 100)
    
    return render_template("index.html") 

@app.route('/compare', methods=['POST'])  
def refresh():
    session['accuracy'] = ''

    if request.form['guess'].isnumeric():
        user_guess = int(request.form['guess'])
    else:
        return redirect("/") 

    if user_guess == session['rand_num']:
        session['accuracy'] = 'correct'
    elif user_guess < session['rand_num'] and user_guess > 0:
        session['accuracy'] = 'low'
    elif user_guess > session['rand_num'] and user_guess < 101:
        session['accuracy'] = 'high'
    elif user_guess == 117:
        session.clear()
    elif user_guess <= 0 or user_guess > 100:
        session['accuracy'] = 'out'
    return redirect("/") 

@app.route('/destroy_session', methods=['POST'])  
def restart():
    session.clear()
    return redirect("/") 

    
    
if __name__=="__main__":    
    app.run(debug=True)   