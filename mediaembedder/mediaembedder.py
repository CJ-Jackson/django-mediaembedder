_services = []
_init = False

def __init__():
    global _init
    from . import services
    from os import path
    service_path = path.dirname(services.__file__)
    from glob import glob
    theservices = glob(service_path + '/*.py')
    from importlib import import_module
    for service in theservices:
        service = service.split('/').pop()
        service = service[:-3]
        try:
            module = import_module(services.__name__+ '.' + service)
            for s in module.services:
                __register__(s)
        except:
            lambda x: x
    _init = True

def __register__(service):
    _services.append(service)

def __hash__(url):
    import hashlib
    hash = hashlib.new('ripemd160')
    hash.update(url)
    return hash.hexdigest()

def parse(kwargs):
    global _init
    try:
        url = kwargs['url']
    except:
        return False
    hash = __hash__(url)
    cache_hash = 'mediaembedder_' + hash
    object = False
    from django.core.cache import cache
    if cache.get(cache_hash):
        object = cache.get(cache_hash)
    else:
        if not _init:
            __init__()
        import re
        for service in _services:
            match = re.match(service['re'], url, re.I)
            if match:
                object = media(service['func'], hash, url, match)
                break
    if not object:
        return '<a href="%s">%s</a>' % (str(url), str(url))
    try:
        object.width = int(kwargs['width'])
    except:
        lambda x: x
    try:
        object.height = int(kwargs['height'])
    except:
        lambda x: x
    value = object.execute()
    if not cache.get(cache_hash):
        cache.set(cache_hash, object, 3600)
    return value


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
            import json
            self.data = json.loads(self.dataRecord.data)
        except:
            self.dataRecord = None
            self.data = {}
            self.gatherMeta()

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

    def gatherMeta(self):
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
        self.saveData()

    def saveData(self):
        import json
        data = json.dumps(self.data)
        if not self.dataRecord:
            from .models import Cache
            self.dataRecord = Cache.objects.create(hash=self.hash, data=data)
        else:
            self.dataRecord.data = data
            self.dataRecord.save()

    def render(self, template, map={}):
        from django.template import Context, loader
        template = 'mediaembedder/' + template
        template = loader.get_template(template)
        context = Context(map)
        return template.render(context)

    def execute(self):
        value = self.service(self)
        # Make it Django Cache Framework Friendly
        self.mainTree = None
        self.width = None
        self.height = None
        return value
