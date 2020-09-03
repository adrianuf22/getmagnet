import re
from webpreview import web_preview

class Magnet:
    def __init__(self, keyword: str, url: str = None, links: list = [], title = '', image = '', offline = False, new = False):
        self._keyword = keyword
        self._url = url
        self._title = title
        self._image = image
        self._links = links
        self._offline = offline
        self._new = new

    @classmethod
    def from_dict(cls, raw_magnet: dict) -> 'Magnet':
        return cls(raw_magnet.keyword, raw_magnet.url, raw_magnet.title, raw_magnet.image, raw_magnet.links, raw_magnet.offline)

    @classmethod
    def create_empty(cls, keyword: str) -> 'Magnet':
        return cls(keyword)

    def update_from_url_content(self, url: str, content: str) -> 'Magnet':
        title, _, image = web_preview(url, content=content, parser='lxml')

        self._url = url
        self._title = title
        self._image = image
        self._links = re.findall(r"(magnet:.*?)[\"|\']", content.decode('utf-8'))
        self._new = True

        return self

    def keyword(self) -> str:
        return "torrent %s \"magnet:\"" % self._keyword

    def get_url(self) -> str:
        return self._url

    def is_new(self) -> bool:
        return self._new

    def is_offline(self) -> bool:
        return self._offline == True

    def turn_offline(self):
        self._offline = True

    def has_links(self) -> bool:
        return bool(self._links)

    def to_dict(self) -> dict:
        return {
            'keyword': self._keyword,
            'url': self._url,
            'title': self._title,
            'image': self._image,
            'links': self._links,
            'offline': self._offline
        }
