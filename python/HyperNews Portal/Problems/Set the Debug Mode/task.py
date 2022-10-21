IS_RELEASE_SERVER = input()
if IS_RELEASE_SERVER == 'true':
    IS_RELEASE_SERVER = True
else:
    IS_RELEASE_SERVER = False
if IS_RELEASE_SERVER:
    DEBUG = False
else:
    DEBUG = True
