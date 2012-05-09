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
    width = 640
    height = 360
    if self.width:
        width = self.width
    if self.height:
        height = self.height
    return self.render('bliptv.html', {
        'id': id, 'width': width, 'height': height
    })

services.append({
        're': '^http://(.*)blip.tv/(?P<bliptv_group>[^/]+)/(?P<bliptv_title>[a-zA-Z0-9-_]+)-(?P<bliptv_id>\d+)',
        'func': bliptv
    })
