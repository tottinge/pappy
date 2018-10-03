from requests import get, post, put, delete, patch, Session
from box import Box

def auth_session(auth=None, base=None):
    import types
    def rget(s, relative, **vargs):
        return s.get(f'{s.base}/{relative}', **vargs)
    session = Session()
    if auth:
        session.headers['Authorization'] = f'Bearer {auth}'
    session.base = base or ''
    session.rget = types.MethodType(rget, session)
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
