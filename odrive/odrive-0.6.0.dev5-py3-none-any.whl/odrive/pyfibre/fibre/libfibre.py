#!/bin/python

from ctypes import *
import asyncio
import os
from itertools import count, takewhile
import struct
from types import MethodType
import concurrent
import threading
import time
import platform
from .utils import Logger, Event
import sys

# Enable this for better tracebacks in some cases
#import tracemalloc
#tracemalloc.start(10)

lib_names = {
    ('Linux', 'x86_64'): 'libfibre-linux-amd64.so',
    ('Linux', 'armv7l'): 'libfibre-linux-armhf.so',
    ('Linux', 'aarch64'): 'libfibre-linux-aarch64.so',
    ('Windows', 'AMD64'): 'libfibre-windows-amd64.dll',
    ('Darwin', 'x86_64'): 'libfibre-macos-x86.dylib'
}

system_desc = (platform.system(), platform.machine())

script_dir = os.path.dirname(os.path.realpath(__file__))
fibre_cpp_paths = [
    os.path.join(os.path.dirname(os.path.dirname(script_dir)), "cpp"),
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(script_dir)))), "Firmware", "fibre-cpp")
]

def get_first(lst, predicate, default):
    for item in lst:
        if predicate(item):
            return item
    return default

if not system_desc in lib_names:
    raise ModuleNotFoundError(("libfibre is not supported on your platform ({} {}). "
            "Go to https://github.com/samuelsadok/fibre-cpp/tree/devel for "
            "instructions on how to compile libfibre. Once you have compiled it, "
            "add it to this folder.").format(*system_desc))

lib_name = lib_names[system_desc]
search_paths = fibre_cpp_paths + [script_dir]

lib_path = get_first(
    (os.path.join(p, lib_name) for p in search_paths),
    os.path.isfile, None)

if lib_path is None:
    raise ModuleNotFoundError("{} was not found in {}".format(lib_name, search_paths))

if os.path.getsize(lib_path) < 1000:
    raise ModuleNotFoundError("{} is too small. Did you forget to init git lfs? Try this:\n"
        " 1. Install git lfs (https://git-lfs.github.com/)\n"
        " 2. Run `cd {}`\n"
        " 3. Run `git lfs install`\n"
        " 4. Run `git lfs pull`".format(lib_path, os.path.dirname(lib_path)))

if os.name == 'nt':
  dll_dir = os.path.dirname(lib_path)
  try:
    # New way in python 3.8+
    os.add_dll_directory(dll_dir)
  except:
    os.environ['PATH'] = dll_dir + os.pathsep + os.environ['PATH']
  lib = windll.LoadLibrary(lib_path)
else:
  lib = cdll.LoadLibrary(lib_path)

# libfibre definitions --------------------------------------------------------#

PostSignature = CFUNCTYPE(c_int, CFUNCTYPE(None, c_void_p), POINTER(c_int))
RegisterEventSignature = CFUNCTYPE(c_int, c_int, c_uint32, CFUNCTYPE(None, c_void_p, c_int), POINTER(c_int))
DeregisterEventSignature = CFUNCTYPE(c_int, c_int)
CallLaterSignature = CFUNCTYPE(c_void_p, c_float, CFUNCTYPE(None, c_void_p), POINTER(c_int))
CancelTimerSignature = CFUNCTYPE(c_int, c_void_p)

OnFoundObjectSignature = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p)
OnLostObjectSignature = CFUNCTYPE(None, c_void_p, c_void_p)
OnStoppedSignature = CFUNCTYPE(None, c_void_p, c_int)

OnAttributeAddedSignature = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p, c_size_t, c_void_p, c_void_p, c_size_t)
OnAttributeRemovedSignature = CFUNCTYPE(None, c_void_p, c_void_p)
OnFunctionAddedSignature = CFUNCTYPE(None, c_void_p, c_void_p, c_void_p, c_size_t, POINTER(c_char_p), POINTER(c_char_p), POINTER(c_char_p), POINTER(c_char_p))
OnFunctionRemovedSignature = CFUNCTYPE(None, c_void_p, c_void_p)

OnCallCompletedSignature = CFUNCTYPE(c_int, c_void_p, c_int, c_void_p, c_void_p, POINTER(c_void_p), POINTER(c_size_t), POINTER(c_void_p), POINTER(c_size_t))
OnTxCompletedSignature = CFUNCTYPE(None, c_void_p, c_void_p, c_int, c_void_p)
OnRxCompletedSignature = CFUNCTYPE(None, c_void_p, c_void_p, c_int, c_void_p)

kFibreOk = 0
kFibreBusy = 1
kFibreCancelled = 2
kFibreClosed = 3
kFibreInvalidArgument = 4
kFibreInternalError = 5
kFibreProtocolError = 6
kFibreHostUnreachable = 7

