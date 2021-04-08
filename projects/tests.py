from django.test import TestCase
from .models import Project, Profile

# Create your tests here.
class ProfileTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.njenga= User(id=1, username='njengaen', password='beau2019')
        self.njenga.save_user()

        self.post= Site(title = 'Test Post',userprofile = self.njenga)
        self.post.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def tearDown(self):
        Profile.objects.all().delete()
        Project.objects.all().delete()
