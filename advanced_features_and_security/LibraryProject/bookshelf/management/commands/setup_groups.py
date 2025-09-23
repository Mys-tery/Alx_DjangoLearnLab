from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = "Setup default groups and assign permissions"

    def handle(self, *args, **kwargs):
        # Define group-permission mapping
        group_permissions = {
            "Viewers": ["can_view"],
            "Editors": ["can_view", "can_create", "can_edit"],
            "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
        }

        for group_name, perms in group_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for codename in perms:
                try:
                    permission = Permission.objects.get(codename=codename)
                    group.permissions.add(permission)
                except Permission.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f"Permission {codename} not found"))
            group.save()

        self.stdout.write(self.style.SUCCESS("Groups and permissions have been set up."))
