from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Tag, Comment
from django.utils.text import slugify

class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.tag = Tag.objects.create(name='Tech', slug=slugify('Tech'))
        self.post = Post.objects.create(
            title='Test Post',
            slug=slugify('Test Post'),
            content='This is a test post.',
            author=self.user,
            is_published=True
        )
        self.post.tags.add(self.tag)
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            content='This is a test comment.'
        )

    def test_tag_str(self):
        self.assertEqual(str(self.tag), 'Tech')

    def test_post_str(self):
        self.assertEqual(str(self.post), 'Test Post')

    def test_comment_str(self):
        self.assertEqual(str(self.comment), 'testuser: This is a test comment.')

    def test_post_slug_generation(self):
        self.assertEqual(self.post.slug, slugify('Test Post'))

    def test_post_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), reverse('post_detail', kwargs={'slug': self.post.slug}))

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.tag = Tag.objects.create(name='Tech', slug=slugify('Tech'))
        self.post = Post.objects.create(
            title='Test Post',
            slug=slugify('Test Post'),
            content='This is a test post.',
            author=self.user,
            is_published=True
        )
        self.post.tags.add(self.tag)

def test_post_list_view(self):
    response = self.client.get(reverse('post_list'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'blog/post_list.html')
    self.assertContains(response, 'react-post-list')  # چک container
    # تست API
    response_api = self.client.get('/api/posts/')
    self.assertEqual(response_api.status_code, 200)
    self.assertContains(response_api, 'Test Post')

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', kwargs={'slug': self.post.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_post_create_view_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('post_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_form.html')

    def test_post_create_view_unauthenticated(self):
        response = self.client.get(reverse('post_create'))
        self.assertEqual(response.status_code, 302)  # Redirect to login
        self.assertTrue(response.url.startswith(reverse('login')))