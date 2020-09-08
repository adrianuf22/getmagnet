from googlesearch import search, get_page
from lib.model.Magnet import Magnet
from urllib.parse import urlparse, parse_qs, urlunparse, urlencode
from lib.model.service.MagnetRepository import MagnetRepository
from typing import Union

def search_magnet_links(magnet: Magnet) -> Magnet:
  repository = MagnetRepository()

  for dirty_url in search(magnet.keyword(), tld="com", num=10, stop=10, pause=10):
    url = _sanitize_url(dirty_url)

    magnet_from_cache = repository.findByUrl(url)

    if magnet_from_cache is not None:
      return magnet_from_cache

    try:
      raw = get_page(url)
      html = raw.decode('utf-8')
    except Exception as err:
      print("- Error: {0}".format(err))
      continue

    if not html:
      continue

    magnet = magnet.update_from_url_content(url=url, content=html)
    if magnet.has_links():
      repository.save(magnet)
      
      return magnet
       
  return magnet

def _sanitize_url(dirty_url) -> str:
  parsedUrl = urlparse(dirty_url)
  queryStrings = parse_qs(parsedUrl.query)
  if 'ved' in queryStrings:
      del queryStrings['ved']

  urlParts = list(parsedUrl)
  urlParts[4] = urlencode(queryStrings)

  return urlunparse(urlParts)