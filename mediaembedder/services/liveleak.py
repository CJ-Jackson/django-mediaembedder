services = []

def liveleak(self):
    if 'id' not in self.data:
        if not self.mainTree:
            self.buildMainTree()
        pattern = '(.*)file_token=(?P<id>[a-z0-9]+)(.*)height: "(?P<height>\d+)"(.*)width: "(?P<width>\d+)"'
        import re
        prog = re.compile(pattern, re.M | re.S)
        for script in self.mainTree.iter('script'):
            match = prog.match(" ".join(script.itertext()))
            if match:
                self.data['id'] = match.group('id')
                self.data['width'] = match.group('width')
                self.data['height'] = match.group('height')
                self.saveData()
                break
    id = self.data['id']
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
    return self.render('liveleak.html', {'id': id, 'width': width, 'height': height})

services.append({
        're': '^http://(www\.)?liveleak.com/view\?(.*)',
        'func': liveleak,
    })
