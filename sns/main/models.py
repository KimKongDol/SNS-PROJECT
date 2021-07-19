from django.db import models

# Create your models here.

class Blog(models.Model): #테이블 생성
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = "blog/", blank=True, null=True) #blog라는 폴더를 만들어서 사진을 관리할 것이고 blank와 null을 허용해서 사진이 없어도 업로드되게함

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]
