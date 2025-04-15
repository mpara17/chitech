from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/internship')
def internship():
    return render_template('internship.html')

@app.route('/jobs')
def jobs():
    return render_template('jobs.html')

if __name__ == '__main__':
    app.run(port=8000,debug=True) 