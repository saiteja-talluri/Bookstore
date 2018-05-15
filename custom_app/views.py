## @brief Views for the Custom app.


from braces.views import LoginRequiredMixin
from django.views import generic
from django.contrib.auth import get_user_model


## @brief view for the chat page of the user.
#
# This view is called by messages url.\n
# It returns to users.html 
class UserListView(LoginRequiredMixin, generic.ListView):
    model = get_user_model()
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'custom_app/users.html'
    login_url = 'admin/'
