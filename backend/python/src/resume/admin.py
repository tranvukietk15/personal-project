from django.contrib import admin
from django.utils.html import format_html
from .models import Profile, Experience, CategorySkill, Skill
import json
# Register your models here.

@admin.register(Experience)
class CategoryAdmin(admin.ModelAdmin):
    def profile_name(self):
        return self.profile.name
    list_display = ('company_name', profile_name)
# admin.site.register(CategorySkill)

@admin.register(CategorySkill)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    def category_admin(self):
        return self.category.name

    list_display = ['name', category_admin]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # fields = ('path', 'name', 'birth_day', 'avatar')
    list_display = ('name', 'admin_image')
    search_fields = ['name']

    def save_model(self, request, obj, form, change):
        print('1111111')
        # print(json.dumps(form))
        print(request)
        # print(json.dumps(request))
        print('22222222')
        super().save_model(request, obj, form, change)

# admin.site.register(Profile, ProfileAdmin)