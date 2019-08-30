#!/usr/bin/env python3

import re
import sys
import json
import os
from urllib import request

scriptPath = os.path.dirname(os.path.realpath(__file__))

#GET request to get JSON site
def getRequest(url):
    with request.urlopen(url) as answer:
        return json.loads(answer.read())


# get all /b/ webm or mp4 threads
def getWebmThreads():
    catalog = {}
    catalog = getRequest('https://2ch.hk/b/catalog.json')
    threads = catalog['threads']
    webmThreads = [val for val in threads if re.search("([цшw][уэe][ибb][ьмm]|[мm][пp]4)", val['subject'], re.I) != None]

    return webmThreads


# print all threads
def printThreads(threads):
    for num, thread in enumerate(threads):
        print("=============== THREAD #", num, " ===============", sep="")
        print("files count: ", thread['files_count'])
        print("subject: ", thread['subject'])
        print("\n")


# read input number of thread to download
def readThreadNum(min, max):
    try:
        num = int(input("Choose your thread (print a number):"))
        while(num < min or num > max):
            num = int(input("Wrong number, try again:"))
        return num
    except ValueError:
        print("It's not a number")
        sys.exit(-1)


# download webm thread and parse it files
def dowloadThread(link):
    posts = getRequest(link)['threads'][0]['posts']
    files = []
    for post in posts:
        for file in post['files']:
            fileName =file['name']
            if(fileName[-3:] == 'mp4' or fileName[-4:] == 'webm'):
                files.append({"name": file['fullname'], "path": file['path'], "duration": file['duration_secs']})

    return files


def generateJsonPlaylist(text):
    with open(scriptPath + "/../temp_playlist.json", 'w', encoding='utf-8') as file:
        json.dump(text, file, ensure_ascii=False, indent="\t")

    with open(scriptPath + "/../playlist.m3u", 'w', encoding='utf-8') as file:
        for item in text:
            file.write("#EXTINF:" + str(item['duration']) +", " + item['name'] + "\n")
            file.write("https://2ch.hk" + item['path'] + "\n\n")


if __name__ == '__main__':
    threads = getWebmThreads()
    printThreads(threads)
    num = readThreadNum(0, len(threads) - 1)
    threadLink = "https://2ch.hk/b/res/" + threads[num]['num'] + ".json"
    files = dowloadThread(threadLink)
    generateJsonPlaylist(files)
