import json
from lib.model.Magnet import Magnet
from typing import Union
from tinydb import TinyDB, Query

class MagnetRepository:
    storage = None
    storagePath = 'cache.json'

    def __init__(self):
        self.storage = TinyDB(self.storagePath)
    
    def save(self, entity: Magnet):        
        self.storage.insert(entity.to_dict())

    def findByUrl(self, url: str) -> Union[Magnet, None]:
        MagnetQuery = Query()
        document = self.storage.get(MagnetQuery.url == url)

        if document is None:
            return None

        return Magnet.from_dict(document)

    def list(self) -> list:
        return self.storage.all()
