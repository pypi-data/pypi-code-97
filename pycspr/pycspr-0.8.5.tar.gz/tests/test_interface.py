import enum
import inspect

import pycspr



def _has_class(mod, cls):
    """Asserts that a container exposes a class.

    """
    _has_member(mod, cls)
    assert inspect.isclass(getattr(mod, cls)), '{} is not a class'.format(cls)


def _has_constant(mod, constant):
    """Asserts that a container exposes a constant.

    """
    _has_member(mod, constant)


def _has_enum(mod, enm):
    """Asserts that a container exposes an enumeration.

    """
    _has_member(mod, enm)
    assert issubclass(getattr(mod, enm), enum.Enum), '{} is not an enum'.format(enm)


def _has_exception(mod, err):
    """Asserts that a container exposes an exception.

    """
    _has_class(mod, err)
    assert issubclass(getattr(mod, err), Exception), \
           'Exception type does not inherit from builtin Exception class.'


def _has_function(mod, func):
    """Asserts that a container exposes a function.

    """
    _has_member(mod, func)
    assert inspect.isfunction(getattr(mod, func)), '{} is not a function'.format(func)


def _has_member(mod, member):
    """Asserts that a module exposes a member.

    """
    assert inspect.ismodule(mod)
    assert hasattr(mod, member), 'Missing member: {}'.format(member)


# Expected interface.
_INTERFACE_OF_LIBRARY = {
    _has_class: {
        "NodeClient",
        "NodeConnectionInfo",
    },
    _has_enum: {
        "NodeSseChannelType",
        "NodeSseEventType",
        "HashAlgorithm",
        "KeyAlgorithm",
    },
    _has_constant: set(),
    _has_exception: set(),
    _has_function: {
        "create_deploy",
        "create_deploy_approval",
        "create_deploy_parameters",
        "create_deploy_argument",
        "create_standard_payment",
        "create_native_transfer",
        "create_validator_auction_bid",
        "create_validator_auction_bid_withdrawal",
        "create_validator_delegation",
        "create_validator_delegation_withdrawal",
        "parse_public_key",
        "parse_private_key",
        "get_account_hash",
        "get_account_key",
        "get_account_key_algo",
        "read_deploy",
        "read_wasm",
        "write_deploy",
    },
    _has_member: {
        "crypto",
        "factory",
        "serialisation",
        "types",
    }
}


# Expected interface of factory methods.
_INTERFACE_OF_FACTORY = {
    _has_member: {
        "accounts",
        "cl",
        "deploys",
    },
}


def test_version_of_library():
    assert pycspr.__version__ == "0.8.5"


def test_exports_of_library():
    for assertor, members in _INTERFACE_OF_LIBRARY.items():
        for member in members:
            assertor(pycspr, member)


def test_exports_of_factory():
    _test_exports(pycspr.factory, _INTERFACE_OF_FACTORY)


def _test_exports(module, interface):
    for assertor, members in interface.items():
        for member in members:
            assertor(module, member)
