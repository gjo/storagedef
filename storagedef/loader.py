# -*- coding: utf-8 -*-

from paste.deploy.util import lookup_object
from zope.interface.verify import verifyObject
from .interfaces import IStorageEngine


def from_config(config, prefix='', **kwargs):
    """
    :type config: dict
    :type prefix: str
    :rtype: IStorage
    """
    config = dict((k[len(prefix):], config[k]) for k in config
                  if k.startswith(prefix))
    config.update(kwargs)
    factory_name = config.pop('provider')
    factory = lookup_object(factory_name)
    storage = factory(**config)
    verifyObject(IStorageEngine, storage)
    return storage
