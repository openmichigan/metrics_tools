#!/usr/bin/env python

#################################################################
# Prerequisites:
# - download python: http://www.python.org/download/
# - run setup for python (see README or INSTALL text file from above)
# set system path for Python (System Information > Advance Settings > Environment Variables > Path)
# - do: sudo pip install google-api-python-client
# - do: sudo pip install gdata
# - cd into this folder to run the script: python utube-data-healthoernetwork.py
#
# THE ONLY CHANGE TWO CHANGES YOU NEED TO MAKE IN SCRIPT IS USERNAME AND NUM VIDEOS
####################################################################

import gdata.youtube
import gdata.youtube.data
import gdata.youtube.client
import gdata.youtube.service
import getpass
import csv
import re
import datetime
import argparse
import sys
import json

def PrintEntryDetailsToTerminal(index, entry_id, title, date, category, url, duration, views, likes, dislikes, rating, raters, num_comments, desc, comment_thread):
	print 'Video Index: %s' % index
	print 'Video ID: %s' % entry_id
	print 'Video title: %s' % title
	print 'Video published on: %s ' % date
	print 'Video category: %s' % category
	print 'Video watch page: %s' % url
	print 'Video duration: %s' % duration
	print 'Video view count: %s' % views
	print 'Video like count: %s' % likes
	print 'Video dislike count: %s' % dislikes
	print 'Video rating (historical): %s' % rating
	print 'Video number of raters (historical): %s' % raters
	print 'Video number of comments: %s' % num_comments
	print 'Video description: %s' % desc
	print 'Video comments: %s' % comment_thread
	print
	print

def PrintEntryDetailsToFile(file, index, entry_id, title, date, category, url, duration, views, likes, dislikes, rating, raters, num_comments, desc, comment_thread):
	file.writerow([index, entry_id, title, date, category, url, duration, views, likes, dislikes, rating, raters, num_comments,desc,comment_thread,' '])


def GetEntryDetails(entry, idx, file, yt_service):
	
	index = str(idx)
	entry_id = str(re.split('http://gdata.youtube.com/feeds/api/videos/', entry.id.text)[1])
	date = str(entry.published.text)[:10]
	title = ''
	category = ''
	tags = ''
	url = ''
	duration = '0'
	views = '0'
	likes = ''
	dislikes = ''	
	rating = '0'
	raters = '0'
	num_comments=''
	desc = ''
	comment_thread = ''
	
	if entry.media:
		title = '\"' + str(entry.media.title.text) + '\"'
	  	category = '\"' + str(entry.media.category[0].text) + '\"'
	  	url = entry.media.player.url
	  	duration = str(entry.media.duration.seconds)
	  	desc = str(entry.media.description.text)

	if entry.statistics:
		views = entry.statistics.view_count
	
	if entry.rating:
		rating = entry.rating.average
		raters = entry.rating.num_raters
		
	if entry.comments:
		if entry.comments.feed_link:
			num_comments = entry.comments.feed_link[0].count_hint
			if num_comments > 0:
				comment_feed = yt_service.GetYouTubeVideoCommentFeed(video_id=entry_id)
				for comment_entry in comment_feed.entry:
					comment_date = str(comment_entry.updated.text)[:10]
					comment_thread += str(comment_entry.author[0].name.text) + ' (' + comment_date +') ' + str(comment_entry.content.text) + ';\n\n'
	
	entry_id = '\"' + entry_id + '\"'
	PrintEntryDetailsToFile(file, index, entry_id, title, date, category, url, duration, views, likes, dislikes, rating, raters, num_comments, desc, comment_thread)
	PrintEntryDetailsToTerminal(index, entry_id, title, date, category, url, duration, views, likes, dislikes, rating, raters, num_comments, desc, comment_thread)


def GetAndPrintVideoFeed(uri, idx, file):
    yt_service = gdata.youtube.service.YouTubeService()
    yt_service.ssl = True
    feed = yt_service.GetYouTubeVideoFeed(uri)
    for entry in feed.entry:
        GetEntryDetails(entry,idx,file, yt_service)
        idx += 1
        
def GetAndPrintVideoNumberFeed(uri):
    yt_service = gdata.youtube.service.YouTubeService()
    yt_service.ssl = True
    feed = yt_service.GetYouTubeVideoFeed(uri)
    totalvids = 0
    totalvids = int(feed.total_results.text)
    return totalvids
    
if __name__ == '__main__':

	username = ""
	numvideos = 0
	# access accounts to be used and save in AmaraAccount instances
	if len(sys.argv) != 2:
		print "youtube channel username required. You may only include 1 username, e.g. python youtube-data-by-channelowner.py openmichigan"	
	else:
		username = sys.argv[1]
		print "username " + username
	
		#Get total number videos on channel
		baseurinum = "http://gdata.youtube.com/feeds/api/users/" + username  + '/uploads?max-results=0'
		numvideos = GetAndPrintVideoNumberFeed(baseurinum)
		print 'numvideos: ' + str(numvideos) + '\n\n\n'
		
		now = datetime.datetime.now()
		mon = 0
		date = 0
		if now.month >= 10:
			mon = str(now.month)
		else:
			mon = '0' +str(now.month)
		if now.day >=10:
			date = str(now.day)
		else:
			date = '0' + str(now.day)
	
		filename = '' + str(now.year) + '_' + mon + '_' + date + ' -' + username + '-YouTube-Videos.csv'
		fileWriter = csv.writer(open(filename, 'wb'), dialect='excel', quoting=csv.QUOTE_MINIMAL)
		fileWriter.writerow(['Index', 'Video ID', 'Video Title', 'Date Published', 'Category', 'URL', 'Duration', 'Views', 'Likes', 'Dislikes', 'Rating (Historical)', 'Raters (Historical)', '# Comments', 'Description', 'Comment Thread'])
		index = 1

		baseuri = 'http://gdata.youtube.com/feeds/api/users/' + username + '/uploads?maxresults=25'

		print 'base uri: ' + str(baseuri) + '\n'

		GetAndPrintVideoFeed(baseuri,index, fileWriter)
		uri = baseuri
		
		while numvideos >= index:
			index +=25
			uri = baseuri + '&start-index=' + str(index)
			GetAndPrintVideoFeed(uri, index, fileWriter)

	