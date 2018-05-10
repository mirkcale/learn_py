#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from xml.parsers.expat import ParserCreate
from urllib import request

class DefaultSaxHandler:
    def startElement(name,attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def endElement(name):
        print('sax:end_element: %s' % name)

    def charData(text):
        print('sax:charData: %s' % text)


def parseXml(xmlStr):
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.startElement
    parser.EndElementHandler = handler.endElement
    parser.CharacterDataHandler = handler.charData
    parser.Parse(xml)
    
if __name__ == '__main__':
    URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

    with request.urlopen(URL, timeout=4) as f:
        data = f.read()

    result = parseXml(data.decode('utf-8'))
    # assert result['city'] == 'Beijing'
