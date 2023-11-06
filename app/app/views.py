from django.http import HttpResponse
from django.http import JsonResponse
from django.views.static import serve
from django.conf import settings
import os
from PIL import Image, ImageFont, ImageDraw
from PIL import ImageFont
from PIL import ImageDraw 


from .models import Code



def redeem_code(request, code):
    try:
        # import random, string
        # for i in range(20):
        #     code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        #     Code.objects.create(code=code, code_type='Beer')


        code_obj = Code.objects.get(code=code)
        if code_obj.is_redeemed:
            failure_image_path = os.path.join(settings.BASE_DIR,  'failure.png')
            img = Image.open(failure_image_path)
            response = HttpResponse(content_type='image/png')
            img.save(response, 'PNG')
            return response                

        code_obj.is_redeemed = True
        code_obj.save()

        success_image_path = os.path.join(settings.BASE_DIR,  'success.png')
        font_path = os.path.join(settings.BASE_DIR,  'myfont.ttf')


        img = Image.open(success_image_path)

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_path, 40)
        draw.text((0, 390),"Code: " + code,(255,255,255),font=font)

        response = HttpResponse(content_type='image/png')
        img.save(response, 'PNG')
        return response   

    except Code.DoesNotExist:
        failure_image_path = os.path.join(settings.BASE_DIR,  'fake.jpg')
        img = Image.open(failure_image_path)
        response = HttpResponse(content_type='image/png')
        img.save(response, 'PNG')
        return response                
