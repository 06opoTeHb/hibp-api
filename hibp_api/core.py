#The Content has been made available for informational and educational purposes only
import cfscrape,json,argparse,urllib3
from requests.adapters import HTTPAdapter
from urllib3.util.ssl_ import create_urllib3_context, DEFAULT_CIPHERS
# urllib3.util.ssl_.DEFAULT_CIPHERS = DEFAULT_CIPHERS
DEFAULT_CIPHERS += ':!SHA1'
class hibp():
    @staticmethod
    def email(email):
        class CustomAdapter(HTTPAdapter):
            def init_poolmanager(self, *args, **kwargs):
                ctx = create_urllib3_context(ciphers=DEFAULT_CIPHERS)
                super(CustomAdapter, self).init_poolmanager(*args, ssl_context=ctx, **kwargs)
        scraper = cfscrape.create_scraper()
        scraper.mount('https://', CustomAdapter())
        url = "https://haveibeenpwned.com/unifiedsearch/"+str(email)
        #print(url)
        req = scraper.get(url)
        if(req.status_code==200):
            json_data = json.loads(req.text)
            return(json_data)
