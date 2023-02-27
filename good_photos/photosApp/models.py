from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class Image(models.Model):
    img_id = models.PositiveSmallIntegerField()
    img_name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    image=models.ImageField(upload_to='uploads/images/')

class User(models.Model):
    username = models.CharField(max_length=40)
    email = models.EmailField()
    password=models.CharField(max_length=300)

    def register(self):
        self.save()
   
    def isExists(self):
        if User.objects.filter(email=self.email):
            return True
        return False

    @staticmethod
    def get_user_by_email(email):
        try:
            return User.objects.get(email=email)
        except:
            return False

class Seller(models.Model):
    seller_id = models.CharField(max_length=30)
    seller_email = models.EmailField()
    seller_pass = models.CharField(max_length=300)

class Package(models.Model):
    package_name = models.CharField(max_length=50)
    def __str__(self):
        return self.package_name

class Subscriber(models.Model):
    sub_id = models.PositiveSmallIntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Package = models.ForeignKey(Package, on_delete=models.CASCADE)
