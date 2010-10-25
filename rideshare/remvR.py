import os

try:
    os.unlink('__init__.pyc')
except:
    pass 
try:
    os.unlink('settings.pyc')
except:
    pass 
try:
    os.unlink('urls.pyc')
except:
    pass
try:
    os.unlink('views.pyc')
except:
    pass 