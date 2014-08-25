metrics_tools
=============

These are various python scripts to pull Google analytics or YouTube details for a particular path, tag, or user. These use the APIs from Google Analytics and YouTube Analytics to create PDF or CSV files. 

=============
script: youtube-data-by-channeluser
=============
In addition to the standard Python libraries, the script requires two libraries from Google: 
sudo pip install google-api-python-client
sudo pip install gdata

The Python script youtube-data-by-channeluser.py requires two inputs: channel owner name and number of videos. This script not require login credentials.

The result is a CSV file with a row for each video with the following variables:  
Ranking by popularity	
Video ID	
Video Title	
Date Published	
Category	
Tags	
URL	
Duration in seconds	
Total Views	
Favorite Count	
Rating on 5.0 scale	
Number of Raters	
Number of Comments	
Description	
Content of All Comments

