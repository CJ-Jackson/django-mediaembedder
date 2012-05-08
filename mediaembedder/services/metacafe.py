services = []

def metacafe(self):
    id = self.match.group('metacafe_id')
    title = self.match.group('metacafe_title')
    if self.width:
        width = self.width
    else:
        width = 640
    if self.height:
        height = self.height
    else:
        height = 360
    return self.render('metacafe.html', {'id': id, 'title': title, 'width': width, 'height': height})

services.append({
        're': '^http://www.metacafe.com/(w|watch)/(?P<metacafe_id>\d+)/(?P<metacafe_title>[a-zA-Z0-9-_]+)',
        'func': metacafe
    })
