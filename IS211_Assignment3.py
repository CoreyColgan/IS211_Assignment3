#!/usr/bin/env python
# coding: utf-8
# IS211_Assignment 3
# Fall 2019

import argparse
import csv
import re
import urllib.request

# Part 1
# download the web log file from the location provided by a url parameter.

def download_csv(url):
    url, headers = urllib.request.urlretrieve(url)
    csv = open(url)
    return csv


# Part 2
#The file should then be processed, using the CSV module

def process_csv(localfile):
    csvlist = []
    csvreader = csv.reader(localfile, delimiter=',')

    for row in csvreader:
        csvlist.append(row)
    return csvlist

# Part 3
# After processing the file, your next task will be to search for all hits that are for an image file. To check if a 
#hitis for an image file or not, we will simply check that the file extension is either .jpg, .gif or .png.

def search_image(csvlist):
    imageCounter = 0

    for row in csvlist:
        if re.search(r'\.(gif|GIF|jpg|JPG|jpeg|png|PNG)', row[0]):
            imageCounter += 1
    percentage = (imageCounter/(len(csvlist)))*100

    return len(csvlist), imageCounter, percentage

# Part 4
#Once Part III is done, your program should find out which browser people are using is the most popular
def search_agent(csvlist):
    
    chromeCounter = 0
    firefoxCounter = 0
    ieCounter = 0
    safariCounter = 0
    
    for row in csvlist:
        if re.search(r'Chrome', row[2]):
            chromeCounter += 1
        elif re.search(r'Firefox', row[2]):
            firefoxCounter += 1
        elif re.search(r'MSIE', row[2]):
            ieCounter += 1
        else:
            safariCounter += 1
            
    return chromeCounter, firefoxCounter, ieCounter, safariCounter

# main function to run script
def main():
    url = 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'
    
    csv_file = download_csv(url)
    csv_list = process_csv(csv_file)
    image_stats = search_image(csv_list)
    browser_stats = search_agent(csv_list)
    
    if max(browser_stats) == browser_stats[0]:
           maxbrowser = 'Chrome'
    elif max(browser_stats) == browser_stats[1]:
           maxbrowser = 'Firefox'
    elif max(browser_stats) == browser_stats[2]:
           maxbrowser = 'IE'
    elif max(browser_stats) == browser_stats[3]:
           maxbrowser = 'Safari'

    print(f'Out of {image_stats[0]} requests, {image_stats[1]} were image requests.\n'
          f'This accounts for {image_stats[2]}% of all requests \n')
    print (f'Statistics for each browser: \n'
           f'Chrome {browser_stats[0]} \n'
           f'Firefox {browser_stats[1]} \n'
           f'IE {browser_stats[2]} \n'
           f'Safari {browser_stats[3]} \n'
           f'The most popular browser used is: {maxbrowser}')

if __name__ == '__main__':

    main()
