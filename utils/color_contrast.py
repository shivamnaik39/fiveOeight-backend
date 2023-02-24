from bs4 import BeautifulSoup
import urllib.request

def checkEmpty(soup):
    return soup.find("div",class_="h2-on-empty-result")

def getNewColor(div_with_id):
    div_with_class=div_with_id.find("td",class_="col01")
    li_with_hexa=div_with_class.find("li",class_="color-value-hexa")
    foreground_color=li_with_hexa.contents

    #background color
    div_with_class=div_with_id.find("td",class_="col02")
    li_with_hexa=div_with_class.find("li",class_="color-value-hexa")
    background_color=li_with_hexa.contents

    return {"color":foreground_color[0],"background-color":background_color[0]}

def makeRequest(fgColor,bgColor,isBg):
    url = f'https://app.contrast-finder.org/result.html?foreground=%23{fgColor[1:]}&background=%23{bgColor[1:]}&ratio=4.5&isBackgroundTested={isBg}&algo=Rgb&lang=en'
    # response = urllib.request.urlretrieve(url)
    # Fetch the HTML content of the webpage
    html_content = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup


def getValidColor(fgColor,bgColor):
  

  # Send a GET request to the website
  soup=makeRequest(fgColor,bgColor,"false")
  
  fCheck=checkEmpty(soup)
  
  if fCheck!=None:
    soup=makeRequest(fgColor,bgColor,"true")
    bCheck=checkEmpty(soup)
    if bCheck!=None :
       return {"color":fgColor,"background-color":bgColor}
    else:
      div_with_id=soup.find("table",id="contrast-solution")
      return getNewColor(div_with_id)
  else:
    if soup.find("table",id="contrast-solution")==None:
      return {"color":fgColor,"background-color":bgColor}
    else:
      div_with_id=soup.find("table",id="contrast-solution")
      return getNewColor(div_with_id)
           