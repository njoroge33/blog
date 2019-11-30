from .models import Quote
import requests

def get_quote():
    url = "http://quotes.stormconsultancy.co.uk/random.json"
    response = requests.get(url)
    quote_json = response.json()

    if quote_json:
        author = quote_json.get('author')
        id = quote_json.get('id')
        quote = quote_json.get('quote')
        permalink = quote_json.get('permalink')

        quote = Quote(author,id,quote,permalink)

    return quote
    