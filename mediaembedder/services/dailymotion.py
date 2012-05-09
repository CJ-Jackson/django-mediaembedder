services = []

def dailymotion(self):
    id = self.match.group('dailymotion_id')
    width = 560
    height = 315
    if self.width:
        width = self.width
    if self.height:
        height = self.height
    return self.render('dailymotion.html', {'id': id, 'width': width, 'height': height})

services.append({
        're': '^http://(.*).dailymotion.com(.*)/video/(?P<dailymotion_id>[a-z0-9]+)_(?P<dailymotion_title>[a-zA-Z0-9-_]+)',
        'func': dailymotion
    })
