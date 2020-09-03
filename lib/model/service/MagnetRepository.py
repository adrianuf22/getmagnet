import json
from urllib.parse import urlparse, parse_qs, urlunparse, urlencode
from lib.model.Magnet import Magnet
from typing import Union

# @Todo Refactor to use TinyDB: https://pypi.org/project/tinydb/
class MagnetRepository:
    storage = None
    storagePath = 'cache.json'

    def __init__(self):
        with open(self.storagePath, 'r') as jsonFile:
            self.storage = json.load(jsonFile)
    
    def save(self, entity: Magnet):
        url = self._sanitize_url(entity.get_url())
        
        self.storage[url] = entity.to_dict()

        with open(self.storagePath, 'w') as jsonFile:
            json.dump(self.storage, jsonFile)

    def findByUrl(self, raw_url: str) -> Union[Magnet, None]:
        url = self._sanitize_url(raw_url)
        
        if url in self.storage:
            magnet = Magnet.from_dict(self.storage[url])

            if magnet.is_offline:
                return None

            return magnet            

        return None

    def list(self) -> list:
        magnets = []    
        for _, magnet in self.storage.items():
            magnets.append(magnet)

        return magnets

    def _sanitize_url(self, dirty_url) -> str:
        parsedUrl = urlparse(dirty_url)
        queryStrings = parse_qs(parsedUrl.query)
        if 'ved' in queryStrings:
            del queryStrings['ved']

        urlParts = list(parsedUrl)
        urlParts[4] = urlencode(queryStrings)

        return urlunparse(urlParts)    