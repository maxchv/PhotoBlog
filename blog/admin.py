from django.contrib import admin
from .models import Post, Comment, Strana, Category
from django.db import models

# from django.forms.extras.widgets import SelectDateWidget
# from django.forms import widgets

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Strana)
admin.site.register(Category)


# class CommentAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.DateField: {'widget': SelectDateWidget},
#     }
#
#     radio_fields = {'gender': admin.HORIZONTAL}
