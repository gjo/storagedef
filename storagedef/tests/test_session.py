# -*- coding: utf-8 -*-

import unittest


class SessionTestCase(unittest.TestCase):

    def test_load_memory(self):
        from ..session import Session
        from ..engines.localmemory import LocalMemoryStorageEngine
        session = Session.from_config({
            'provider': 'storagedef:LocalMemoryStorageEngine'
        })
        self.assertIsInstance(session.engine, LocalMemoryStorageEngine)