class LibFibreVersion(Structure):
    _fields_ = [
        ("major", c_uint16),
        ("minor", c_uint16),
        ("patch", c_uint16),
    ]

    def __repr__(self):
        return "{}.{}.{}".format(self.major, self.minor, self.patch)

class LibFibreEventLoop(Structure):
    _fields_ = [
        ("post", PostSignature),
        ("register_event", RegisterEventSignature),
        ("deregister_event", DeregisterEventSignature),
        ("call_later", CallLaterSignature),
        ("cancel_timer", CancelTimerSignature),
    ]

libfibre_get_version = lib.libfibre_get_version
libfibre_get_version.argtypes = []
libfibre_get_version.restype = POINTER(LibFibreVersion)

version = libfibre_get_version().contents
if (version.major, version.minor) != (0, 1):
    raise Exception("Incompatible libfibre version: {}".format(version))

libfibre_open = lib.libfibre_open
libfibre_open.argtypes = [LibFibreEventLoop]
libfibre_open.restype = c_void_p

libfibre_close = lib.libfibre_close
libfibre_close.argtypes = [c_void_p]
libfibre_close.restype = None

libfibre_open_domain = lib.libfibre_open_domain
libfibre_open_domain.argtypes = [c_void_p, c_char_p, c_size_t]
libfibre_open_domain.restype = c_void_p

libfibre_close_domain = lib.libfibre_close_domain
libfibre_close_domain.argtypes = [c_void_p]
libfibre_close_domain.restype = None

libfibre_start_discovery = lib.libfibre_start_discovery
libfibre_start_discovery.argtypes = [c_void_p, c_void_p, OnFoundObjectSignature, OnLostObjectSignature, OnStoppedSignature, c_void_p]
libfibre_start_discovery.restype = None

libfibre_stop_discovery = lib.libfibre_stop_discovery
libfibre_stop_discovery.argtypes = [c_void_p]
libfibre_stop_discovery.restype = None

libfibre_subscribe_to_interface = lib.libfibre_subscribe_to_interface
libfibre_subscribe_to_interface.argtypes = [c_void_p, OnAttributeAddedSignature, OnAttributeRemovedSignature, OnFunctionAddedSignature, OnFunctionRemovedSignature, c_void_p]
libfibre_subscribe_to_interface.restype = None

libfibre_get_attribute = lib.libfibre_get_attribute
libfibre_get_attribute.argtypes = [c_void_p, c_void_p, POINTER(c_void_p)]
libfibre_get_attribute.restype = c_int

libfibre_call = lib.libfibre_call
libfibre_call.argtypes = [c_void_p, POINTER(c_void_p), c_int, c_void_p, c_size_t, c_void_p, c_size_t, POINTER(c_void_p), POINTER(c_void_p), OnCallCompletedSignature, c_void_p]
libfibre_call.restype = c_int

libfibre_start_tx = lib.libfibre_start_tx
libfibre_start_tx.argtypes = [c_void_p, c_char_p, c_size_t, OnTxCompletedSignature, c_void_p]
libfibre_start_tx.restype = None

libfibre_cancel_tx = lib.libfibre_cancel_tx
libfibre_cancel_tx.argtypes = [c_void_p]
libfibre_cancel_tx.restype = None

libfibre_start_rx = lib.libfibre_start_rx
libfibre_start_rx.argtypes = [c_void_p, c_char_p, c_size_t, OnRxCompletedSignature, c_void_p]
libfibre_start_rx.restype = None

libfibre_cancel_rx = lib.libfibre_cancel_rx
libfibre_cancel_rx.argtypes = [c_void_p]
libfibre_cancel_rx.restype = None


# libfibre wrapper ------------------------------------------------------------#

class ObjectLostError(Exception):
    def __init__(self):
        super(Exception, self).__init__("the object disappeared")

def _get_exception(status):
    if status == kFibreOk:
        return None
    elif status == kFibreCancelled:
        return asyncio.CancelledError()
    elif status == kFibreClosed:
        return EOFError()
    elif status == kFibreInvalidArgument:
        return ArgumentError()
    elif status == kFibreInternalError:
        return Exception("internal libfibre error")
    elif status == kFibreProtocolError:
        return Exception("peer misbehaving")
    elif status == kFibreHostUnreachable:
        return ObjectLostError()
    else:
        return Exception("unknown libfibre error {}".format(status))

class StructCodec():
    """
    Generic serializer/deserializer based on struct pack
    """
    def __init__(self, struct_format, target_type):
        self._struct_format = struct_format
        self._target_type = target_type
    def get_length(self):
        return struct.calcsize(self._struct_format)
    def serialize(self, libfibre, value):
        value = self._target_type(value)
        return struct.pack(self._struct_format, value)
    def deserialize(self, libfibre, buffer):
        value = struct.unpack(self._struct_format, buffer)
        value = value[0] if len(value) == 1 else value
        return self._target_type(value)

