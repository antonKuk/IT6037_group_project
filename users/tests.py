# from datetime import date
# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from django.urls import reverse

# from blog.models import Post,Comment,Author

# '''Model Test'''

# class PostTests(TestCase):
#     @classmethod
#     def setUpTestData(self):
#         self.author = Author.objects.create(
#             first_name="testuser", last_name="lastname", email_address="test@gmail.com")

#         self.post = Post.objects.create(title="this is a test!",excerpt="test!",date = date.today(),content="content test")

#     def test_model_content(self):
#         self.assertEqual(self.post.title, "this is a test!")
#         self.assertEqual(self.post.excerpt, "test!")
#         self.assertEqual(self.post.date, date.today())
#         self.assertEqual(self.post.content, "content test")

# '''User Test'''

# class UserAccountTests(TestCase):

#     def test_new_superuser(self):
#         db = get_user_model()
#         super_user = db.objects.create_superuser(email='new_admin@gmail.com', username='username', first_name='firstname')
#         self.assertEqual(super_user.email, 'new_admin@gmail.com')
#         self.assertEqual(super_user.username, 'username')
#         self.assertEqual(super_user.first_name, 'firstname')
#         self.assertTrue(super_user.is_superuser)
#         self.assertTrue(super_user.is_staff)
#         self.assertTrue(super_user.is_active)
#         self.assertEqual(str(super_user), "username")

#     def test_new_user(self):
#         db = get_user_model()
#         user = db.objects.create_user(username='username',email='samuel@gmail.com',first_name = 'firstname')
#         self.assertEqual(user.email, 'samuel@gmail.com')
#         self.assertEqual(user.username, 'username')
#         self.assertEqual(user.first_name, 'firstname')
#         self.assertFalse(user.is_superuser)
#         self.assertFalse(user.is_staff)
  