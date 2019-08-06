from django.db import models

# Create your models here.


# About us model (who we are,mission-vision,board of director,message from CEO ,Management,corporate facilities service
class WhoWeAre(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class MissionVision(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField()
    image=models.ImageField(blank=True,null=True)


    def __str__(self):
        return self.title


class BoardOfDirector(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField()
    image=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.title


class MessageFromCEO(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField()
    image=models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.title



class Management(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField()
    image=models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.title

#corporate facilities service

class CorporateFacilitiesService(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField()
    image=models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.title