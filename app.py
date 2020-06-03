from flask import Flask,render_template
import use_me

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('main.html')

@app.route('/v')
def visu():
    return render_template('visu.html')

@app.route('/first')
def first():
    return render_template('index.html')

@app.route('/s')
def first1():
    return render_template('second.html')



@app.route('/admin')
def seperate():
    use_me.main()
    return render_template('index.html')

if __name__ == '__main__':
   app.run()
