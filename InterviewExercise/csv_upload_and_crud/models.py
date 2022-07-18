from django.db import models

class Upload(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    file = models.FileField(blank=True,default=None)
    data = models.TextField(blank=True,default=None)
    rows = models.IntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
      db_table = "upload"
    
    def __str__(self):
       return f"{self.file} {self.data}"
    
    def __repr__(self):
        return f"{self.file} {self.data}"
