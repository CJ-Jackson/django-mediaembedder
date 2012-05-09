services = []

def gametrailers(self):
    id = self.match.group('gametrailers_id')
    width = 640
    height = 360
    if self.width:
        width = self.width
    if self.height:
        height = self.height
    return self.render('gametrailers.html', {'id': id, 'width': width, 'height': height})

services.append({
        're': '^http://(www\.)?gametrailers.com/video/(?P<gametrailers_title>[a-zA-Z0-9-_]+)/(?P<gametrailers_id>\d+)',
        'func': gametrailers
    })
