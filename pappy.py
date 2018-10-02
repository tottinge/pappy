from requests import get, post, put, delete, patch
from box import Box


def body_for(request):
    return Box(request.json())

"Should run with ipython -i for interactive usage"

print("whoo: this is ready to rock")
