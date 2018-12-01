from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Dojo objects: {self.name} {self.city}, {self.desc}"


class Ninja(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, related_name='ninja_names', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Ninja objects: {self.f_name} {self.l_name} {self.dojo.name}"
