# operation-khakis

[Spotify Commands Source](https://community.spotify.com/t5/Help-Desktop-Linux-Mac-and/Commands-to-play-songs-and-playlists-from-terminal/td-p/802287/page/2)

	osascript -e 'tell application "spotify" to play'
	
	
	
What is osascript?

http://www.hackmac.org/tutorials/run-applescript-from-the-command-line/
	
###GOT Spotify 0.6xx on my PowerBook G4

###Calcs	

	fee_yearly = 30.
	months = 12.
	pay_per_play = 0.001 #dollas $$$$ cha-ching
	count_songs = 5.
	avg_song_length = ((2.+59./60.)+(3.+51./60.)+(3.+4./60.)+(4.+44./60.)+(4.+27./60.))/count_songs
	hours_in_day = 24.
	mins_in_hour = 60. 
	mins_in_day = hours_in_day * mins_in_hour
	song_plays_per_day = mins_in_day/avg_song_length
	
	
http://askubuntu.com/questions/28564/run-simple-bash-script-to-start-applications-at-login

	echo "start spotify"
	gnome-terminal -e spotify --title spotify
	
	


http://mitchfournier.com/2013/03/26/install-command-line-spotify-on-a-headless-raspberry-pi/