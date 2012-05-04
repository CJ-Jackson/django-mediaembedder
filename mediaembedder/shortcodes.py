shortcodes = {}

def embed(kwargs):
    from .mediaembedder import parse
    return parse(kwargs['attr'])

shortcodes['embed'] = embed
