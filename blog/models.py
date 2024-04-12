from django.db import models



class Class(models.Model):
    code = models.CharField(max_length=64)
    
    def __str__(self):
        return self.code


class Branch(models.Model):
    _class = models.ForeignKey(Class, on_delete= models.CASCADE)
    title = models.CharField(max_length=64)
    

class Exercice(models.Model):
    _class = models.ForeignKey(Class, on_delete = models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete = models.CASCADE)
    code = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    file = models.FileField(upload_to="blog/static/files")
    
    
    def __str__(self):
        return self.title
