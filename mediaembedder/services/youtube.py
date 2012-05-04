services = []

def youtube(self):
    id = self.match.group('youtube_id')
    if self.width:
        width = self.width
    else:
        try:
            width = int(self.data['meta']['og:video:width'])
        except:
            width = 398

    if self.height:
        height = self.height
    else:
        try:
            height = int(self.data['meta']['og:video:height'])
        except:
            height = 224

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
