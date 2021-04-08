from django.test import TestCase
from .models import Project, Profile

# Create your tests here.
class ProfileTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.user= User(id=1, username='njengaen', password='beau2019')
        self.user.save_user()

        self.project= Project(title = 'Test Project',userprofile = self.njenga)
        self.post.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def tearDown(self):
        Profile.objects.all().delete()

class ProjectTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='njenga')
        self.project = Project.objects.create(id=1, project='http://njenga.com', description='wtwhthstshstshst', title='test project')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_project(self):
        self.project.save_project()
        project = Project.objects.all()
        self.assertTrue(len(post) > 0)

    def test_get_projects(self):
        self.project.save()
        projects = Project.objects.all()
        self.assertTrue(len(posts) > 0)

