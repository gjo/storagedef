# -*- coding: utf-8 -*-

import unittest


class FromConfigTestCase(unittest.TestCase):

    def test_load_memory(self):
        from ..loader import from_config
        from ..engines.localmemory import LocalMemoryStorageEngine
        storage = from_config({
            'provider': 'storagedef:LocalMemoryStorageEngine'
        })
        self.assertIsInstance(storage, LocalMemoryStorageEngine)
