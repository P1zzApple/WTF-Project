from flask import Flask, render_template, url_for, request
import os
from main import present  # home page
from model import process  # specific search
from add import add  # add to db
from count import count
from config import secret_key
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key  # idk
img = os.path.join('static', 'pictures')  # output images
icon = os.path.join(img, 'pcounts.png')  # favicon


# random model
def rand_n(n):
    ran = random.randint(0, n)
    return ran


@app.route('/')
def home():
    res = present()
    n = count()  # for rand_n
    print(url_for('home'))
    return render_template('home.html', title='What to Fold', icon=icon, data=res, ran=rand_n(n))


@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html', title='About', icon=icon)


@app.route('/help')
def help():
    print(url_for('help'))
    return render_template('help.html', title='Help', icon=icon)


@app.route('/search', methods=['POST', 'GET'])
def search():  # maybe will be in home link
    if request.method == 'POST':
        name = request.form['name']
        size = request.form['size']
        color = request.form['color']
        author = request.form['author']
        diff = request.form['diff']
        spec_search = [name, size, color, author, diff]
    return render_template('search.html', title='Search', icon=icon, find=spec_search)


@app.route('/add', methods=['POST', 'GET'])
def add_model():
    if request.method == 'POST':
        name = request.form['name']
        image = request.form['image_link']
        author = request.form['author']
        color = request.form['colors']
        size = request.form['size']
        diff = request.form['diff']
        video = request.form['video']
        diagram = request.form['diagram']
        cp = request.form['cp']
        comment = request.form['comment']
        adding = [name, image, author, color, size, diff, video, diagram, cp, comment]
        add(adding)
    return render_template('add.html', title='Add', icon=icon)


# organize this better
@app.route('/model/<int:m_id>')
def model(m_id):
    data = process(m_id)
    title = data[0][1]
    micon = data[0][3]
    print(url_for('model', m_id=m_id))
    return render_template('model.html', title=title, icon=micon, data=data)


if __name__ == '__main__':
    app.run(debug=True)
