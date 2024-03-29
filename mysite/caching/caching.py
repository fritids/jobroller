from django.core.cache import cache
from example_bootstrap.settings import CACHE_TIMEOUT

def cache_update(sender, **kwargs):
	item = kwargs.get('instance')
	cache.set(item.cache_key, item, CACHE_TIMEOUT)
	
def cache_evict(sender, **kwargs):
	item = kwargs.get('instance')
	cache.delete(item.cache_key)

