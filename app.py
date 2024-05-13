from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define Movie model
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    actors = db.Column(db.String(200), nullable=False)
    publication_year = db.Column(db.Integer, nullable=False)

# Function to create database tables
def addcontext():
    with app.app_context():
        db.create_all()

# Route to display list of movies
@app.route('/movies')
def movies():
    movies = Movie.query.all()
    return render_template('movies.html', movies=movies)

# Route to add a new movie
@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        actors = request.form['actors']
        publication_year = request.form['publication_year']
        new_movie = Movie(title=title, genre=genre, actors=actors, publication_year=publication_year)
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('movies'))
    return render_template('add_movie.html')

if __name__ == '__main__':
    # Create database tables
    addcontext()
    # Run Flask application
    app.run(debug=True)

