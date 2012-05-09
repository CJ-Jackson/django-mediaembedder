services = []

def collegehumor(self):
    id = self.match.group('collegehumor_id')
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
    return self.render('collegehumor.html', {
        'id': id, 'width': width, 'height': height
    })

services.append({
        're': '^http(s?)://(?:www\.)?collegehumor.com/video/(?P<collegehumor_id>\d+)/(?P<collegehumor_name>[a-zA-Z0-9-_]+)',
        'func': collegehumor
    })
