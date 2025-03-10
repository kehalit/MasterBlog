from xml.etree.ElementTree import indent

from flask import Flask, render_template, request
import json


blog_posts = [
    {'id': 1, 'author': 'John Doe', 'title': 'First Post', 'content': 'This is my first post.'},
    {'id': 2, 'author': 'Jane Doe', 'title': 'Second Post', 'content': 'This is another post.'},
    # More blog posts can go here...
]

with open ('DB/blog_posts.json', 'w') as file:
    json.dump(blog_posts, file, indent=4)


app = Flask(__name__)


@app.route('/')
def index():

    with open ('DB/blog_posts.json', 'r') as file:
        blog_posts = json.load(file)
    return render_template('index.html', posts=blog_posts)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5003, debug=True)