from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')
# hi
@app.route('/')
def home():
    return render_template('Allarin.html')

@app.route('/signup')
def signup():
    return render_template('Sign up.html')

@app.route('/signin')
def signin():
    return render_template('Sign in.html')

if __name__ == '__main__':
    app.run(debug=True)
