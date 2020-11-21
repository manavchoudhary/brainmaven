from collections import OrderedDict

class LRU_cache():
    def __init__(self, max_size):
        self.cache = OrderedDict()
        self.max_size = max_size

    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key, last=True)
            val =  self.cache[key]
            return val
    def put(self, key, val):
        if(len(self.cache.keys()) == self.max_size):
            self.cache.popitem(last=False)
        self.cache[key] = val


def test_case_1():
    lru_cache = LRU_cache(2)
    lru_cache.put('a', 1)
    assert lru_cache.cache == OrderedDict({'a':1})
    lru_cache.put('b', 2)
    assert lru_cache.cache == OrderedDict({'a':1, 'b':2})
    val = lru_cache.get('a')
    assert val == 1
    assert lru_cache.cache == OrderedDict({'b':2, 'a':1})
    lru_cache.put('c', 3)
    assert lru_cache.cache == OrderedDict({'a':1, 'c':3})
    val = lru_cache.get('b')
    assert val == -1
    assert lru_cache.cache == OrderedDict({'a':1, 'c':3})
    lru_cache.put('d', 4)
    assert lru_cache.cache == OrderedDict({'c':3, 'd':4})
    val = lru_cache.get('a')
    assert val == -1
    assert lru_cache.cache == OrderedDict({'c':3, 'd':4})
    val = lru_cache.get('c')
    assert val == 3
    assert lru_cache.cache == OrderedDict({'d':4, 'c':3})
    val = lru_cache.get('d')
    assert val == 4
    assert lru_cache.cache == OrderedDict({'c':3, 'd':4})
    print('Test Case 1 passed')

test_case_1()