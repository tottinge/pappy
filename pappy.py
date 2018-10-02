from requests import get, post, put, delete, patch, Session
from box import Box

def auth_session(auth=None):
    session = Session()
    if auth:
        session.headers['Authorization'] = f'Bearer {auth}'
    return session


def body_for(request):
    return Box(request.json())

"Should run with ipython -i for interactive usage"

print("whoo: this is ready to rock")
