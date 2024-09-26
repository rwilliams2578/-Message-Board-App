from django.views.generic import ListView
from .models import Post


class HomePageView(ListView):
    """Home Page View"""

    # After defining what model to use here,
    # the ListView we are inheriting from will
    # automatically fetch out all posts from the DB
    # and store that in a variable called post_list
    # that is then passed to the template.
    # we can't see this magic!
    # The "formula" is always <model_name>_list
    # where <model_name> is the name of the model
    # converted to lower case.
    model = Post
    template_name = "home.html"
