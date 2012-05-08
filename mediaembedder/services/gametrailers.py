services = []

def gametrailers(self):
    id = self.match.group('gametrailers_id')
    if self.width:
        width = self.width
    else:
        width = 640
    if self.height:
        height = self.height
    else:
        height = 360
    return self.render('gametrailers.html', {'id': id, 'width': width, 'height': height})

services.append({
        're': '^http://(www\.)?gametrailers.com/video/(?P<gametrailers_title>[a-zA-Z0-9-_]+)/(?P<gametrailers_id>\d+)',
        'func': gametrailers
    })
