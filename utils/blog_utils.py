import json
def load_posts():
    """
       Load all blog posts from the JSON storage file.

       Returns:
           list: A list of blog post dictionaries. Returns an empty list if the file is missing,
           corrupt, or does not contain a valid list.
       """
    try:
        with open('DB/blog_posts.json', 'r') as file:
            data = json.load(file)
            if not isinstance(data, list):
                return []
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_posts(posts):
    """
        Save the list of blog posts to the JSON storage file.

        Args:
            posts (list): A list of blog post dictionaries to be saved.
        """
    with open('DB/blog_posts.json', 'w') as file:
        json.dump(posts, file, indent=4)


def fetch_post_by_id(post_id):
    """
        Fetch a single blog post by its unique ID.

        Args:
            post_id (int): The unique identifier of the blog post.

        Returns:
            dict or None: Returns the blog post dictionary if found, otherwise None.
        """
    posts = load_posts()
    for post in posts:
       if post['id'] == post_id:
        return post
    return None
