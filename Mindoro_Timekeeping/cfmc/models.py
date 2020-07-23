from django.db import models
from django.db.models.signals import post_save
from PIL import Image
from django.utils.html import mark_safe

class employee(models.Model):
    status_choice = [ 
        ('P', 'Present'),
        ('L', 'Late'),
        ('A', 'Absent')
    ]
    t1 = models.IntegerField(unique=True)
    user_id = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    birthday = models.DateField(auto_now=False, null=True)
    picture = models.ImageField(default="no-avatar.png", upload_to="pic_files")
    status = models.CharField(max_length=5 , blank=True, choices=status_choice)
    class Meta:
        verbose_name_plural = ("Employees")

    def __str__(self):
        name = self.lastname + ", " + self.firstname + " " + self.middlename[0] + ". "
        return str(name)
    
    def save(self, *args, **kwargs):
        # capitalize name
        for field_name in ['firstname', 'middlename', 'lastname']:
            val = getattr(self, field_name, False)
            if val:
                # setattr(self, field_name, val.capitalize())
                setattr(self, field_name, val.upper())

        # delete old file when replacing by updating the file
        try:
            this = employee.objects.get(id=self.id)
            if this.picture != self.picture & this.picture.url != '/media/no-avatar.png':
                this.picture.delete(save=False)
            if this.name_sound != self.name_sound:
                this.name_sound.delete(save=False)
        except: pass # when new photo then we do nothing, normal case
        super(employee, self).save(*args, **kwargs)

        # resize image
        pic = Image.open(self.picture.path)
        #if pic.height > 300 or pic.width > 300:
        output_size = (300,300)
        pic = pic.resize(output_size, Image.ANTIALIAS)
        pic.save(self.picture.path)

    def thumbnail(self, *args, **kwargs):
        return mark_safe(f'<img src="{self.picture.url}" width="100" height="100" />')
        image_tag.short_description = 'Image'