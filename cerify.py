import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

URL = 'https://results.cusat.ac.in'
session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

print(session.get(URL))