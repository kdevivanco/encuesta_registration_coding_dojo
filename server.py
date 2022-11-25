from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' 

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/redirect',methods = ['POST'])
def direction():
    session['form_answer'] = request.form
    print(session['form_answer'])
    return redirect('/result')

@app.route('/result')
def show_result():
    user_input = session['form_answer']
    print(user_input['name'])
    print(user_input['city'])
    print(user_input['fav_lan'])
    return render_template('result.html',user_input=user_input)

@app.route('/return',methods = ['POST'])
def return_():
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)