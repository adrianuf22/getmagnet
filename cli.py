#!/usr/bin/env python3

import sys

from lib.model.Magnet import Magnet
from lib.model.service.MagnetRepository import MagnetRepository
from lib.model.service.search_handler import search_magnet_links

keyword = sys.argv[1]

print('Searching...')
magnet = search_magnet_links(Magnet.create_empty(keyword))
if not magnet.has_links():
  sys.exit('Magnet links not found! Exiting...')

if magnet.is_new():
  print('Magnet links found from the web!')
  sys.exit(0)

print('Magnet links found from cache!')
