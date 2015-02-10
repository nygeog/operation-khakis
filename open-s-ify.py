import urllib
#import spotify #install both https://pyspotify.mopidy.com/en/latest/installation/#installing-libspotify    and thedo pyspotify, see the notes at the bottom. 
import webbrowser
from appscript import *

##GOTTA INSTALL appscript https://pypi.python.org/pypi/appscript/

theURL = 'http://open.spotify.com/user/nygeog/playlist/3ig96iljYPAV3kbe3WK4ct'
theURL = 'http://open.spotify.com/user/pilotsuits/playlist/6EyyKO72lOydoNMFEVwjct'

#response = urllib.urlopen(theURL)


safari = app("Safari")
safari.make(new=k.document,with_properties={k.URL:theURL})

# session = spotify.Session()
# audio = spotify.AlsaSink(session)
# loop = spotify.EventLoop(session)
# loop.start()
# track = session.get_track('spotify:track:3N2UhXZI4Gf64Ku3cCjz2g')
# track.load()
# session.player.load(track)
# session.player.play()

#response.open