class ObjectPtrCodec():
    """
    Serializer/deserializer for an object reference

    libfibre transcodes object references internally from/to something that can
    be sent over the wire and understood by the remote instance.
    """
    def get_length(self):
        return struct.calcsize("P")
    def serialize(self, libfibre, value):
        if value is None:
            return struct.pack("P", 0)
        elif isinstance(value, RemoteObject):
            assert(value._obj_handle) # Cannot serialize reference to a lost object
            return struct.pack("P", value._obj_handle)
        else:
            raise TypeError("Expected value of type RemoteObject or None but got '{}'. An example for a RemoteObject is this expression: odrv0.axis0.controller._input_pos_property".format(type(value).__name__))
    def deserialize(self, libfibre, buffer):
        handle = struct.unpack("P", buffer)[0]

        # TODO: this is broken: A function can return an object ref before it is known to PyFibre.
        return None if handle == 0 else libfibre._objects[handle]


codecs = {
    'int8': StructCodec("<b", int),
    'uint8': StructCodec("<B", int),
    'int16': StructCodec("<h", int),
    'uint16': StructCodec("<H", int),
    'int32': StructCodec("<i", int),
    'uint32': StructCodec("<I", int),
    'int64': StructCodec("<q", int),
    'uint64': StructCodec("<Q", int),
    'bool': StructCodec("<?", bool),
    'float': StructCodec("<f", float),
    'object_ref': ObjectPtrCodec()
}

def decode_arg_list(arg_names, codec_names):
    for i in count(0):
        if arg_names[i] is None or codec_names[i] is None:
            break
        arg_name = arg_names[i].decode('utf-8')
        codec_name = codec_names[i].decode('utf-8')
        if not codec_name in codecs:
            raise Exception("unsupported codec {}".format(codec_name))
        yield arg_name, codec_name, codecs[codec_name]

def insert_with_new_id(dictionary, val):
    key = next(x for x in count(1) if x not in set(dictionary.keys()))
    dictionary[key] = val
    return key

# Runs a function on a foreign event loop and blocks until the function is done.
def run_coroutine_threadsafe(loop, func):
    future = concurrent.futures.Future()
    async def func_async():
        try:
            result = func()
            if hasattr(result, '__await__'):
                result = await result
            future.set_result(result)
        except Exception as ex:
            future.set_exception(ex)
    loop.call_soon_threadsafe(asyncio.ensure_future, func_async())
    return future.result()

class TxStream():
    """Python wrapper for libfibre's LibFibreTxStream interface"""

    def __init__(self, libfibre, tx_stream_handle):
        self._libfibre = libfibre
        self._tx_stream_handle = tx_stream_handle
        self._future = None
        self._tx_buf = None
        self._c_on_tx_completed = OnTxCompletedSignature(self._on_tx_completed)
        self.is_closed = False

    def _on_tx_completed(self, ctx, tx_stream, status, tx_end):
        tx_start = cast(self._tx_buf, c_void_p).value

        n_written = tx_end - tx_start
        assert(n_written <= len(self._tx_buf))
        future = self._future
        self._future = None
        self._tx_buf = None
        
        if status == kFibreClosed:
            self.is_closed = True
        
        if status == kFibreOk or status == kFibreClosed:
            future.set_result(n_written)
        else:
            future.set_exception(_get_exception(status))

    def write(self, data):
        """
        Writes the provided data to the stream. Not all bytes are guaranteed to
        be written. The caller should check the return value to determine the
        actual number of bytes written.

        If a non-empty buffer is provided, this function will either write at
        least one byte to the output, set is_closed to True or throw an
        Exception (through the future).

        Currently only one write call may be active at a time (this may change
        in the future).

        Returns: A future that completes with the number of bytes actually
        written or an Exception.
        """
        assert(self._future is None)
        self._future = future = self._libfibre.loop.create_future()
        self._tx_buf = data # Retain a reference to the buffer to prevent it from being garbage collected

        libfibre_start_tx(self._tx_stream_handle,
            cast(self._tx_buf, c_char_p), len(self._tx_buf),
            self._c_on_tx_completed, None)

        return future
        
    async def write_all(self, data):
        """
        Writes all of the provided data to the stream or completes with an
        Exception.

        If an empty buffer is provided, the underlying stream's write function
        is still called at least once.

        Returns: A future that either completes with an empty result or with
        an Exception.
        """

        while True:
            n_written = await self.write(data)
            data = data[n_written:]
            if len(data) == 0:
                break
            elif self.is_closed:
                raise EOFError("the TX stream was closed but there are still {} bytes left to send".format(len(data)))
            assert(n_written > 0) # Ensure progress

