#!/usr/bin/env python3

import json
import os

scriptPath = os.path.dirname(os.path.realpath(__file__))

class ListCreator:
    def __init__(self):
        self.list="\t<ul id=\"playlist\">\n\t"

    def parseJSON(self, json):
        self.list+="\t<li src=\"https://2ch.hk" + json['path'] + "\">" + json['name'] + "</li>\n\t"

    def getList(self):
        tempList = self.list + "</ul>\n"
        return tempList


def appendLine(fileName, afterLine, targetText):
    file = open(fileName, 'r', encoding='utf-8')
    fileOut = open(scriptPath + "/index.html", 'w', encoding='utf-8')
    text = file.readlines()
    for it, line in enumerate(text):
        if(line.find(afterLine) != -1):
            text[it] += "\n" + targetText + "\n"
            break

    fileOut.writelines(text)

    file.close()
    fileOut.close()

if __name__ == '__main__':
    with open(scriptPath + "/../temp_playlist.json", 'r', encoding='utf-8') as file:
        listCreator = ListCreator()
        json.load(file, object_hook=listCreator.parseJSON)

    # print("output list:")
    # print(listCreator.getList())
    appendLine(scriptPath + "/template.html", "playlistContainer", listCreator.getList())
