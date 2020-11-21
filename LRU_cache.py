from collections import OrderedDict

class LRU_cache():
    def __init__(self, max_size):
        self.cache = OrderedDict()
        self.max_size = max_size

    def get(self, key):
        if key not in self.cache:
            return None
        else:
            self.cache.move_to_end(key, last=True)
            val = self.cache[key]
            return val

    def put(self, key, val):
        if key in self.cache:
            self.cache[key] = val
            self.cache.move_to_end(key, last=True)
            return
        if(len(self.cache.keys()) == self.max_size):
            self.cache.popitem(last=False)
        self.cache[key] = val
        return

    def delete(self, key):
        if key not in self.cache:
            return None
        else:
            val = self.cache.pop(key)
            return val

    def reset(self):
        self.cache = OrderedDict()
        return

# Unit Test case 1
# This checks the basic put and get functionality
def unit_test_1():
    lru_cache = LRU_cache(2)
    lru_cache.put('a', 1)
    assert lru_cache.cache == OrderedDict({'a':1})
    lru_cache.put('b', 2)
    assert lru_cache.cache == OrderedDict({'a':1, 'b':2})
    val = lru_cache.get('a')
    assert val == 1
    assert lru_cache.cache == OrderedDict({'b':2, 'a':1})
    print('Unit Test 1 passed')

# Unit Test case 2
# This checks that when the cache size is full the Least Recently Used item is removed
def unit_test_2():
    lru_cache = LRU_cache(2)
    lru_cache.put('a', 1)
    lru_cache.put('b', 2)
    val = lru_cache.get('a')
    lru_cache.put('c', 3)
    assert lru_cache.cache == OrderedDict({'a':1, 'c':3})
    val = lru_cache.get('b')
    assert val == None
    assert lru_cache.cache == OrderedDict({'a':1, 'c':3})
    print('Unit Test 2 passed')

# Unit Test case 3
# This also checks that when the cache size is full the Least Recently used item is removed for 2 such removals
def unit_test_3():
    lru_cache = LRU_cache(2)
    lru_cache.put('a', 1)
    lru_cache.put('b', 2)
    val = lru_cache.get('a')
    lru_cache.put('c', 3)
    lru_cache.put('d', 4)
    assert lru_cache.cache == OrderedDict({'c':3, 'd':4})
    val = lru_cache.get('a')
    assert val == None
    assert lru_cache.cache == OrderedDict({'c':3, 'd':4})
    print('Unit Test 3 passed')

# Unit Test case 4
# This checks that when a key is 'get', it becomes the most recently used item properly
def unit_test_4():
    lru_cache = LRU_cache(2)
    lru_cache.put('a', 1)
    lru_cache.put('b', 2)
    val = lru_cache.get('a')
    lru_cache.put('c', 3)
    lru_cache.put('d', 4)
    val = lru_cache.get('c')
    assert val == 3
    assert lru_cache.cache == OrderedDict({'d':4, 'c':3})
    val = lru_cache.get('d')
    assert val == 4
    assert lru_cache.cache == OrderedDict({'c':3, 'd':4})
    print('Unit Test 4 passed')

# Unit Test case 5
# This checks that if a key is deleted properly
def unit_test_5():
    lru_cache = LRU_cache(2)
    lru_cache.put('a', 1)
    lru_cache.put('b', 2)
    val = lru_cache.get('a')
    lru_cache.put('c', 3)
    lru_cache.put('d', 4)
    val = lru_cache.delete('c')
    assert val == 3
    assert lru_cache.delete('c') == None
    print('Unit Test 5 passed')

# Unit Test case 6
# This checks that if the LRU cache is reset properly
def unit_test_6():
    lru_cache = LRU_cache(2)
    lru_cache.put('a', 1)
    lru_cache.put('b', 2)
    lru_cache.reset()
    assert lru_cache.cache == OrderedDict()
    print('Unit Test 6 passed')

# Unit Test case 7
# This checks that if a key is 'Put' 2 times, i.e if the key is overwritten properly
def unit_test_7():
    lru_cache = LRU_cache(2)
    lru_cache.put('a', 1)
    lru_cache.put('b', 2)
    assert lru_cache.cache == OrderedDict({'a': 1, 'b': 2})
    lru_cache.put('a', 5)
    assert lru_cache.cache == OrderedDict({'b': 2, 'a': 5})
    print('Unit Test 7 passed')

unit_test_1()
unit_test_2()
unit_test_3()
unit_test_4()
unit_test_5()
unit_test_6()
unit_test_7()