from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    items = [
        {'id': 1, 'gender': 'Male', 'link':'/male'},
        {'id': 2, 'gender': 'Female', 'link':'/female'},
        {'id': 3, 'gender': 'Non-Binary', 'link':'/non-binary'},
        
    ]
    return render_template('home.html', items=items)


@app.route('/male')
def male():
    return render_template('male.html')

@app.route('/female')
def female():
    return render_template('female.html')

@app.route('/non-binary')
def nonbinary():
    return render_template('nonbinary.html')


if __name__ == "__main__":
    app.run(debug=True)