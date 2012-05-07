services = []

def collegehumor(self):
    id = self.match.group('collegehumor_id')
    if self.width:
        width = self.width
    else:
        try:
            width = int(self.data['meta']['og:video:width'])
        except:
            width = 640
    if self.height:
        height = self.height
    else:
        try:
            height = int(self.data['meta']['og:video:height'])
        except:
            height = 360
    return self.render('collegehumor.html', {
        'id': id, 'width': width, 'height': height
    })

services.append({
        're': '^http(s?)://(?:www\.)?collegehumor.com/video/(?P<collegehumor_id>\d+)/(?P<collegehumor_name>[a-zA-Z0-9-_]+)',
        'func': collegehumor
    })
