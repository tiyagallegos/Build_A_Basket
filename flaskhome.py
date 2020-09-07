from flask import Flask, render_template
app = Flask(__name__)

families = [
    {
        'last_name': 'Gonzalez',
        'total_members': 3,
        'adolescents': 1,
        'infants': 0,
        'adults': 2,
        'closest_city': 'Denver',
        'comments':'JJ is 6 and loves Elmo',
        'date_posted': 'September 20, 2020',
        'needs': 'food, toiletries, clothing'
    },
      {
        'last_name': 'Sanchez',
        'total_members': 5,
        'adolescents': 1,
        'infants': 1,
        'adults': 2,
        'closest_city': 'Aurora',
        'comments':'bottles and formula would be super helpful',
        'date_posted': 'September 20, 2020',
        'needs': 'food, clothing'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', families=families)

@app.route("/detail")
def detail():
    return render_template('detail.html', families=families)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)