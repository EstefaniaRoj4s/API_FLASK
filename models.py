class Post:
    _id_counter = 1

    def __init__(self, title, content):
        self.id = Post._id_counter
        self.title = title
        self.content = content
        Post._id_counter += 1

class Blog:
    def __init__(self, name):
        self.name = name
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def delete_post(self, post_id):
        self.posts = [post for post in self.posts if post.id != post_id]
