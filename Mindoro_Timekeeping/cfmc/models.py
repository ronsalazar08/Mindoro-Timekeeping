from django.db import models
from django.db.models.signals import post_save
from PIL import Image
from django.utils.html import mark_safe
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


# def qtest(o, x):
#     try:
#         q = employee.objects.raw(f'SELECT * FROM cfmc_employee WHERE (t1 = {x} and user_id != {o}) or (t2 = {x} and user_id != {o}) or (t3 = {x} and user_id != {o}) or (t4 = {x} and user_id != {o}) or (t5 = {x} and user_id != {o})')
#         return len(q)
#     except:
#         return 0
class employee(models.Model):
    status_choice = [
        ('P', 'PRESENT'),
        ('A', 'ABSENT')
    ]
    t1 = models.IntegerField(unique=True)
    t2 = models.IntegerField(unique=True)
    t3 = models.IntegerField(unique=True)
    t4 = models.IntegerField(unique=True)
    t5 = models.IntegerField(unique=True)
    user_id = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    birthday = models.DateField(auto_now=False, null=True)
    picture = models.ImageField(default="no-avatar.png", upload_to="pic_files")
    status = models.CharField(max_length=5, blank=True, choices=status_choice)

    class Meta():
        verbose_name_plural = ("Employees")
        # unique_together = (('t5', 't4', 't3', 't2',),)
        unique_together = (('t1', 't2', 't3', 't4', 't5'),)
    # class Meta:
        # constraints = [
        #     models.UniqueConstraint(fields=['t1', 't2', 't3', 't4', 't5',], name='name of constraint')
        # ]
    

    # def clean(self, *args, **kwargs):
    #     # my_unique_fields = ['t1', 't2', 't3', 't4', 't5']
    #     # values = []
    #     # for field in my_unique_fields:
    #     #     values.append(getattr(self, field))
    #     # if len(values) != len(my_unique_fields):
    #     t1 = qtest(self.user_id, self.t1)
    #     t2 = qtest(self.user_id, self.t2)
    #     t3 = qtest(self.user_id, self.t3)
    #     t4 = qtest(self.user_id, self.t4)
    #     t5 = qtest(self.user_id, self.t5)
    #     if t1 >= 0 or t2 >= 0 or t3 >= 0 or t4 >= 0 or t5 >= 0:
    #         raise ValidationError(_('Some Trace Number are already in use.'))
    #     super(employee, self).clean(*args, **kwargs)

    def __str__(self):
        name = self.lastname + ", " + self.firstname + \
            " " + self.middlename[0] + ". "
        return str(name)

    def save(self, *args, **kwargs):
        # self.full_clean()
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
            # if this.name_sound != self.name_sound:
            #     this.name_sound.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super(employee, self).save(*args, **kwargs)

        # resize image
        pic = Image.open(self.picture.path)
        # if pic.height > 300 or pic.width > 300:
        output_size = (300, 300)
        pic = pic.resize(output_size, Image.ANTIALIAS)
        pic.save(self.picture.path)

    def thumbnail(self, *args, **kwargs):
        return mark_safe(f'<img src="{self.picture.url}" width="100" height="100" />')
        image_tag.short_description = 'Image'

    def action(self,  *args, **kwargs):
        return mark_safe(f'''<input type="button" onclick="location.href='/cfmc/record/{self.id}'" style="height:25px; padding: 5px 15px; font-weight: bolder;" value="Records" />''')


class logbox(models.Model):
    transact_choice = [('I', 'IN'), ('O', 'OUT')]
    employee = models.ForeignKey(
        employee, to_field="t1", db_column="t1", on_delete=models.CASCADE)
    date_time = models.DateTimeField(null=True, blank=True)
    transaction = models.CharField(max_length=1, choices=transact_choice)

    class Meta:
        verbose_name_plural = "Logbox"

    def __str__(self):
        employee = str(self.employee)
        return str(employee)
