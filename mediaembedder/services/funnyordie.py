services = []

def funnyordie(self):
    id = self.match.group('funnyordie_id')
    width = 640
    height = 400
    if self.width:
        width = self.width
    if self.height:
        height = self.height
    return self.render('funnyordie.html', {'id': id, 'width': width, 'height': height})

services.append({
        're': '^http://(www\.)funnyordie.com/videos/(?P<funnyordie_id>[a-z0-9]+)/(?P<funnyordie_title>[a-zA-Z0-9_-]+)',
        'func': funnyordie
    })



