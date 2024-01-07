from django.contrib import admin
from .models import Html_CSS, React_JS, Python_DJ, Stack
# Register your models here.

# отоюражаем в админке
admin.site.register(Html_CSS)
admin.site.register(React_JS)
admin.site.register(Python_DJ)
admin.site.register(Stack)
