services = []

def aniboom(self):
    id = self.match.group('aniboom_id')
    width = 594
    height = 334
    if self.width:
        width = self.width
    if self.height:
        height = self.height
    return self.render('aniboom.html', {'id': id, 'height': height, 'width': width})

services.append({
        're': '^http://(www\.)?aniboom.com/animation-video/(?P<aniboom_id>\d+)/(?P<aniboom_title>.+)(/?)',
        'func': aniboom
    })
