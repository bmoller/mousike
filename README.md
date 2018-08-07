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
| [createPlaylist](http://www.subsonic.org/pages/api.jsp#createPlaylist) | | | | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • |
| [deletePlaylist](http://www.subsonic.org/pages/api.jsp#deletePlaylist) | | | | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • |
| [download](http://www.subsonic.org/pages/api.jsp#download) | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • |
| [getAlbum](http://www.subsonic.org/pages/api.jsp#getAlbum) | | | | | | | | | | • | • | • | • | • | • | • | • | • |
| [getAlbumInfo](http://www.subsonic.org/pages/api.jsp#getAlbumInfo) | | | | | | | | | | | | | | | | • | • | • |
| [getAlbumInfo2](http://www.subsonic.org/pages/api.jsp#getAlbumInfo2) | | | | | | | | | | | | | | | | • | • | • |
| [getAlbumList](http://www.subsonic.org/pages/api.jsp#getAlbumList) | | | | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • |
| [getAlbumList2](http://www.subsonic.org/pages/api.jsp#getAlbumList2) | | | | | | | | | | • | • | • | • | • | • | • | • | • |
| [getArtist](http://www.subsonic.org/pages/api.jsp#getArtist) | | | | | | | | | | • | • | • | • | • | • | • | • | • |
| [getArtistInfo](http://www.subsonic.org/pages/api.jsp#getArtistInfo) | | | | | | | | | | | | | • | • | • | • | • | • |
| [getArtistInfo2](http://www.subsonic.org/pages/api.jsp#getArtistInfo2) | | | | | | | | | | | | | • | • | • | • | • | • |
| [getArtists](http://www.subsonic.org/pages/api.jsp#getArtists) | | | | | | | | | | • | • | • | • | • | • | • | • | • |
| [getAvatar](http://www.subsonic.org/pages/api.jsp#getAvatar) | | | | | | | | | | • | • | • | • | • | • | • | • | • |
| [getCaptions](http://www.subsonic.org/pages/api.jsp#getCaptions) | | | | | | | | | | | | | | | | • | • | • |
| [getCoverArt](http://www.subsonic.org/pages/api.jsp#getCoverArt) | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • |
| [getGenres](http://www.subsonic.org/pages/api.jsp#getGenres) | | | | | | | | | | | • | • | • | • | • | • | • | • |
| [getIndexes](http://www.subsonic.org/pages/api.jsp#getIndexes) | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • |
| [getLicense](http://www.subsonic.org/pages/api.jsp#getLicense) | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • |
| [getLyrics](http://www.subsonic.org/pages/api.jsp#getLyrics) | | | | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • |
| [getMusicDirectory](http://www.subsonic.org/pages/api.jsp#getMusicDirectory) | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • |
| [getMusicFolders](http://www.subsonic.org/pages/api.jsp#getMusicFolders) | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • |
| [getNowPlaying](http://www.subsonic.org/pages/api.jsp#getNowPlaying) | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • |
| [getPlaylist](http://www.subsonic.org/pages/api.jsp#getPlaylist) | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • |
| [getPlaylists](http://www.subsonic.org/pages/api.jsp#getPlaylists) | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • |
| [getRandomSongs](http://www.subsonic.org/pages/api.jsp#getRandomSongs) | | | | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • |
| [getSimilarSongs](http://www.subsonic.org/pages/api.jsp#getSimilarSongs) | | | | | | | | | | | | | • | • | • | • | • | • |
| [getSimilarSongs2](http://www.subsonic.org/pages/api.jsp#getSimilarSongs2) | | | | | | | | | | | | | • | • | • | • | • | • |
| [getSong](http://www.subsonic.org/pages/api.jsp#getSong) | | | | | | | | | | • | • | • | • | • | • | • | • | • |
| [getSongsByGenre](http://www.subsonic.org/pages/api.jsp#getSongsByGenre) | | | | | | | | | | | • | • | • | • | • | • | • | • |
| [getStarred](http://www.subsonic.org/pages/api.jsp#getStarred) | | | | | | | | | | • | • | • | • | • | • | • | • | • |
| [getStarred2](http://www.subsonic.org/pages/api.jsp#getStarred2) | | | | | | | | | | • | • | • | • | • | • | • | • | • |
| [getTopSongs](http://www.subsonic.org/pages/api.jsp#getTopSongs) | | | | | | | | | | | | | | | • | • | • | • |
| [getVideoInfo](http://www.subsonic.org/pages/api.jsp#getVideoInfo) | | | | | | | | | | | | | | | | • | • | • |
| [getVideos](http://www.subsonic.org/pages/api.jsp#getVideos) | | | | | | | | | | • | • | • | • | • | • | • | • | • |
| [hls](http://www.subsonic.org/pages/api.jsp#hls) | | | | | | | | | | • | • | • | • | • | • | • | • | • |
| [ping](http://www.subsonic.org/pages/api.jsp#ping) | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • |
| [scrobble](http://www.subsonic.org/pages/api.jsp#scrobble) | | | | | | | • | • | • | • | • | • | • | • | • | • | • | • |
| [search](http://www.subsonic.org/pages/api.jsp#search) | • | • | • | • | • | | | | | | | | | | | | | |
| [search2](http://www.subsonic.org/pages/api.jsp#search2) | | | | | | • | • | • | • | • | • | • | • | • | • | • | • | • |
| [search3](http://www.subsonic.org/pages/api.jsp#search3) | | | | | | | | | | • | • | • | • | • | • | • | • | • |
| [setRating](http://www.subsonic.org/pages/api.jsp#setRating) | | | | | | | | • | • | • | • | • | • | • | • | • | • | • |
| [star](http://www.subsonic.org/pages/api.jsp#star) | | | | | | | | | | • | • | • | • | • | • | • | • | • |
| [stream](http://www.subsonic.org/pages/api.jsp#stream) | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • | • |
| [unstar](http://www.subsonic.org/pages/api.jsp#unstar) | | | | | | | | | | • | • | • | • | • | • | • | • | • |
| [updatePlaylist](http://www.subsonic.org/pages/api.jsp#updatePlaylist) | | | | | | | | | | • | • | • | • | • | • | • | • | • |