class RxStream():
    """Python wrapper for libfibre's LibFibreRxStream interface"""

    def __init__(self, libfibre, rx_stream_handle):
        self._libfibre = libfibre
        self._rx_stream_handle = rx_stream_handle
        self._future = None
        self._rx_buf = None
        self._c_on_rx_completed = OnRxCompletedSignature(self._on_rx_completed)
        self.is_closed = False

    def _on_rx_completed(self, ctx, rx_stream, status, rx_end):
        rx_start = cast(self._rx_buf, c_void_p).value

        n_read = rx_end - rx_start
        assert(n_read <= len(self._rx_buf))
        data = self._rx_buf[:n_read]
        future = self._future
        self._future = None
        self._rx_buf = None
        
        if status == kFibreClosed:
            self.is_closed = True
        
        if status == kFibreOk or status == kFibreClosed:
            future.set_result(data)
        else:
            future.set_exception(_get_exception(status))

    def read(self, n_read):
        """
        Reads up to the specified number of bytes from the stream.

        If more than zero bytes are requested, this function will either read at
        least one byte, set is_closed to True or throw an Exception (through the
        future).

        Currently only one write call may be active at a time (this may change
        in the future).

        Returns: A future that either completes with a buffer containing the
        bytes that were read or completes with an Exception.
        """
        assert(self._future is None)
        self._future = future = self._libfibre.loop.create_future()
        self._rx_buf = bytes(n_read)

        libfibre_start_rx(self._rx_stream_handle,
            cast(self._rx_buf, c_char_p), len(self._rx_buf),
            self._c_on_rx_completed, None)

        return future
        
    async def read_all(self, n_read):
        """
        Reads the specified number of bytes from the stream or throws an
        Exception.

        If zero bytes are requested, the underlying stream's read function
        is still called at least once.

        Returns: A future that either completes with a buffer of size n_read or
        an Exception.
        """

        data = bytes()
        while True:
            chunk = await self.read(n_read - len(data))
            data += chunk
            if n_read == len(data):
                break
            elif self.is_closed:
                raise EOFError()
            assert(len(chunk) > 0) # Ensure progress
        return data


class Call(object):
    """
    This call behaves as you would expect an async generator to behave. This is
    used to provide compatibility down to Python 3.5.
    """
    def __init__(self, func):
        self._func = func
        self._call_handle = c_void_p(0)
        self._is_started = False
        self._should_close = False
        self._is_closed = False
        self._tx_buf = None

    def __aiter__(self):
        return self

    async def asend(self, val):
        assert(self._is_started == (not val is None))
        if not val is None:
            self._tx_buf, self._rx_len, self._should_close = val
        return await self.__anext__()

    async def __anext__(self):
        if not self._is_started:
            self._is_started = True
            return None # This immitates the weird starting behavior of Python 3.6+ async generators iterators

        if self._is_closed:
            raise StopAsyncIteration

        tx_end = c_void_p(0)
        rx_end = c_void_p(0)

        rx_buf = b'\0' * self._rx_len

        call_id = insert_with_new_id(self._func._libfibre._calls, self)

        status = libfibre_call(self._func._func_handle, byref(self._call_handle),
                kFibreClosed if self._should_close else kFibreOk,
                cast(self._tx_buf, c_char_p), len(self._tx_buf),
                cast(rx_buf, c_char_p), len(rx_buf),
                byref(tx_end), byref(rx_end), self._func._libfibre.c_on_call_completed, call_id)

        if status == kFibreBusy:
            self.ag_await = self._func._libfibre.loop.create_future()
            status, tx_end, rx_end = await self.ag_await
            self.ag_await = None

        if status != kFibreOk and status != kFibreClosed:
            raise _get_exception(status)

        n_written = tx_end - cast(self._tx_buf, c_void_p).value
        self._tx_buf = self._tx_buf[n_written:]
        n_read = rx_end - cast(rx_buf, c_void_p).value
        rx_buf = rx_buf[:n_read]

        if status != kFibreOk:
            self._is_closed = True
        return self._tx_buf, rx_buf, self._is_closed

    async def cancel():
        # TODO: this doesn't follow the official Python async generator protocol. Should implement aclose() instead.
        status = libfibre_call(self._func._func_handle, byref(self._call_handle), kFibreOk,
                0, 0, 0, 0, 0, 0, self._func._libfibre.c_on_call_completed, call_id)

    #async def aclose(self):
    #    assert(self._is_started and not self._is_closed)
    #    return self._tx_buf, rx_buf, self._is_closed


