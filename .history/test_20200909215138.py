# import bs4
# import requests


# response = requests.get("https://en.wikipedia.org/wiki/List_of_algorithms")

# if response is not None:
#     html = bs4.BeautifulSoup(response.text, 'html.parser')

#     titles = html.select("h4")
#     print(len(titles))
#     paragraphs = html.select(".mw-headline")
#     for para in paragraphs:
#         if len(para.text)<50:
#             print(para.text)
#             subtitles= para.select("ul>li>a")
#             # print(subtitles.text)
import bs4
import requests
import pprint
from bs4 import BeautifulSoup

# response = requests.get("https://en.wikipedia.org/wiki/List_of_algorithms")

with open('algo_list(1).html', 'r') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')
    for i in range(100):
        if soup.h2!=  None:
            print(soup.h2)
    # print(soup.head)
    print(soup.li)


# if response is not None:
#     html = bs4.BeautifulSoup(response.text, 'html.parser')
#     h2_tags = html.select('h2')

#     algorithm_categories_tags = []

#     for h2 in h2_tags:
#         if len(h2.select('.mw-headline')) > 0 and len(h2.select('.mw-headline')) > 0:
#             algorithm_categories_tags.append(h2)
    
# for i in algorithm_categories_tags:
#     print(i.select("span")[0].text)

# targeted_pages = {'http://m.yp.com/search?search_term=restaurants&search_type=category',
#                   'http://www.yellowpages.com/search?search_terms=Gas+Stations&geo_location_terms=Los+Angeles%2C+CA'
#                   }
# for target in targeted_pages:
#     targeted_page = s.get(target)
#     targeted_soup = BeautifulSoup(targeted_page.content, "lxml")
#     for record in targeted_soup.findAll('div'):
#         print(record.text)
# just grab the text up to contents as stated in question
# intro = '\n'.join([ para.text for para in paragraphs[0:5]])
# print (intro)