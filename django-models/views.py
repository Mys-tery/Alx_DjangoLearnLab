from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# Role check helper
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# Admin-only view
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "admin_view.html")
