from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
# Create your models here.
class Webqrcode(models.Model):
    name = models.CharField(max_length=30, null=True)
    about = models.CharField(max_length=255, null=True)
    phone = models.IntegerField(null=True)
    qr_code = models.ImageField(blank=True)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        info = f'Name: ' + f'{self.name} \n' + f'Phone no: ' + f'{self.phone} \n' + f'About me: ' + f'{self.about}'
        qrcode_img = qrcode.make(info)
        canvas = Image.new('RGB',(620,620), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qrcode-{info}'+'.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)