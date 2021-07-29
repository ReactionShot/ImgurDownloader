#!/usr/bin/env python3

import os
import requests
import wget

album_id = input('Enter Imgur Album ID/Hash: ')
get_album_url = 'https://api.imgur.com/3/album/' + album_id

api_headers = {}
''' .apicreds file format below (single line)
{'Authorization': 'Client-ID ###############'}
'''
with open('.apicreds', 'r') as api_header:
    header_auth = api_header.read().replace('\n', '')
api_headers = eval(header_auth)
api_header.close()

api_response = requests.get(get_album_url, headers=api_headers)
api_response_saved = api_response.json()
api_response.close()

album_title = api_response_saved['data']['title']
if album_title == None:
    album_title = album_id
print(album_title)

# Create Album Folder
if not os.path.exists(album_title):
    os.makedirs(album_title)

# Loop through the API response to get the links and download
images = 0
for links in api_response_saved['data']['images']:
    img_url = api_response_saved['data']['images'][images]['link']
    filename = img_url.split("/")[-1]
    album_directory = os.getcwd() + '\\' + album_title + '\\'
    filepath = album_directory + str(images+1) + ' - ' + filename
    img = wget.download(img_url, filepath)
    images += 1
print("\nFiles downloaded to '" + album_directory + "'")
