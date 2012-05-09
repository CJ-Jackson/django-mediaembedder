services = []

def metacafe(self):
    id = self.match.group('metacafe_id')
    title = self.match.group('metacafe_title')
    width = 640
    height = 360
    if self.width:
        width = self.width
    if self.height:
        height = self.height
    return self.render('metacafe.html', {'id': id, 'title': title, 'width': width, 'height': height})

services.append({
        're': '^http://www.metacafe.com/(w|watch)/(?P<metacafe_id>\d+)/(?P<metacafe_title>[a-zA-Z0-9-_]+)',
        'func': metacafe
    })