class RemoteFunction(object):
    """
    Represents a callable function that maps to a function call on a remote object.
    """
    def __init__(self, libfibre, func_handle, inputs, outputs):
        self._libfibre = libfibre
        self._func_handle = func_handle
        self._inputs = inputs
        self._outputs = outputs
        self._rx_size = sum(codec.get_length() for _, _, codec in self._outputs)

    async def async_call(self, args, cancellation_token):
        #print("making call on " + hex(args[0]._obj_handle))
        tx_buf = bytes()
        for i, arg in enumerate(self._inputs):
            tx_buf += arg[2].serialize(self._libfibre, args[i])
        rx_buf = bytes()

        agen = Call(self)
        
        if not cancellation_token is None:
            cancellation_token.add_done_callback(agen.cancel)

        try:
            assert(await agen.asend(None) is None)

            is_closed = False
            while not is_closed:
                tx_buf, rx_chunk, is_closed = await agen.asend((tx_buf, self._rx_size - len(rx_buf), True))
                rx_buf += rx_chunk

        finally:
            if not cancellation_token is None:
                cancellation_token.remove_done_callback(agen.cancel)

        assert(len(rx_buf) == self._rx_size)

        outputs = []
        for arg in self._outputs:
            arg_length = arg[2].get_length()
            outputs.append(arg[2].deserialize(self._libfibre, rx_buf[:arg_length]))
            rx_buf = rx_buf[arg_length:]

        if len(outputs) == 0:
            return
        elif len(outputs) == 1:
            return outputs[0]
        else:
            return tuple(outputs)

    def __call__(self, *args, cancellation_token = None):
        """
        Starts invoking the remote function. The first argument is usually a
        remote object.
        If this function is called from the Fibre thread then it is nonblocking
        and returns an asyncio.Future. If it is called from another thread then
        it blocks until the function completes and returns the result(s) of the 
        invokation.
        """

        if threading.current_thread() != libfibre_thread:
            return run_coroutine_threadsafe(self._libfibre.loop, lambda: self.__call__(*args))

        if (len(self._inputs) != len(args)):
            raise TypeError("expected {} arguments but have {}".format(len(self._inputs), len(args)))

        coro = self.async_call(args, cancellation_token)
        return asyncio.ensure_future(coro, loop=self._libfibre.loop)

    def __get__(self, instance, owner):
        return MethodType(self, instance) if instance else self

    def _dump(self, name):
        print_arglist = lambda arglist: ", ".join("{}: {}".format(arg_name, codec_name) for arg_name, codec_name, codec in arglist)
        return "{}({}){}".format(name,
            print_arglist(self._inputs),
            "" if len(self._outputs) == 0 else
            " -> " + print_arglist(self._outputs) if len(self._outputs) == 1 else
            " -> (" + print_arglist(self._outputs) + ")")

class RemoteAttribute(object):
    def __init__(self, libfibre, attr_handle, intf_handle, intf_name, magic_getter, magic_setter):
        self._libfibre = libfibre
        self._attr_handle = attr_handle
        self._intf_handle = intf_handle
        self._intf_name = intf_name
        self._magic_getter = magic_getter
        self._magic_setter = magic_setter

    def _get_obj(self, instance):
        assert(not instance._obj_handle is None)

        obj_handle = c_void_p(0)
        status = libfibre_get_attribute(instance._obj_handle, self._attr_handle, byref(obj_handle))
        if status != kFibreOk:
            raise _get_exception(status)
        
        obj = self._libfibre._load_py_obj(obj_handle.value, self._intf_handle)
        if obj in instance._children:
            self._libfibre._release_py_obj(obj_handle.value)
        else:
            # the object will be released when the parent is released
            instance._children.add(obj)

        return obj

    def __get__(self, instance, owner):
        if not instance:
            return self

        if self._magic_getter:
            if threading.current_thread() == libfibre_thread:
                # read() behaves asynchronously when run on the fibre thread
                # which means it returns an awaitable which _must_ be awaited
                # (otherwise it's a bug). However hasattr(...) internally calls
                # __get__ and does not await the result. Thus the safest thing
                # is to just disallow __get__ from run as an async method.
                raise Exception("Cannot use magic getter on Fibre thread. Use _[prop_name]_propery.read() instead.")
            return self._get_obj(instance).read()
        else:
            return self._get_obj(instance)

    def __set__(self, instance, val):
        if self._magic_setter:
            return self._get_obj(instance).exchange(val)
        else:
            raise Exception("this attribute cannot be written to")

class EmptyInterface():
    def __str__(self):
        return "[lost object]"
    def __repr__(self):
        return self.__str__()

