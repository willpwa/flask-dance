import six
from abc import ABCMeta, abstractmethod


class BaseBackend(six.with_metaclass(ABCMeta)):
    @abstractmethod
    def get(self, blueprint):
        return None

    @abstractmethod
    def set(self, blueprint, token):
        return None

    @abstractmethod
    def delete(self, blueprint):
        return None


class NullBackend(BaseBackend):
    """
    This mock storage will never store OAuth tokens.
    If you try to retrieve a token from this storage, you will always
    get ``None``.
    """

    def get(self, blueprint):
        return None

    def set(self, blueprint, token):
        return None

    def delete(self, blueprint):
        return None


class MemoryBackend(BaseBackend):
    """
    This mock storage stores an OAuth token in memory and so that it can
    be retrieved later. Since the token is not persisted in any way,
    this is mostly useful for writing automated tests.

    The initializer accepts a ``token`` argument, for setting the
    initial value of the token.
    """

    def __init__(self, token=None, *args, **kwargs):
        self.token = token

    def get(self, blueprint):
        return self.token

    def set(self, blueprint, token):
        self.token = token

    def delete(self, blueprint):
        self.token = None
