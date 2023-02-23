import urllib
import os
import alt

def get_alt(src):
    # Use urllib.parse.urlsplit to split the src into components
    # and extract the path component
    path = urllib.parse.urlsplit(src).path

    # Use os.path.basename to extract the file name from the path
    filename = os.path.basename(path)
    print(alt.get_alt_text("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTanH4tQ8qNti33Xnz1OoyKJC_687ROIutEx4CfeRa9og&usqp=CAU&ec=48600112"))
    return filename

