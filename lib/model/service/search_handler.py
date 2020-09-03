from googlesearch import search, get_page
from lib.model.Magnet import Magnet
from lib.model.service.MagnetRepository import MagnetRepository
from typing import Union

def search_magnet_links(magnet: Magnet) -> Magnet:
  repository = MagnetRepository()

  for url in search(magnet.keyword(), tld="com", num=10, stop=10, pause=10):
    magnet_from_cache = repository.findByUrl(url)

    if magnet_from_cache is not None:
      return magnet_from_cache

    try:
      html = get_page(url)
    except:
      print(' - Notice: URL or something failed, skipping...')
      continue

    if not html:
      continue

    magnet = magnet.update_from_url_content(url=url, content=html)
    if not magnet.has_links():
      continue

    repository.save(magnet)
    
  return magnet