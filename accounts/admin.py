from django.contrib import admin
from .models import Profile, Branch

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'branch', 'role')
    list_filter = ('branch', 'role')

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name',)
