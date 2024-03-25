from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import secrets
# solution to db is locked
import time



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:''@localhost/flask_aws2'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
app.config['SECRET_KEY']=secrets.token_hex(16)
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float)

    def __repr__(self):
        return f"Book(Title:{self.title}, author:{self.author}, price:{self.price}.)"


@app.route('/')
def resume():
    return render_template('index.html')

@app.route('/book')
def home():
    books = Book.query.all()
    return render_template('book.html', books=books)

@app.route('/add', methods=['POST'])
def add_book():
    if request.method =='POST':
        book = Book(
            title=request.form.get('title'),
            author=request.form.get('author'),
            price=request.form.get('price'))
        db.session.add(book)
        db.session.commit()
        flash('New book added successfully.')
        return redirect(url_for('home'))


@app.route('/update', methods=['POST'])
def update():
    if request.method == "POST":
        book_id = request.form.get('id')
        the_data = Book.query.get(book_id)
        if the_data:
            the_data.title = request.form['title']
            the_data.author = request.form['author']
            the_data.price = request.form['price']
            db.session.commit()
            flash('Book updated successfully.')
        else:
            flash('Book not found.')
        return redirect(url_for('home'))

@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    book = Book.query.get(id)
    if book:
        db.session.delete(book)
        db.session.commit()
        flash('Book deleted successfully.')
    else:
        flash('Book not found.')
    return redirect(url_for('home'))


# @app.route('/resume')
# def resume():
#     return render_template('resume.html')




if __name__ =='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)