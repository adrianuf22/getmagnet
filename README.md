# getmagnet

Searchs for magnet links using Google search.

---

## Releases

### v0.1.0

- [x] Search torrent on Google (torrent [file name] magnet:)
  - [x] Search magnet links in search results
  - [x] Use Python3 (re, urllib) to request and search regex in html (r"magnet:.*?\"")
- [x] Send magnet link to transmission-daemon

#### Notes

- To search: `search.py` "torrent name"
  All search results are loaded to search 'magnet' URi inside page script, when found, the magnet uri is storage in cache.json file, next searchs will looking for on cache before.

- To add: `add.py` "magnet"
  The magnet uri is sent to transmission-daemon web server via JSONRPC and download is started automatically.

### v0.2.0

- [x] Web API
- [x] Web client

### v0.3.0

- [x] Code refactor

#### Notes
- The domain model was entire rethink, increasing the effort to refactor, some parts was removed and moved to backlog.

## Backlog

- [ ] Add torrent to remote client
- [ ] Configuration file
- [ ] Search for subtitles when not exists
- [ ] Command to list/view magnet links found
- [ ] Show all friendly or allow filter by name
