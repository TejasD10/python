import requests
import json

def main(source, params):
    r"""

    The function uses the NEWS API v2 and returns the top headlines in JSON format
    :source: Pass in the source of the news
            To view all the available sources use
            https://newsapi.org/v2/sources
            If the source is None, returns the top-headlines
    :params: Comma seperated, key=value pairs as dict
    :return: List of trending articles
    """
    if not source:
        source = 'top-headlines'
    # generated apiKey from the NewsAPI.org
    apikey = '191882de17664b89ba6dfe361a25f35d'

    # Check if the params is a dict
    if not isinstance(params, dict):
        raise ValueError('Params should be key=value pair of type dict')
    paramnames = '?'

    for key, value in params.items():
        paramnames = paramnames + key + '=' + value + '&'

    URL = 'https://newsapi.org/v2/' + source + paramnames + f'apiKey={apikey}'

    try:
        response = requests.get(URL)
        response.raise_for_status()
    except Exception as exc:
        print(f'Error Occured: {exc}')

    jsonresponse = response.json()

    articles = jsonresponse['articles']
    for article in articles:
        print(article['description'])
    return list(articles)


if __name__ == '__main__':
    main('top-headlines', {'language': 'en'})
