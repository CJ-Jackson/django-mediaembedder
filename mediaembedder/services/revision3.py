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
    return self.render('revision3.html', {'id': id, 'width': width, 'height': height})

services.append({
        're': '^http(s?)://(.*)revision3.com/(?P<revision3_group>[a-zA-Z0-9-_]+)/(?P<revision3_name>[a-zA-Z0-9-_]+)(/?)',
        'func': revision3,
    })

def revision3_broadcast(self):
    if 'id' not in self.data:
        if not self.mainTree:
            self.buildMainTree()
        import re
        prog = re.compile('^(.*)http://revision3.com/html5player-s(?P<id>\d+)')
        for textarea in self.mainTree.iter('textarea'):
            match = prog.match(textarea.text)
            if match:
                self.data['id'] = match.group('id')
                self.saveData()
                break
    id = self.data['id']
    width = 640
    height = 360
    if self.width:
        width = self.width
    if self.height:
        height = self.height
    return self.render('revision3_broadcast.html', {'id': id, 'width': width, 'height': height})

services.append({
        're': '^http(s?)://(.*)revision3.com/(?P<revision3_group>[a-zA-Z0-9-_]+)(/?)',
        'func': revision3_broadcast,
    })
