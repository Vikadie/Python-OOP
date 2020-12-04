import requests
import xml.etree.ElementTree as ET

AUTOCOMPLETE_URL = 'http://suggestqueries.google.com/complete/search?&output=toolbar&gl=us&hl=en&q='


class Suggestions:
    def __init__(self, term):
        self.__term = term

    def get_suggestion(self):
        search_term = f"{self.__term}%20vs%20"
        response = requests.get(AUTOCOMPLETE_URL + search_term)
        root = ET.fromstring(response.content)
        for element in root:
            value = element[0].attrib['data']
            yield value


if __name__ == '__main__':
    term = input()
    suggestion = Suggestions(term)
    for suggestion in (suggestion.c):
        print(suggestion)