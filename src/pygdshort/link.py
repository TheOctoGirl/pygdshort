import requests

def shorten(long_url:str, custom_short_url: str=None):
    
    if custom_short_url != None:
        parameters = {
            "url": long_url,
            "shorturl": custom_short_url,
            "format": "json"
        }
        shortened_url = requests.get("https://is.gd/create.php", params=parameters)
    
    else:
        parameters = {
            "url": long_url,
            "format": "json"
        }
        shortened_url = requests.get("https://is.gd/create.php", params=parameters)
    
    shortened_url = shortened_url.json()

    if "errorcode" in shortened_url:
        
        if shortened_url["errorcode"] == 1:
            raise LongUrlError(shortened_url["errormessage"])
        
        elif shortened_url["errorcode"] == 2:
            raise ShortUrlError(shortened_url["errormessage"])
        
        elif shortened_url["errorcode"] == 3:
            raise RateLimitError(shortened_url["errormessage"])
        
        else:
            raise GenericError(shortened_url["errormessage"])
        
    else:
        return shortened_url["shorturl"]


class LongUrlError(Exception):
    pass

class ShortUrlError(Exception):
    pass

class RateLimitError(Exception):
    pass

class GenericError(Exception):
    pass