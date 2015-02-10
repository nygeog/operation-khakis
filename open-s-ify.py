import time, datetime
import urllib
import webbrowser
from appscript import *

##GOTTA INSTALL appscript https://pypi.python.org/pypi/appscript/
pause = 10 #this is in seconds, change to how long it'll take for the FREE acount playlist to run out.  

for i in range(1,5): #change this to the number of times you want the loop to run, + 1, 1,5 runs only 4 times. 
	#theURL = 'http://open.spotify.com/user/nygeog/playlist/3ig96iljYPAV3kbe3WK4ct' #NYgeog playlst
	theURL = 'http://open.spotify.com/user/pilotsuits/playlist/6EyyKO72lOydoNMFEVwjct'  #PilotSuits Playlist. 

	safari = app("Safari")
	safari.make(new=k.document,with_properties={k.URL:theURL})

	print 'Loop '+str(i)+' script started at this time: ' + time.strftime('%c') 
	time.sleep(pause)