class RemoteObject(object):
    """
    Base class for interfaces of remote objects.
    """
    __sealed__ = False

    def __init__(self, libfibre, obj_handle):
        self.__class__._refcount += 1
        self._refcount = 0
        self._children = set()

        self._libfibre = libfibre
        self._obj_handle = obj_handle
        self._on_lost = concurrent.futures.Future() # TODO: maybe we can do this with conc

        # Ensure that assignments to undefined attributes raise an exception
        self.__sealed__ = True

    def __setattr__(self, key, value):
        if self.__sealed__ and not key in dir(self) and not hasattr(self, key):
            raise AttributeError("Attribute {} not found".format(key))
        object.__setattr__(self, key, value)

    #def __del__(self):
    #    print("unref")
    #    libfibre_unref_obj(self._obj_handle)

    def _dump(self, indent, depth):
        if self._obj_handle is None:
            return "[object lost]"

        try:
            if depth <= 0:
                return "..."
            lines = []
            for key in dir(self.__class__):
                if key.startswith('_'):
                    continue
                class_member = getattr(self.__class__, key)
                if isinstance(class_member, RemoteFunction):
                    lines.append(indent + class_member._dump(key))
                elif isinstance(class_member, RemoteAttribute):
                    val = getattr(self, key)
                    if isinstance(val, RemoteObject) and not class_member._magic_getter:
                        lines.append(indent + key + (": " if depth == 1 else ":\n") + val._dump(indent + "  ", depth - 1))
                    else:
                        if isinstance(val, RemoteObject) and class_member._magic_getter:
                            val_str = get_user_name(val)
                        else:
                            val_str = str(val)
                        property_type = str(class_member._get_obj(self).__class__.read._outputs[0][1])
                        lines.append(indent + key + ": " + val_str + " (" + property_type + ")")
                else:
                    lines.append(indent + key + ": " + str(type(val)))
        except:
            return "[failed to dump object]"

        return "\n".join(lines)

    def __str__(self):
        return self._dump("", depth=2)

    def __repr__(self):
        return self.__str__()

    def _destroy(self):
        libfibre = self._libfibre
        on_lost = self._on_lost
        children = self._children

        self._libfibre = None
        self._obj_handle = None
        self._on_lost = None
        self._children = set()

        for child in children:
            libfibre._release_py_obj(child._obj_handle)

        self.__class__._refcount -= 1
        if self.__class__._refcount == 0:
            libfibre.interfaces.pop(self.__class__._handle)

        self.__class__ = EmptyInterface # ensure that this object has no more attributes
        on_lost.set_result(True)


