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
        font_path = os.path.join(settings.BASE_DIR,  'font.ttf')

        code_obj = Code.objects.get(code=code)

        if code_obj.is_redeemed:
            failure_image_path = os.path.join(settings.BASE_DIR,  'claimed.jpg')
            img = Image.open(failure_image_path)
            response = HttpResponse(content_type='image/png')
            img.save(response, 'PNG')
            return response         

        
        if code_obj.code_type == 'food':
            image_path = os.path.join(settings.BASE_DIR,  'food.jpg')

        if code_obj.code_type == 'hat':
            image_path = os.path.join(settings.BASE_DIR,  'hat.jpg')
        
        if code_obj.code_type == 'ticket':
            image_path = os.path.join(settings.BASE_DIR,  'refund.jpg')
        
        if code_obj.code_type == 'shirt':
            image_path = os.path.join(settings.BASE_DIR,  'shirt.jpg')
        
        if code_obj.code_type == 'try again':
            image_path = os.path.join(settings.BASE_DIR,  'try again.jpg')

        if code_obj.code_type == 'beer':
            image_path = os.path.join(settings.BASE_DIR,  'beer.jpg')

        if code_obj.code_type == 'cocktail':
            image_path = os.path.join(settings.BASE_DIR,  'cocktail.jpg')


        img = Image.open(image_path)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_path, 80)
        draw.text((420, 860),"Code: " + code,(220,59,51),font=font)
        response = HttpResponse(content_type='image/png')
        img.save(response, 'PNG')

        code_obj.is_redeemed = True
        code_obj.save()

        return response   

    except Code.DoesNotExist:
        failure_image_path = os.path.join(settings.BASE_DIR,  'try again.jpg')
        img = Image.open(failure_image_path)
        response = HttpResponse(content_type='image/png')
        img.save(response, 'PNG')
        return response                
