import bs4
import requests


response = requests.get("https://en.wikipedia.org/wiki/List_of_algorithms")

if response is not None:
    html = bs4.BeautifulSoup(response.text, 'html.parser')

    title = html.select("#firstHeading")[0].text
    paragraphs = html.select("p")
    for para in paragraphs:
        print (para.text)

    # just grab the text up to contents as stated in question
    intro = '\n'.join([ para.text for para in paragraphs[0:5]])
    print (intro)