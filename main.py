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
    clothes = [
      {'img': "/static/img/mens-blazer.jpg",  'title': 'Blazer',   'text': 'Placeholder text'},
      {'img': "/static/img/mens-shirts.jpg",  'title': 'Shirt',    'text': 'Placeholder text'},
      {'img': "/static/img/mens-pants.webp",   'title': 'Pants',    'text': 'Placeholder text'},
      {'img': "/static/img/mens-shoes.jpg",  'title': 'Shoes',   'text': 'Placeholder text'},
      {'img': "/static/img/mens-sweater.jpg", 'title': 'Sweater',  'text': 'Placeholder text'},
      {'img': "/static/img/mens-tshirt.jpg",  'title': 'Tshirt',   'text': 'Placeholder text'}
      
    ]
    return render_template('male.html', clothes=clothes)

@app.route('/female')
def female():
    return render_template('female.html')

@app.route('/non-binary')
def nonbinary():
    return render_template('nonbinary.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)