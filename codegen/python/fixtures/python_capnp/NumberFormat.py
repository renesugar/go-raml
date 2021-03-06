# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.

"""
Auto-generated class for NumberFormat
"""
import capnp
import os

from . import client_support

dir = os.path.dirname(os.path.realpath(__file__))


class NumberFormat(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type d: float
        :type f: float
        :type i: int
        :type i16: int
        :type i32: int
        :type i64: int
        :type i8: int
        :type l: int
        :type num: float
        :rtype: NumberFormat
        """

        return NumberFormat(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'NumberFormat'
        data = json or kwargs

        # set attributes
        data_types = [float]
        self.d = client_support.set_property('d', data, data_types, False, [], False, True, class_name)
        data_types = [float]
        self.f = client_support.set_property('f', data, data_types, False, [], False, True, class_name)
        data_types = [int]
        self.i = client_support.set_property('i', data, data_types, False, [], False, True, class_name)
        data_types = [int]
        self.i16 = client_support.set_property('i16', data, data_types, False, [], False, True, class_name)
        data_types = [int]
        self.i32 = client_support.set_property('i32', data, data_types, False, [], False, True, class_name)
        data_types = [int]
        self.i64 = client_support.set_property('i64', data, data_types, False, [], False, True, class_name)
        data_types = [int]
        self.i8 = client_support.set_property('i8', data, data_types, False, [], False, True, class_name)
        data_types = [int]
        self.l = client_support.set_property('l', data, data_types, False, [], False, True, class_name)
        data_types = [float]
        self.num = client_support.set_property('num', data, data_types, False, [], False, True, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)

    def to_capnp(self):
        """
        Load the class in capnp schema NumberFormat.capnp
        :rtype bytes
        """
        template = capnp.load('%s/NumberFormat.capnp' % dir)
        return template.NumberFormat.new_message(**self.as_dict()).to_bytes()


class NumberFormatCollection:
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def new(binary=None):
        """
        Load the binary of NumberFormat.capnp into class NumberFormat
        :type binary: bytes. If none creates an empty capnp object.
        rtype: NumberFormat
        """
        template = capnp.load('%s/NumberFormat.capnp' % dir)
        struct = template.NumberFormat.from_bytes(binary) if binary else template.NumberFormat.new_message()
        return NumberFormat(**struct.to_dict(verbose=True))
