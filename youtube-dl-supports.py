#!/usr/bin/env python3
# This simple script exits with 0 when passed url is supported by youtube-dl
# And with 1 otherwise
# It opens entire new universe of unlimited possibilities
#
# https://nesterov.cc
import sys
from urllib.parse import urlparse
from youtube_dl.extractor import gen_extractors

url = ' '.join(sys.argv[1:])

try:
    result = urlparse(url)
    if not all([result.scheme, result.netloc, result.path]):
        raise
    ies = gen_extractors()
    for ie in ies:
        if type(ie).__name__ != 'GenericIE' and ie._WORKING != False and ie.suitable(url):
            sys.exit(0)
    raise
except Exception:
    sys.exit(1)

