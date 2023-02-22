from bs4 import BeautifulSoup
import requests

def getValidColor(fgColor,bgColor):
  url = f'https://app.contrast-finder.org/result.html?foreground=%23{fgColor[1:]}&background=%23{bgColor[1:]}&ratio=4.5&isBackgroundTested=false&algo=Rgb&lang=en'

  # Send a GET request to the website
  response = requests.get(url)
  

  soup = BeautifulSoup(response.content, 'html.parser')

  div_with_id = soup.find("table", id="contrast-solution")

  if div_with_id==None:
    return {"color":fgColor,"background-color":bgColor}

  #foreground color
  div_with_class=div_with_id.find("td",class_="col01")
  li_with_hexa=div_with_class.find("li",class_="color-value-hexa")
  foreground_color=li_with_hexa.contents

  #background color
  div_with_class=div_with_id.find("td",class_="col02")
  li_with_hexa=div_with_class.find("li",class_="color-value-hexa")
  background_color=li_with_hexa.contents

  return {"color":foreground_color[0],"background-color":background_color[0]}