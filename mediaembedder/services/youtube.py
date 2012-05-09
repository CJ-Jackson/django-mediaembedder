services = []

def youtube(self):
    id = self.match.group('youtube_id')
    width = 640
    height = 360
    if self.width:
        width = self.width
    elif 'og:video:width' in self.data['meta']:
        width = int(self.data['meta']['og:video:width'])
    if self.height:
        height = self.height
    elif 'og:video:height' in self.data['meta']:
        height = int(self.data['meta']['og:video:height'])
    return self.render('youtube.html', {
        'id': id, 'width': width, 'height': height
    })

services.append({
        're': '^http(s?)://([a-z]*).youtube.com/(watch|index)\?(.*)v=(?P<youtube_id>[a-zA-Z0-9-_]+)',
        'func': youtube,
    })
services.append({
        're': '^http(s?)://([a-z]*).youtube.com/v/(?P<youtube_id>[a-zA-Z0-9-_]+)',
        'func': youtube,
    })
services.append({
        're': '^http(s?)://youtu.be/(?P<youtube_id>[a-zA-Z0-9-_]+)',
        'func': youtube,
    })

def youtube_playlist(self):
    id = self.match.group('youtube_playlist_id')
    width = 640
    height = 368
    if self.width:
        width = self.width
    if self.height:
        height = self.height
    return self.render('youtube_playlist.html', {
        'id': id, 'width': width, 'height': height
    })

services.append({
        're': '^http(s?)://([a-z]*).youtube.com/playlist?(.*)list=(?P<youtube_playlist_id>[a-zA-Z0-9-_]+)',
        'func': youtube_playlist,
    })
