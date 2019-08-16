#!/usr/bin/env python3

import json

class ListCreator:
    def __init__(self):
        self.list="\t<ul id=\"playlist\">\n\t"

    def parseJSON(self, json):
        self.list+="\t<li src=\"https://2ch.hk" + json['path'] + "\">" + json['name'] + "</li>\n\t"

    def getList(self):
        tempList = self.list + "</ul>\n"
        return tempList


def appendLine(fileName, afterLine, targetText):
    file = open(fileName, 'r')
    text = file.readlines()
    for it, line in enumerate(text):
        if(line.find(afterLine) != -1):
            text[it] += "\n" + targetText + "\n"
            break

    file.close()
    file = open("index.html", 'w')
    file.writelines(text)

if __name__ == '__main__':
    with open("../temp_playlist.json", 'r') as file:
        listCreator = ListCreator()
        json.load(file, object_hook=listCreator.parseJSON)

    # print("output list:")
    # print(listCreator.getList())
    appendLine("template.html", "playlistContainer", listCreator.getList())
