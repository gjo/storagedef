# -*- coding: utf-8 -*-

import unittest


class FromConfigTestCase(unittest.TestCase):

    def test_load_memory(self):
        from ..loader import from_config
        from ..memoryengine import MemoryStorageEngine
        storage = from_config({'provider': 'storagedef:MemoryStorageEngine'})
        self.assertIsInstance(storage, MemoryStorageEngine)
