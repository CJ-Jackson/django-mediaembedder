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
            lambda x:x
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
            object = media(service['func'], hash, url)
            break

    if not object:
        return object
    return object.execute()


class media(object):

    def __init__(self, service, hash, url):
        self.service = service
        self.hash = hash
        self.url = url
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

    def updateDataRecord(self):
        if not self.dataRecord:
            from .models import Cache
            self.dataRecord = Cache.objects.create(hash=self.hash, data='_new_')
        import cPickle as pickle
        data = pickle.dumps(self.data, 2)
        self.dataRecord.data = data
        self.dataRecord.save()

    def execute(self):
        value = self.service()
        self.mainTree = None
        return value

