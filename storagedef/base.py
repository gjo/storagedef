# -*- coding: utf-8 -*-


class StorageEngine(object):

    def __init__(self, **kwargs):
        for k in kwargs:
            if hasattr(self, k):
                setattr(self, k, kwargs[k])

    def delete(self, filename):
        """
        :type filename: str
        """
        raise NotImplementedError

    def exists(self, filename):
        """
        :type filename: str
        :rtype: bool
        """
        raise NotImplementedError

    def retrieve(self, filename):
        """
        :type filename: str
        :rtype: fileobj
        """
        raise NotImplementedError

    def store(self, filename, fileobj):
        raise NotImplementedError
