# operation-khakis


###New Stuff:
#####PySpotify

https://pyspotify.mopidy.com/en/latest/








[Spotify Commands Source](https://community.spotify.com/t5/Help-Desktop-Linux-Mac-and/Commands-to-play-songs-and-playlists-from-terminal/td-p/802287/page/2)

	osascript -e 'tell application "spotify" to play'
	
	
	
What is osascript?

http://www.hackmac.org/tutorials/run-applescript-from-the-command-line/
	
###GOT Spotify 0.6xx on my PowerBook G4

###Calcs	

	fee_yearly = 30.
	months = 12.
	days_in_year = 365.
	pay_per_play = 0.001 #dollas $$$$ cha-ching
	count_songs = 5.
	avg_song_length = ((2.+59./60.)+(3.+51./60.)+(3.+4./60.)+(4.+44./60.)+(4.+27./60.))/count_songs
	hours_in_day = 24.
	mins_in_hour = 60. 
	mins_in_day = hours_in_day * mins_in_hour
	song_plays_per_day = mins_in_day/avg_song_length
	profit_per_day = song_plays_per_day * pay_per_play
	profit_per_year = days_in_year * profit_per_day
	net_per_year = profit_per_year - fee_yearly

	print 'We can play ' + str(song_plays_per_day) + ' songs per day (with 1 spotify user) - assumption is that user\'s membership is free and we optimize so it plays always.'
	print 'Which yields a daily profit of $' + str(profit_per_day) 
	print 'And a yearly profit of $' + str(profit_per_year)
	print 'Netting $'+str(net_per_year)+' per year'
	
###Prints to

	We can play 377.292576419 songs per day (with 1 spotify user) - assumption is that user's membership is free and we optimize so it plays always.
	Which yields a daily profit of $0.377292576419
	And a yearly profit of $137.711790393
	Netting $107.711790393 per year	
	
http://askubuntu.com/questions/28564/run-simple-bash-script-to-start-applications-at-login

	echo "start spotify"
	gnome-terminal -e spotify --title spotify
	
	


http://mitchfournier.com/2013/03/26/install-command-line-spotify-on-a-headless-raspberry-pi/