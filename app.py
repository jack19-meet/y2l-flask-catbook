from flask import Flask
from flask import render_template
from database import get_all_cats, find_cat , create_cat

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    new_cat = create_cat('add cat')
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:id>')
def view_details(id):
	# cat = find_cat(number)
	return render_template("cat.html")


if __name__ == '__main__':
   app.run(debug = True)
