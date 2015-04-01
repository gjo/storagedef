# -*- coding: utf-8 -*-

import unittest


class MemoryStorageEngineTestCase(unittest.TestCase):

    def test_delete(self):
        from ..memoryengine import MemoryStorageEngine
        engine = MemoryStorageEngine()
        engine.storage['test.ext'] = b'test content'
        engine.delete('test.ext')
        self.assertDictEqual(engine.storage, {})

    def test_exists_false(self):
        from ..memoryengine import MemoryStorageEngine
        engine = MemoryStorageEngine()
        self.assertFalse(engine.exists(b'test.ext'))

    def test_exists_true(self):
        from ..memoryengine import MemoryStorageEngine
        engine = MemoryStorageEngine()
        engine.storage['test.ext'] = b'test content'
        self.assertTrue(engine.exists('test.ext'))

    def test_retrieve_not_found(self):
        from ..exceptions import DoesNotExist
        from ..memoryengine import MemoryStorageEngine
        engine = MemoryStorageEngine()
        self.assertRaises(DoesNotExist, engine.retrieve, 'test.ext')

    def test_retrieve_found(self):
        from ..memoryengine import MemoryStorageEngine
        engine = MemoryStorageEngine()
        engine.storage['test.ext'] = b'test content'
        fobj = engine.retrieve('test.ext')
        self.assertTrue(hasattr(fobj, 'read'))
        self.assertEqual(fobj.read(), b'test content')

    def test_store(self):
        from io import BytesIO
        from ..memoryengine import MemoryStorageEngine
        engine = MemoryStorageEngine()
        engine.store('test.ext', BytesIO(b'test content'))
        self.assertDictEqual(engine.storage, {'test.ext': b'test content'})
