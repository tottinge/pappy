from requests import get, post, put, delete, patch, Session
from box import Box
import os

def _load_extensions(path):
    """
    _load_extensions(path)

    Where path is a directory containing extension modules, 
    basically python scripts containing functions to make testing
    easier.

    Note: loads all python files in 'path' to the global namespace.
    This has obvious risks. Don't override important python behaviors 
    accidentally!
    """
    import sys  
    import importlib

    sys.path.append(path)
    imports = [ filename 
        for filename in os.listdir(path)
        if not filename.startswith('__') 
            and not filename.startswith('.') 
        ]
    for filename in imports:
        module_name, _ = os.path.splitext(filename)
        module = importlib.import_module(module_name)
        for attribute_name in dir(module):
            if attribute_name.startswith('__'):
                continue
            globals()[attribute_name] = getattr(module,attribute_name)
            print(f"* {attribute_name} <---({module_name})")

if os.path.isdir('local_extensions'):
    _load_extensions('local_extensions')

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
    * auth_session(auth=token, base=url) - make a session
    * body_for(request) - get the body of the request as an object
    * what() - print this.
    ---------------------------------------------------------------
    """)

what()
