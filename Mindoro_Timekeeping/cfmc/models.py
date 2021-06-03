import os
from PIL import Image
from django.db import models
from django.utils.html import mark_safe
from django.db.models.signals import post_save
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError


def content_file_name1(instance, filename):
    try:
        old_file = employee.objects.get(pk=instance.pk).picture1
        print(old_file.path)
        if old_file != 'no-avatar.png':
            os.remove(old_file.path)
    except:
        pass
    ext = filename.split('.')[-1]
    filename = f"{instance.id}.{ext}"
    return os.path.join('pic_files', filename)

def content_file_name2(instance, filename):
    try:
        old_file = employee.objects.get(pk=instance.pk).picture2
        print(old_file.path)
        if old_file != 'no-avatar.png':
            os.remove(old_file.path)
    except:
        pass
    ext = filename.split('.')[-1]
    filename = f"{instance.id}.{ext}"
    return os.path.join('pic_files', filename)

def content_file_name3(instance, filename):
    try:
        old_file = employee.objects.get(pk=instance.pk).picture3
        print(old_file.path)
        if old_file != 'no-avatar.png':
            os.remove(old_file.path)
    except:
        pass
    ext = filename.split('.')[-1]
    filename = f"{instance.id}.{ext}"
    return os.path.join('pic_files', filename)

def content_file_name4(instance, filename):
    try:
        old_file = employee.objects.get(pk=instance.pk).picture4
        print(old_file.path)
        if old_file != 'no-avatar.png':
            os.remove(old_file.path)
    except:
        pass
    ext = filename.split('.')[-1]
    filename = f"{instance.id}.{ext}"
    return os.path.join('pic_files', filename)

def content_file_name5(instance, filename):
    try:
        old_file = employee.objects.get(pk=instance.pk).picture5
        print(old_file.path)
        if old_file != 'no-avatar.png':
            os.remove(old_file.path)
    except:
        pass
    ext = filename.split('.')[-1]
    filename = f"{instance.id}.{ext}"
    return os.path.join('pic_files', filename)



