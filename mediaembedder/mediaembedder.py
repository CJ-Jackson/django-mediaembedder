_services = []
_init = False

def __init__():
    global _init
    from . import services
    for service in dir(services):
        try:
            module = getattr(services, service)
            for s in module.services:
                __register__(s)
        except:
            lambda x: x
    _init = True

def __register__(service):
    _services.add(service)

def __hash__(url):
    import hashlib
    hash = hashlib.new('ripemd160')
    hash.update(url)
    return hash.hexdigest()

def parse(kwargs):
    global _init
    if not _init:
        __init__()
    try:
        url = kwargs['url']
    except:
        return False

    hash = __hash__(url)

    object = False
    import re
    for service in _services:
        match = re.match(service['re'], url, flags=re.I)
        if match:
            object = media(service['func'], hash, url, match)
            break

    if not object:
        return False

    try:
        object.width = int(kwargs['width'])
    except:
        lambda x: x

    try:
        object.height = int(kwargs['height'])
    except:
        lambda x: x

    return object.execute()


class media(object):

    def __init__(self, service, hash, url, match):
        self.service = service
        self.hash = hash
        self.url = url
        self.match = match
        self.mainTree = None
        self.width = None
        self.height = None
        self.setUpData()

    def setUpData(self):
        try:
            from .models import Cache
            self.dataRecord = Cache.objects.get(hash=self.hash)
            import cPickle as pickle
            self.data = pickle.loads(self.dataRecord.data)
        except:
            self.dataRecord = None
            self.data = {}
            self.gatherData()

    def buildMainTree(self):
        self.mainTree = self.getTreeUrl(self.url)

    def getTree(self, string):
        import html5lib
        from html5lib import treebuilders
        from xml.etree import cElementTree
        parser = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("etree", cElementTree), namespaceHTMLElements=False)
        return parser.parse(string)

    def getTreeUrl(self, url):
        import html5lib
        from html5lib import treebuilders
        from xml.etree import cElementTree
        parser = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("etree", cElementTree), namespaceHTMLElements=False)
        from urllib2 import build_opener
        opener = build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0'), ('Accept', '*/*')] # To get round anti-spam system.
        return parser.parse(opener.open(url).read())

    def gatherData(self):
        if not self.mainTree:
            self.buildMainTree()
        meta = {}
        for element in self.mainTree.findall('head/meta'):
            key = element.get('property')
            if key == None:
                key = element.get('name')
            if key != None:
                meta[key] = element.get('content')
        self.data['meta'] = meta
        self.updateDataRecord()

    def updateDataRecord(self):
        import cPickle as pickle
        data = pickle.dumps(self.data, 2)
        if not self.dataRecord:
            from .models import Cache
            self.dataRecord = Cache.objects.create(hash=self.hash, data=data)
        else:
            self.dataRecord.data = data
            self.dataRecord.save()

    def execute(self):
        value = self.service()
        self.mainTree = None
        return value
