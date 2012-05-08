services = []

def bliptv(self):
    if 'id' not in self.data:
        pattern = '^http://(.*)blip.tv/play/(?P<id>[a-zA-Z0-9]+)'
        import re
        match = re.match(pattern, self.data['meta']['og:video'], re.I)
        if match:
            self.data['id'] = match.group('id')
            self.saveData()
    id = self.data['id']
    if self.width:
        width = self.width
    else:
        width = 640
    if self.height:
        height = self.height
    else:
        height = 360
    return self.render('bliptv.html', {
        'id': id, 'width': width, 'height': height
    })

services.append({
        're': '^http://(.*)blip.tv/(?P<bliptv_group>[^/]+)/(?P<bliptv_title>[a-zA-Z0-9-]+)-(?P<bliptv_id>\d+)',
        'func': bliptv
    })