class employee(models.Model):
    user_id = models.CharField(max_length=50, unique=True)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    birthday = models.DateField(auto_now=False, null=True)
    picture1 = models.ImageField(upload_to="content_file_name1")
    picture2 = models.ImageField(upload_to="content_file_name2")
    picture3 = models.ImageField(upload_to="content_file_name3")
    picture4 = models.ImageField(upload_to="content_file_name4")
    picture5 = models.ImageField(upload_to="content_file_name5")

    class Meta():
        verbose_name_plural = ("Employees")

    def __str__(self):
        name = self.lastname + ", " + self.firstname + \
            " " + self.middlename[0] + ". "
        return str(name)

    def save(self, *args, **kwargs):
        # capitalize name
        for field_name in ['firstname', 'middlename', 'lastname']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.upper())

        super(employee, self).save(*args, **kwargs)

        # resize image
        try:
            output_size = (450, 450)
            pic1 = Image.open(self.picture1.path)
            pic1 = pic1.resize(output_size, Image.ANTIALIAS)
            pic1.save(self.picture1.path)
            pic2 = Image.open(self.picture2.path)
            pic2 = pic2.resize(output_size, Image.ANTIALIAS)
            pic2.save(self.picture2.path)
            pic3 = Image.open(self.picture3.path)
            pic3 = pic3.resize(output_size, Image.ANTIALIAS)
            pic3.save(self.picture3.path)
            pic4 = Image.open(self.picture4.path)
            pic4 = pic4.resize(output_size, Image.ANTIALIAS)
            pic4.save(self.picture4.path)
            pic5 = Image.open(self.picture5.path)
            pic5 = pic5.resize(output_size, Image.ANTIALIAS)
            pic5.save(self.picture5.path)
        except:
            pass

        try:
            thisa = employee.objects.get(pk = self.pk)
            fil1 = str(thisa.picture1)
            filename1 = (fil1.split('/'))[1]
            filenumber1 = filename1.split('.')[0]
            ext = filename1.split('.')[1]
            final_filename1 = f"{self.pk}_1.{ext}"
            if str(self.pk)+"_1" != str(filenumber1):
                os.rename(str(thisa.picture1.path), f"/home/pi/Desktop/Mindoro-Timekeeping/Mindoro_Timekeeping/media/pic_files/{final_filename1}")
                thisa.picture1 = f"pic_files/{final_filename1}"
                print("pk is different to picture1 number")
                thisa.save()
            fil2 = str(thisa.picture2)
            filename2 = (fil2.split('/'))[1]
            filenumber2 = filename2.split('.')[0]
            final_filename2 = f"{self.pk}_2.{ext}"
            if str(self.pk)+"_2" != str(filenumber2):
                os.rename(str(thisa.picture2.path), f"/home/pi/Desktop/Mindoro-Timekeeping/Mindoro_Timekeeping/media/pic_files/{final_filename2}")
                thisa.picture2 = f"pic_files/{final_filename2}"
                print("pk is different to picture2 number")
                thisa.save()
            fil3 = str(thisa.picture3)
            filename3 = (fil3.split('/'))[1]
            filenumber3 = filename3.split('.')[0]
            final_filename3 = f"{self.pk}_3.{ext}"
            if str(self.pk)+"_3" != str(filenumber3):
                os.rename(str(thisa.picture3.path), f"/home/pi/Desktop/Mindoro-Timekeeping/Mindoro_Timekeeping/media/pic_files/{final_filename3}")
                thisa.picture3 = f"pic_files/{final_filename3}"
                print("pk is different to picture3 number")
                thisa.save()
            fil4 = str(thisa.picture4)
            filename4 = (fil4.split('/'))[1]
            filenumber4 = filename4.split('.')[0]
            final_filename4 = f"{self.pk}_4.{ext}"
            if str(self.pk)+"_4" != str(filenumber4):
                os.rename(str(thisa.picture4.path), f"/home/pi/Desktop/Mindoro-Timekeeping/Mindoro_Timekeeping/media/pic_files/{final_filename4}")
                thisa.picture4 = f"pic_files/{final_filename4}"
                print("pk is different to picture4 number")
                thisa.save()
            fil5 = str(thisa.picture5)
            filename5 = (fil5.split('/'))[1]
            filenumber5 = filename5.split('.')[0]
            final_filename5 = f"{self.pk}_5.{ext}"     
            if str(self.pk)+"_5" != str(filenumber5):
                os.rename(str(thisa.picture5.path), f"/home/pi/Desktop/Mindoro-Timekeeping/Mindoro_Timekeeping/media/pic_files/{final_filename5}")
                thisa.picture5 = f"pic_files/{final_filename5}"
                print("pk is different to picture5 number")
                thisa.save()
            

            os.system("rm -f /home/pi/facial/IMAGE/*")
            print("UPDATING IMAGES")
            os.system("cp /home/pi/Desktop/Mindoro-Timekeeping/Mindoro_Timekeeping/media/pic_files/* /home/pi/facial/IMAGE")
            print("IMAGES UPDATED")
        except Exception as ex:
            print(ex)

    def delete(self, *args, **kwargs):
        print("deleting")
        super(employee, self).delete(*args, **kwargs)
        try:
            print("DELETING IMAGE")
            os.remove(self.picture1.path)
            os.remove(self.picture2.path)
            os.remove(self.picture3.path)
            os.remove(self.picture4.path)
            os.remove(self.picture5.path)
            
            os.system("rm -f /home/pi/facial/IMAGE/*")
            print("UPDATING IMAGES")
            os.system("cp /home/pi/Desktop/Mindoro-Timekeeping/Mindoro_Timekeeping/media/pic_files/* /home/pi/facial/IMAGE")
            print("IMAGES UPDATED")
        except Exception as ex:
            print(ex)

    def thumbnail(self, *args, **kwargs):
        return mark_safe(f'<img src="{self.picture1.url}" width="100" height="100" />')
        image_tag.short_description = 'Image'

    def action(self,  *args, **kwargs):
        return mark_safe(f'''<input type="button" onclick="location.href='/cfmc/record/{self.id}'" style="height:25px; padding: 5px 15px; font-weight: bolder;" value="Records" />''')


class logbox(models.Model):
    transact_choice = [('I', 'IN'), ('O', 'OUT')]
    employee = models.ForeignKey(
        employee, on_delete=models.CASCADE)
    date_time = models.DateTimeField(null=True, blank=True)
    transaction = models.CharField(max_length=1, choices=transact_choice)

    class Meta:
        verbose_name_plural = "Logbox"

    def __str__(self):
        employee = str(self.employee)
        return str(employee)
