from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to display in the list view
    list_filter = ('author', 'publication_year')  # Fields to filter by
    search_fields = ('title', 'author')  # Fields to search by

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'date_of_birth', 'is_staff', 'is_active']
    list_filter = ['email', 'is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)



from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

class Command(BaseCommand):
    help = 'Set up initial groups and permissions'

    def handle(self, *args, **kwargs):
        # Create groups
        editors_group, created = Group.objects.get_or_create(name='Editors')
        viewers_group, created = Group.objects.get_or_create(name='Viewers')
        admins_group, created = Group.objects.get_or_create(name='Admins')

        # Get permissions
        content_type = ContentType.objects.get_for_model(Book)
        can_view = Permission.objects.get(codename='can_view', content_type=content_type)
        can_create = Permission.objects.get(codename='can_create', content_type=content_type)
        can_edit = Permission.objects.get(codename='can_edit', content_type=content_type)
        can_delete = Permission.objects.get(codename='can_delete', content_type=content_type)

        # Assign permissions to groups
        editors_group.permissions.add(can_create, can_edit)
        viewers_group.permissions.add(can_view)
        admins_group.permissions.add(can_view, can_create, can_edit, can_delete)

        self.stdout.write(self.style.SUCCESS('Successfully set up groups and permissions'))