class LibFibre():
    def __init__(self):
        self.loop = asyncio.get_event_loop()

        # We must keep a reference to these function objects so they don't get
        # garbage collected.
        self.c_post = PostSignature(self._post)
        self.c_register_event = RegisterEventSignature(self._register_event)
        self.c_deregister_event = DeregisterEventSignature(self._deregister_event)
        self.c_call_later = CallLaterSignature(self._call_later)
        self.c_cancel_timer = CancelTimerSignature(self._cancel_timer)
        self.c_on_found_object = OnFoundObjectSignature(self._on_found_object)
        self.c_on_lost_object = OnLostObjectSignature(self._on_lost_object)
        self.c_on_discovery_stopped = OnStoppedSignature(self._on_discovery_stopped)
        self.c_on_attribute_added = OnAttributeAddedSignature(self._on_attribute_added)
        self.c_on_attribute_removed = OnAttributeRemovedSignature(self._on_attribute_removed)
        self.c_on_function_added = OnFunctionAddedSignature(self._on_function_added)
        self.c_on_function_removed = OnFunctionRemovedSignature(self._on_function_removed)
        self.c_on_call_completed = OnCallCompletedSignature(self._on_call_completed)
        
        self.timer_map = {}
        self.eventfd_map = {}
        self.interfaces = {} # key: libfibre handle, value: python class
        self.discovery_processes = {} # key: ID, value: python dict
        self._objects = {} # key: libfibre handle, value: python class
        self._calls = {} # key: libfibre handle, value: Call object

        event_loop = LibFibreEventLoop()
        event_loop.post = self.c_post
        event_loop.register_event = self.c_register_event
        event_loop.deregister_event = self.c_deregister_event
        event_loop.call_later = self.c_call_later
        event_loop.cancel_timer = self.c_cancel_timer

        self.ctx = c_void_p(libfibre_open(event_loop))
        assert(self.ctx)

    def _post(self, callback, ctx):
        self.loop.call_soon_threadsafe(callback, ctx)
        return 0

    def _register_event(self, event_fd, events, callback, ctx):
        self.eventfd_map[event_fd] = events
        if (events & 1):
            self.loop.add_reader(event_fd, lambda x: callback(x, 1), ctx)
        if (events & 4):
            self.loop.add_writer(event_fd, lambda x: callback(x, 4), ctx)
        if (events & 0xfffffffa):
            raise Exception("unsupported event mask " + str(events))
        return 0

    def _deregister_event(self, event_fd):
        events = self.eventfd_map.pop(event_fd)
        if (events & 1):
            self.loop.remove_reader(event_fd)
        if (events & 4):
            self.loop.remove_writer(event_fd)
        return 0

    def _call_later(self, delay, callback, ctx):
        timer_id = insert_with_new_id(self.timer_map, self.loop.call_later(delay, callback, ctx))
        return timer_id

    def _cancel_timer(self, timer_id):
        self.timer_map.pop(timer_id).cancel()
        return 0

    def _load_py_intf(self, name, intf_handle):
        """
        Creates a new python type for the specified libfibre interface handle or
        returns the existing python type if one was already create before.

        Behind the scenes the python type will react to future events coming
        from libfibre, such as functions/attributes being added/removed.
        """
        if intf_handle in self.interfaces:
            return self.interfaces[intf_handle]
        else:
            if name is None:
                name = "anonymous_interface_" + str(intf_handle)
            py_intf = self.interfaces[intf_handle] = type(name, (RemoteObject,), {'_handle': intf_handle, '_refcount': 0})
            #exit(1)
            libfibre_subscribe_to_interface(intf_handle, self.c_on_attribute_added, self.c_on_attribute_removed, self.c_on_function_added, self.c_on_function_removed, intf_handle)
            return py_intf

    def _load_py_obj(self, obj_handle, intf_handle):
        if not obj_handle in self._objects:
            name = None # TODO: load from libfibre
            py_intf = self._load_py_intf(name, intf_handle)
            py_obj = py_intf(self, obj_handle)
            self._objects[obj_handle] = py_obj
        else:
            py_obj = self._objects[obj_handle]

        # Note: this refcount does not count the python references to the object
        # but rather mirrors the libfibre-internal refcount of the object. This
        # is so that we can destroy the Python object when libfibre releases it.
        py_obj._refcount += 1
        return py_obj

    def _release_py_obj(self, obj_handle):
        py_obj = self._objects[obj_handle]
        py_obj._refcount -= 1
        if py_obj._refcount <= 0:
            self._objects.pop(obj_handle)
            py_obj._destroy()

    def _on_found_object(self, ctx, obj, intf):
        py_obj = self._load_py_obj(obj, intf)
        discovery = self.discovery_processes[ctx]
        

        # TODO: this is a hack because ObjectPtrCodec is broken
        def load(subobj):
            for key in dir(subobj):
                if not key.startswith('_'):
                    attr = getattr(subobj.__class__, key)
                    if isinstance(attr, RemoteAttribute):
                        load(attr._get_obj(subobj))

        load(py_obj)

        discovery._unannounced.append(py_obj)
        old_future = discovery._future
        discovery._future = self.loop.create_future()
        old_future.set_result(None)
    
    def _on_lost_object(self, ctx, obj):
        assert(obj)
        self._release_py_obj(obj)
    
    def _on_discovery_stopped(self, ctx, result):
        print("discovery stopped")

    def _on_attribute_added(self, ctx, attr, name, name_length, subintf, subintf_name, subintf_name_length):
        name = string_at(name, name_length).decode('utf-8')
        subintf_name = None if subintf_name is None else string_at(subintf_name, subintf_name_length).decode('utf-8')
        intf = self.interfaces[ctx]

        magic_getter = not subintf_name is None and subintf_name.startswith("fibre.Property<") and subintf_name.endswith(">")
        magic_setter = not subintf_name is None and subintf_name.startswith("fibre.Property<readwrite ") and subintf_name.endswith(">")

        setattr(intf, name, RemoteAttribute(self, attr, subintf, subintf_name, magic_getter, magic_setter))
        if magic_getter or magic_setter:
            setattr(intf, "_" + name + "_property", RemoteAttribute(self, attr, subintf, subintf_name, False, False))

    def _on_attribute_removed(self, ctx, attr):
        print("attribute removed") # TODO

    def _on_function_added(self, ctx, func, name, name_length, input_names, input_codecs, output_names, output_codecs):
        name = string_at(name, name_length).decode('utf-8')
        inputs = list(decode_arg_list(input_names, input_codecs))
        outputs = list(decode_arg_list(output_names, output_codecs))
        intf = self.interfaces[ctx]
        setattr(intf, name, RemoteFunction(self, func, inputs, outputs))

    def _on_function_removed(self, ctx, func):
        print("function removed") # TODO

    def _on_call_completed(self, ctx, status, tx_end, rx_end, tx_buf, tx_len, rx_buf, rx_len):
        call = self._calls.pop(ctx)

        call.ag_await.set_result((status, tx_end, rx_end))

        return kFibreBusy

