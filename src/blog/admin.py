from django.contrib import admin
from django_admin_hstore_widget.forms import HStoreFormField
from .models import Post_Bio, Post_Projet, Post_Experience
from django.contrib import admin
from django import forms

admin.site.register(Post_Bio)
admin.site.register(Post_Projet)

class PostExperienceAdminForm(forms.ModelForm):
    langage_prog = HStoreFormField()
    class Meta:
        model = Post_Experience
        exclude = ()


@admin.register(Post_Experience)
class PostExperienceAdmin(admin.ModelAdmin):
    form = PostExperienceAdminForm