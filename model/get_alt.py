import urllib
import os


def get_alt(src):
    # Use urllib.parse.urlsplit to split the src into components
    # and extract the path component
    path = urllib.parse.urlsplit(src).path

    # Use os.path.basename to extract the file name from the path
    filename = os.path.basename(path)

    return filename