class Discovery():
    """
    All public members of this class are thread-safe.
    """

    def __init__(self, domain):
        self._domain = domain
        self._id = 0
        self._discovery_handle = c_void_p(0)
        self._unannounced = []
        self._future = domain._libfibre.loop.create_future()

    async def _next(self):
        if len(self._unannounced) == 0:
            await self._future
        return self._unannounced.pop(0)

    def _stop(self):
        self._domain._libfibre.discovery_processes.pop(self._id)
        libfibre_stop_discovery(self._discovery_handle)
        self._future.set_exception(asyncio.CancelledError())

    def stop(self):
        if threading.current_thread() == libfibre_thread:
            self._stop()
        else:
            run_coroutine_threadsafe(self._domain._libfibre.loop, self._stop)

class _Domain():
    """
    All public members of this class are thread-safe.
    """

    def __init__(self, libfibre, handle):
        self._libfibre = libfibre
        self._domain_handle = handle

    def _close(self):
        libfibre_close_domain(self._domain_handle)
        self._domain_handle = None
        #decrement_lib_refcount()

    def _start_discovery(self):
        discovery = Discovery(self)
        discovery._id = insert_with_new_id(self._libfibre.discovery_processes, discovery)
        libfibre_start_discovery(self._domain_handle, byref(discovery._discovery_handle), self._libfibre.c_on_found_object, self._libfibre.c_on_lost_object, self._libfibre.c_on_discovery_stopped, discovery._id)
        return discovery

    async def _discover_one(self):
        discovery = self._start_discovery()
        obj = await discovery._next()
        discovery._stop()
        return obj

    def discover_one(self):
        """
        Blocks until exactly one object is discovered.
        """
        return run_coroutine_threadsafe(self._libfibre.loop, self._discover_one)

    def run_discovery(self, callback):
        """
        Invokes `callback` for every object that is discovered. The callback is
        invoked on the libfibre thread and can be an asynchronous function.
        Returns a `Discovery` object on which `stop()` can be called to
        terminate the discovery.
        """
        discovery = run_coroutine_threadsafe(self._libfibre.loop, self._start_discovery)
        async def loop():
            while True:
                obj = await discovery._next()
                await callback(obj)
        self._libfibre.loop.call_soon_threadsafe(lambda: asyncio.ensure_future(loop()))
        return discovery


class Domain():
    def __init__(self, path):
        increment_lib_refcount()
        self._opened_domain = run_coroutine_threadsafe(libfibre.loop, lambda: Domain._open(path))
        
    def _open(path):
        assert(libfibre_thread == threading.current_thread())
        buf = path.encode('ascii')
        domain_handle = libfibre_open_domain(libfibre.ctx, buf, len(buf))
        return _Domain(libfibre, domain_handle)

    def __enter__(self):
        return self._opened_domain

    def __exit__(self, type, value, traceback):
        run_coroutine_threadsafe(self._opened_domain._libfibre.loop, self._opened_domain._close)
        self._opened_domain = None
        decrement_lib_refcount()

libfibre = None

def _run_event_loop():
    global libfibre
    global terminate_libfibre

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    terminate_libfibre = loop.create_future()
    libfibre = LibFibre()

    libfibre.loop.run_until_complete(terminate_libfibre)

    libfibre_close(libfibre.ctx)

    # Detach all objects that still exist
    # TODO: the proper way would be either of these
    #  - provide a libfibre function to destroy an object on-demand which we'd
    #    call before libfibre_close().
    #  - have libfibre_close() report the destruction of all objects

    while len(libfibre._objects):
        libfibre._objects.pop(list(libfibre._objects.keys())[0])._destroy()
    assert(len(libfibre.interfaces) == 0)

    libfibre = None


lock = threading.Lock()
libfibre_refcount = 0
libfibre_thread = None

def increment_lib_refcount():
    global libfibre_refcount
    global libfibre_thread

    with lock:
        libfibre_refcount += 1
        #print("inc refcount to {}".format(libfibre_refcount))

        if libfibre_refcount == 1:
            libfibre_thread = threading.Thread(target = _run_event_loop)
            libfibre_thread.start()

        while libfibre is None:
            time.sleep(0.1)

def decrement_lib_refcount():
    global libfibre_refcount
    global libfibre_thread

    with lock:
        #print("dec refcount from {}".format(libfibre_refcount))
        libfibre_refcount -= 1

        if libfibre_refcount == 0:
            libfibre.loop.call_soon_threadsafe(lambda: terminate_libfibre.set_result(True))

            # It's unlikely that releasing fibre from a fibre callback is ok. If
            # there is a valid scenario for this then we can remove the assert.
            assert(libfibre_thread != threading.current_thread())

            libfibre_thread.join()
            libfibre_thread = None

def get_user_name(obj):
    """
    Can be overridden by the application to return the user-facing name of an
    object.
    """
    return "[anonymous object]"
