metrics_tools
=============

These are various python scripts to pull Google analytics or YouTube details for a particular path, tag, or user. These use the APIs from Google Analytics and YouTube Analytics to create PDF or CSV files. 


## requirements

#### CSV scripts
In addition to the standard Python libraries, these scripts require two libraries from Google APIs: 
sudo pip install google-api-python-client
sudo pip install gdata

#### pdf scripts
In order to use the PDF creation functionality, there are further requirements.

For Python dependencies, you must install (``` pip install ``` in a virtual environment, ```sudo pip install ``` otherwise):

- matplotlib
- numpy
- apiclient
- oauth2client
- httplib2
- requests
- BeautifulSoup4

You also need a Google account with read access to the Google Analytics profile you are interested in.

##openmichigan-metrics-pdf

###use

In order to use the PDF functionality, in the ``` openmichian-metrics-pdf ``` folder, you need to fill in the files ``` client_secrets_blank.json ``` and ``` infofile_blank.py ``` with the appropriate information, and save them respectively as ``` client_secrets.json ``` and ``` infofile.py ```. These each provide necessary, but private to account holder(s), specific information.

In ``` client_secrets.json ```, you must fill in this structure:

```
{
  "installed": {
    "client_id": "[longstringofcharacters].apps.googleusercontent.com",
    "client_secret": "stringoflettersandnumbers",
    "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob","http://localhost"],
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://accounts.google.com/o/oauth2/token"
  }
}
```

You can find your ``` client_id ``` and your ``` client_secret ``` for your Google account, and learn more about what this means, by going to [this page](https://developers.google.com/api-client-library/python/guide/aaa_client_secrets).

In ``` infofile.py ```, you need to fill in

```
profileid = ""
pgpath = ""
```

with relevant information. The ``` profileid ``` string should contain the Google Analytics profile id that you're interested in, which you can find at [this page](). The ``` pgpath ``` string variable should contain a path to a course or resource you are interested in, if you are using this for Open.Michigan's OERBit instance. (This is specifically configured to work with an instance of the [OERbit platform](), as of August 2014.) For example, this could be

```pgpath = pgpath = "/education/si/si508/fall2008" ```

##results

To run, ``` cd ``` to the ``` openmichigan-metrics-pdf ``` folder. Make sure you have filled in information and installed dependencies as specified above. Then run ```python create_pdf_plots.py ```.

In the process, a few other files will be created: ``` incomplete summary ```, and ``tf_ ``` 1, 2, and 3. Do not worry about these -- you can delete them or ignore them, but they will be overwritten each time you run this process.

In addition, a .PDF file will be saved and created each time you run it with a name such as ``` si_si508_fall2008_YYYY-MM-DD.pdf ```, with the date on which you ran this set of scripts. These will be different every time, and there are your results.


##csv scripts

###script: youtube-data-by-channelowner

The Python script youtube-data-by-channeluser.py requires one argumenr: channel owner name, 
e.g. python youtube-data-by-channelowner.py openmichigan


This script does not require login credentials or an API key because it uses v1 of the YouTube Analytics API. (N.B. The most recent version of the YouTube API is v3, which requires an API key. Likes and dislikes can only be retrieved by v3.)

The result is a CSV (spreadsheet) file with a row for each video with the following variables:  
Ranking by popularity, Video ID, Video Title, Date Published, Category, URL, Duration in seconds, Total Views, Rating on 5.0 scale (Historical), Number of Raters (Historical), Number of Comments, Description, Content of All Comments
