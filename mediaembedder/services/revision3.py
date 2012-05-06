services = []

def revision3(self):
    if 'id' not in self.data:
        pattern = '^http(s?)://(.*)revision3.com/player-v(?P<id>\d+)'
        import re
        match = re.match(pattern, self.data['meta']['og:video'], re.I)
        if match:
            self.data['id'] = match.group('id')
            self.saveData()
    id = self.data['id']
    if self.width:
        width = self.width
    else:
        width = self.data['meta']['og:video:width']
    if self.height:
        height = self.height
    else:
        height = self.data['meta']['og:video:height']
    return self.render('revision3.html', {'id': id, 'width': width, 'height': height})

services.append({
        're': '^http(s?)://(.*)revision3.com/(?P<revision3_group>[a-zA-Z0-9-_]+)/(?P<revision3_name>[a-zA-Z0-9-_]+)(/?)',
        'func': revision3,
    })
