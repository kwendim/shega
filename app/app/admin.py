from django.contrib import admin
from .models import Code

class CodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'code_type', 'is_redeemed', 'is_claimed')
    class Meta:
        model = Code

admin.site.register(Code, CodeAdmin)
