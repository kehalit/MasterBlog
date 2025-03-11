import json
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


def fetch_post_by_id(post_id):
   posts = load_posts()
   for post in posts:
       if post['id'] == post_id:
           return post
       return None
