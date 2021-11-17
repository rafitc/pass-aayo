import os
import ssl                                        
openssl_dir, openssl_cafile = os.path.split(      
    ssl.get_default_verify_paths().openssl_cafile)
# no content in this folder
os.listdir(openssl_dir)
# non existent file
print(os.path.exists(os.path.join(openssl_dir, openssl_cafile)))

import platform
# ...

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
ssl_context.verify_mode = ssl.CERT_REQUIRED
ssl_context.check_hostname = True
ssl_context.load_default_certs()

if platform.system().lower() == 'darwin':
    import certifi
    ssl_context.load_verify_locations(
        cafile=os.path.relpath(certifi.where()),
        capath=None,
        cadata=None)

import urllib.request
# previous context
https_handler = urllib.request.HTTPSHandler(context=ssl_context)
url = "http://results.cusat.ac.in"
opener = urllib.request.build_opener(https_handler)
ret = opener.open(url, timeout=2)