bottle-toolbelt
======================

[![Build Status](https://travis-ci.org/paulocheque/bottle-toolbelt.png?branch=master)](https://travis-ci.org/paulocheque/bottle-toolbelt)
[![Docs Status](https://readthedocs.org/projects/bottle-toolbelt/badge/?version=latest)](http://bottle-toolbelt.readthedocs.org/en/latest/index.html)
[![Coverage Status](https://coveralls.io/repos/paulocheque/bottle-toolbelt/badge.png?branch=master)](https://coveralls.io/r/paulocheque/bash?branch=master)
[![Code Status](https://landscape.io/github/paulocheque/bottle-toolbelt/master/landscape.png)](https://landscape.io/github/paulocheque/bottle-toolbelt/)
[![PyPi version](https://pypip.in/v/bottle-toolbelt/badge.png)](https://crate.io/packages/bottle-toolbelt/)
[![PyPi downloads](https://pypip.in/d/bottle-toolbelt/badge.png)](https://crate.io/packages/bottle-toolbelt/)

**Latest version: 0.0.1 (2016/01)**

Utility methods to facilitate automation of devops tasks. Good to be used with Fabric or Invoke.

Documentation
-------------

http://bottle-toolbelt.readthedocs.org/en/latest/index.html

Your *run.py* file:

    if __name__ == "__main__":
        import bottle

        from toolbelt.middleware import cors_options # OPTIONS routes
        from toolbelt.middleware import https_safe_api_cors_lang_bench
        bottle.install(https_safe_api_cors_lang_bench)

        # Add static files routes
        from toolbelt.routes.static import *

        # Add social login routes
        from toolbelt.routes.social import *

        # VALIDATE_TOKEN=app.models.validate_token
        def validate_token(token):
            return User.objects.get(api_key=token)
        from toolbelt.auth import token_authentication

        from toolbelt.main import run
        run()

    MEMFILE_MAX_BYTES=512000 DEBUG=true SERVER=meinheld PORT=3000 python run.py


Your *handlers.py* file:

    from toolbelt.requests import p, error_response

    @route
    def x():
        p('my_param', default='__None__')
        return error_response('msg', 400)

*.env* file (for *autoenv*):

    VALIDATE_TOKEN=app.models.validate_token
    MEMFILE_MAX_BYTES=512000
    DEBUG=true
    SERVER=meinheld
    PORT=3000
    API_URL=http://localhost:8000
    STATIC_DIR=./dist
    STATIC_INDEX=index.html
