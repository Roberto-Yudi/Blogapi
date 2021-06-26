from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

class BlogTests(TestCase):

    @classmethod 
    def setUp(cls):
        User = get_user_model()
        testuser = User.objects.create_user(
            username = 'testuser', password = 'testpass'
        )
        testuser.save()

        testpost = Post.objects.create(
            title = 'test title', author = testuser, body = 'test content'
        )
        testpost.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        title = f'{post.title}'
        author = f'{post.author}'
        body = f'{post.body}'
        self.assertEqual(author,'testuser')
        self.assertEqual(title, 'test title')
        self.assertEqual(body, 'test content')

