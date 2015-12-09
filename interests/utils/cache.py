from django.conf import settings

cache_key_prefix = getattr(settings, 'STOCK_CACHE_KEY_PREFIX', 'stock|')


def gen_cache_key(template, prefix=cache_key_prefix, **keywords):
    key = template.format(**keywords) if keywords else template
    return prefix + key if prefix else key
