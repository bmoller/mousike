Example event with parameters:


{'body': None,
 'headers': {'Accept': '*/*',
             'Host': 'localhost:3000',
             'User-Agent': 'curl/7.60.0',
             'X-Forwarded-Port': '3000',
             'X-Forwarded-Proto': 'http'},
 'httpMethod': 'GET',
 'isBase64Encoded': False,
 'path': '/ping',
 'pathParameters': None,
 'queryStringParameters': {'t': ['askldjflkasdf'],
                           'u': ['bob'],
                           'v': ['aklsdjfl']},
 'requestContext': {'accountId': '123456789012',
                    'apiId': '1234567890',
                    'extendedRequestId': None,
                    'httpMethod': 'GET',
                    'identity': {'accountId': None,
                                 'apiKey': None,
                                 'caller': None,
                                 'cognitoAuthenticationProvider': None,
                                 'cognitoAuthenticationType': None,
                                 'cognitoIdentityPoolId': None,
                                 'sourceIp': '127.0.0.1',
                                 'user': None,
                                 'userAgent': 'Custom User Agent String',
                                 'userArn': None},
                    'path': '/ping',
                    'requestId': 'c6af9ac6-7b61-11e6-9a41-93e8deadbeef',
                    'resourceId': '123456',
                    'resourcePath': '/ping',
                    'stage': 'prod'},
 'resource': '/ping',
 'stageVariables': None}


API matrix:

| Method | 1.0.0 | 1.1.0 | 1.1.1 | 1.2.0 | 1.3.0 | 1.4.0 | 1.5.0 | 1.6.0 | 1.7.0 | 1.8.0 | 1.9.0 | 1.10.2 | 1.11.0 | 1.12.0 | 1.13.0 | 1.14.0 | 1.15.0 | 1.16.0 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [ping](http://www.subsonic.org/pages/api.jsp#ping) | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • |
| [getLicense](http://www.subsonic.org/pages/api.jsp#getLicense) | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • |

Browsing    getMusicFolders getIndexes getMusicDirectory getGenres getArtists getArtist getAlbum getSong getVideos getVideoInfo getArtistInfo getArtistInfo2 getAlbumInfo getAlbumInfo2 getSimilarSongs getSimilarSongs2 getTopSongs
Album/song lists    getAlbumList getAlbumList2 getRandomSongs getSongsByGenre getNowPlaying getStarred getStarred2
Searching   search search2 search3
Playlists   getPlaylists getPlaylist createPlaylist updatePlaylist deletePlaylist
Media retrieval stream download hls getCaptions getCoverArt getLyrics getAvatar
Media annotation    star unstar setRating scrobble
Sharing getShares createShare updateShare deleteShare
Podcast getPodcasts getNewestPodcasts refreshPodcasts createPodcastChannel deletePodcastChannel deletePodcastEpisode downloadPodcastEpisode
Jukebox jukeboxControl
Internet radio  getInternetRadioStations createInternetRadioStation updateInternetRadioStation deleteInternetRadioStation
Chat    getChatMessages addChatMessage
User management getUser getUsers createUser updateUser deleteUser changePassword
Bookmarks   getBookmarks createBookmark deleteBookmark getPlayQueue savePlayQueue
Media library scanning  getScanStatus startScan
