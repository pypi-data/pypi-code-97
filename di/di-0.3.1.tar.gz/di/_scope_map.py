from __future__ import annotations

from typing import Any, Dict, Generic, Hashable, List, TypeVar, Union, overload

from di.dependency import Scope
from di.exceptions import DuplicateScopeError, UnknownScopeError

T = TypeVar("T")
KT = TypeVar("KT", bound=Hashable)
VT = TypeVar("VT")


_unset: Any = object()


class ScopeMap(Generic[KT, VT]):
    """Mapping-like structure to hold binds and cached values.

    The important aspect of this is that we may have thousands of dependencies, but generally only a couple (<10) scopes.
    So this is designed to operate in ~ O(S) time, where S is the number of scopes.
    Imporantly, when we enter or exit a scope (which can happen very frequently, e.g. requests in a web framework),
    no iteration is required: we can simply pop all keys in that scope.

    The interface is *almost* a Mapping[KT, VT] but not quite: some operations like set / __setitem__ require a key, a value *and* a scope.
    We could implement ScopeMap[key, scope] = value, but that can lead to a bit of confusion since we want lookups like ScopMap[key].
    Additionally, operations are not O(1) but rather O(S).
    So we choose to use method names like get() and set() to deal with the API differences and indicate that operations are more expensive than O(1).
    This is also similar to collections.ChainMap, except that we want "named" nodes (Scopes) and ChainMap uses a plain list.
    ChainMap also doesn't allow you to set values anywhere but the left mapping, and we need to set values in arbitrary mappings.
    """

    def __init__(self) -> None:
        self.mappings: Dict[Scope, Dict[KT, VT]] = {}

    def get(self, key: KT) -> VT:
        for mapping in self.mappings.values():
            if key in mapping:
                return mapping[key]
        raise KeyError(key)

    def set(self, key: KT, value: VT, *, scope: Scope) -> None:
        if scope not in self.mappings:
            raise UnknownScopeError(
                f"The scope {scope} is not amongst the known scopes: {self.mappings.keys()}"
            )
        for mapping_scope, mapping in self.mappings.items():
            if scope == mapping_scope:
                mapping[key] = value
            else:
                if key in mapping:
                    mapping.pop(key)

    @overload
    def pop(self, key: KT) -> VT:
        ...

    @overload
    def pop(self, key: KT, default: T) -> Union[VT, T]:
        ...

    def pop(self, key: KT, default: T = _unset) -> Union[VT, T]:
        for mapping in self.mappings.values():
            if key in mapping:
                return mapping.pop(key)
        if default is not _unset:
            return default
        raise KeyError(key)

    def contains(self, key: KT) -> bool:
        for mapping in self.mappings.values():
            if key in mapping:
                return True
        return False

    def get_scope(self, key: KT) -> Scope:
        for scope, mapping in self.mappings.items():
            if key in mapping:
                return scope
        raise KeyError(key)

    def add_scope(self, scope: Scope) -> None:
        if scope in self.mappings:
            raise DuplicateScopeError(f"The scope {scope} already exists!")
        self.mappings[scope] = {}

    def pop_scope(self, scope: Scope) -> None:
        if scope not in self.mappings:
            raise UnknownScopeError(
                f"The scope {scope} is not amongst the known scopes: {self.mappings.keys()}"
            )
        self.mappings.pop(scope)

    def has_scope(self, scope: Scope) -> bool:
        return scope in self.mappings

    def copy(self) -> ScopeMap[KT, VT]:
        new = ScopeMap[KT, VT]()
        new.mappings = self.mappings.copy()
        return new

    def __repr__(self) -> str:  # pragma: no cover, used only for debugging
        values: List[str] = []
        for scope, mapping in self.mappings.items():
            for k, v in mapping.items():
                values.append(f'{repr(k)}: {repr(v)} @ scope="{scope}"')
        return "{" + ", ".join(values) + "}"
