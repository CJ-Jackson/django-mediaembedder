services = []

def thebreak(self):
    id = self.match.group('break_id')
    width = 640
    height = 360
    if self.width:
        width = self.width
    elif 'embed_video_width' in self.data['meta']:
        width = int(self.data['meta']['embed_video_width'])
    if self.height:
        height = self.height
    elif 'embed_video_height' in self.data['meta']:
        height = int(self.data['meta']['embed_video_height'])
    return self.render('break.html', {
        'id': id, 'width': width, 'height': height
    })

services.append({
        're': '^http://www.break.com/(.*)-(?P<break_id>\d+)',
        'func': thebreak
    })
