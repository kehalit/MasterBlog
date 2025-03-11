import json
from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect


def load_posts():
    try:
        with open('DB/blog_posts.json', 'r') as file:
            data = json.load(file)
            if not isinstance(data, list):
                return []
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_posts(posts):
    with open('DB/blog_posts.json', 'w') as file:
        json.dump(posts, file, indent=4)

app = Flask(__name__)


@app.route('/')
def index():

    posts = load_posts()
    return render_template('index.html', posts=posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')

        posts = load_posts()

        new_post = {
                    'id': posts[-1]['id'] + 1 if posts else 1,
                    'author': author,
                    'title': title,
                    'content': content
        }

        posts.append(new_post)
        save_posts(posts)
        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/delete/<int:post_id>', methods = ['POST'])
def delete(post_id):

    posts = load_posts()
    posts = [post for post in posts if post['id'] != post_id]# Find the blog post with the given id and remove it from the list
    save_posts(posts)
    return redirect(url_for('index')) # Redirect back to the home page



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5003, debug=True)