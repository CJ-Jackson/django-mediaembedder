services = []

def sciencestage(self):
    id = self.match.group('sciencestage_id')
    title = self.match.group('sciencestage_title')
    if 'image' not in self.data:
        if not self.mainTree:
            self.buildMainTree()
        pattern = '(.*)width="(?P<width>\d+)"(.*)height="(?P<height>\d+)"(.*)file=(?P<file>.+)&image=(?P<image>.+)&width'
        import re
        prog = re.compile(pattern, re.M | re.S)
        for theinput in self.mainTree.iter('input'):
            if theinput.get('name', 'noname') == 'embedded':
                match = prog.match(theinput.get('value'))
                if match:
                    self.data['image'] = match.group('image')
                    self.data['file'] = match.group('file')
                    self.data['width'] = match.group('width')
                    self.data['height'] = match.group('height')
                    self.saveData()
                    break
    image = self.data['image']
    file = self.data['file']
    width = 640
    height = 360
    if self.width:
        width = self.width
    elif 'width' in self.data:
        width = self.data['width']
    if self.height:
        height = self.height
    elif 'height' in  self.data:
        height = self.data['height']
    return self.render('sciencestage.html', {'id': id, 'width': width, 'height': height, 'image': image, 'title': title, 'file': file})

services.append({
        're': '^http://(www\.)?sciencestage.com/v/(?P<sciencestage_id>\d+)/(?P<sciencestage_title>.+)(\.html)?',
        'func': sciencestage
    })

def sciencestage_audio(self):
    id = self.match.group('sciencestage_id')
    title = self.match.group('sciencestage_title')
    if 'file' not in self.data:
        if not self.mainTree:
            self.buildMainTree()
        pattern = '(.*)width="(?P<width>\d+)"(.*)height="(?P<height>\d+)"(.*)file=(?P<file>.+)&width'
        import re
        prog = re.compile(pattern, re.M | re.S)
        for theinput in self.mainTree.iter('input'):
            if theinput.get('name', 'noname') == 'embedded':
                match = prog.match(theinput.get('value'))
                if match:
                    self.data['file'] = match.group('file')
                    self.data['width'] = match.group('width')
                    self.data['height'] = match.group('height')
                    self.saveData()
                    break
    file = self.data['file']
    width = 590
    height = 220
    if self.width:
        width = self.width
    elif 'width' in self.data:
        width = self.data['width']
    if self.height:
        height = self.height
    elif 'height' in  self.data:
        height = self.data['height']
    return self.render('sciencestage_audio.html', {'id': id, 'width': width, 'height': height, 'title': title, 'file': file})

services.append({
        're': '^http://(www\.)?sciencestage.com/a/(?P<sciencestage_id>\d+)/(?P<sciencestage_title>.+)(\.html)?',
        'func': sciencestage_audio
    })
