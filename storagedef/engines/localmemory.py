# -*- coding: utf-8 -*-

from io import BytesIO
from zope.interface import implementer
from ..base import StorageEngine
from ..exceptions import DoesNotExist
from ..interfaces import IStorageEngine


@implementer(IStorageEngine)
class LocalMemoryStorageEngine(StorageEngine):

    def __init__(self, **kwargs):
        super(LocalMemoryStorageEngine, self).__init__(**kwargs)
        self.storage = {}

    def delete(self, filename):
        if filename not in self.storage:
            raise DoesNotExist(filename)
        del self.storage[filename]

    def exists(self, filename):
        return filename in self.storage

    def retrieve(self, filename):
        if filename not in self.storage:
            raise DoesNotExist(filename)
        return BytesIO(self.storage[filename])

    def store(self, filename, fileobj):
        v = fileobj.read()
        self.storage[filename] = v
