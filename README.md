metrics_tools
=============

These are various python scripts to pull Google analytics or YouTube details for a particular path, tag, or user. These use the APIs from Google Analytics and YouTube Analytics to create PDF or CSV files. 

In addition to the standard Python libraries, these scripts requires two libraries from Google APIs: 
sudo pip install google-api-python-client
sudo pip install gdata

=============
script: youtube-data-by-channelowner
=============

The Python script youtube-data-by-channeluser.py requires one input: channel owner name. This script does not require login credentials or an API key.

The result is a CSV (spreadsheet) file with a row for each video with the following variables:  
Ranking by popularity, Video ID, Video Title, Date Published, Category, URL, Duration in seconds, Total Views, Total Likes, Total Dislikes, Rating on 5.0 scale, Number of Raters, Number of Comments, Description, Content of All Comments
