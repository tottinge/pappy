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

def what():
    print("""Some things to try
    * auth_session(auth=token) - make an authenticated session
    * body_for(request) - get the body of the request as an object
    * what() - print this.
    ---------------------------------------------------------------
    """)

what()