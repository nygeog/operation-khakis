import time, datetime
import urllib
import webbrowser
from appscript import *


##GOTTA INSTALL appscript https://pypi.python.org/pypi/appscript/
pause = 20 #this is in seconds, change to how long it'll take for the FREE acount playlist to run out.  Every 5 hours is 18000 seconds
#pause = 18000  #5 hours

for i in range(1,5): #change this to the number of times you want the loop to run, + 1, 1,5 runs only 4 times. 
	#theURL = 'http://open.spotify.com/user/nygeog/playlist/3ig96iljYPAV3kbe3WK4ct' #NYGeog latest mix playlst
	#theURL = 'http://open.spotify.com/user/pilotsuits/playlist/6EyyKO72lOydoNMFEVwjct'  #PilotSuits Playlist. 
	#theURL = 'http://open.spotify.com/user/frandukes/playlist/073AS20Rk1IXydWjtH5keD' #The LH2B Playlist
	theURL = 'https://open.spotify.com/user/lh2b/playlist/0H3p1513EtVTjEw0UROtF4' #the vasquez

	# safari = app("Safari")
	# safari.make(new=k.document,with_properties={k.URL:theURL})

	webbrowser.open(theURL)

	print 'Loop '+str(i)+' script started at this time: ' + time.strftime('%c') 
	time.sleep(pause)
