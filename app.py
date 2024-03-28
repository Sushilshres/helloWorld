from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Sushil Shrestha! I am adding my first code change.'

@app.route('/hello')
def hello():
    return render_template('hello.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about-css')
def aboutcss():
    return render_template('about-css.html')

@app.route('/favorite-course')
def favoritecourse():
    print('Subject:' + request.args.get('subject'))
    print('Course Number:' + request.args.get('course_number'))
    print('You entered your favorite course as:' + request.args.get('subject'))
    return render_template('favorite-course.html')


@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        print('First name entered:'+request.form.get('first_name'))
        print('Last name entered:'+request.form.get('last_name'))
        print('Email entered:'+request.form.get('email'))
        print('Favorite car entered:'+request.form.get('car'))

    if request.form.get('agree_check'):
        print('Agree to be contacted entered:' + request.form.get('agree_check'))

    return render_template('contact.html')



@app.route('/base')
def base():
    return render_template('base.html')





if __name__ == '__main__':
    app.run()
