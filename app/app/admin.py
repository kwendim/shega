from django.contrib import admin
from .models import Code
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class CodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'code_type', 'is_redeemed', 'is_claimed')
    class Meta:
        model = Code

admin.site.register(Code, CodeAdmin)


admin.site.unregister(User)
admin.site.unregister(Group)
