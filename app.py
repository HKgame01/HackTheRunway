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

if __name__ == "__main__":
    app.run(debug=True)