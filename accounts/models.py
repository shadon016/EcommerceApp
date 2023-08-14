from django.db import models
from django.contrib.auth.models import User


state_choices=(
    ('Dhaka','Dhaka'),
    ('Chittagong','Chittagong'),
('Sylhet','Sylhet'),
    ('Khulna','Khulna'),
('Rajshahi','Rajshahi'),
    ('Rangpur','Rangpur'),

)
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    bio=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='profile')
    state=models.CharField(max_length=30,choices=state_choices)
    city=models.CharField(max_length=20)
    town=models.CharField(max_length=20)
    zip_code=models.CharField(max_length=10)
    phone=models.IntegerField()
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user