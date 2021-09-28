import ast
import functools
import sys
from typing import Iterable
from typing import List
from typing import Tuple

from tokenize_rt import NON_CODING_TOKENS
from tokenize_rt import Offset
from tokenize_rt import Token

from pyupgrade._ast_helpers import ast_to_offset
from pyupgrade._ast_helpers import is_name_attr
from pyupgrade._data import register
from pyupgrade._data import State
from pyupgrade._data import TokenFunc
from pyupgrade._token_helpers import CLOSING
from pyupgrade._token_helpers import find_closing_bracket
from pyupgrade._token_helpers import find_token
from pyupgrade._token_helpers import OPENING


def _fix_optional(i: int, tokens: List[Token]) -> None:
    j = find_token(tokens, i, '[')
    k = find_closing_bracket(tokens, j)
    if tokens[j].line == tokens[k].line:
        tokens[k] = Token('CODE', ' | None')
        del tokens[i:j + 1]
    else:
        tokens[j] = tokens[j]._replace(src='(')
        tokens[k] = tokens[k]._replace(src=')')
        tokens[i:j] = [Token('CODE', 'None | ')]


def _fix_union(
        i: int,
        tokens: List[Token],
        *,
        arg_count: int,
) -> None:
    depth = 1
    parens_done = []
    open_parens = []
    commas = []
    coding_depth = None

    j = find_token(tokens, i, '[')
    k = j + 1
    while depth:
        # it's possible our first coding token is a close paren
        # so make sure this is separate from the if chain below
        if (
                tokens[k].name not in NON_CODING_TOKENS and
                tokens[k].src != '(' and
                coding_depth is None
        ):
            if tokens[k].src == ')':  # the coding token was an empty tuple
                coding_depth = depth - 1
            else:
                coding_depth = depth

        if tokens[k].src in OPENING:
            if tokens[k].src == '(':
                open_parens.append((depth, k))

            depth += 1
        elif tokens[k].src in CLOSING:
            if tokens[k].src == ')':
                paren_depth, open_paren = open_parens.pop()
                parens_done.append((paren_depth, (open_paren, k)))

            depth -= 1
        elif tokens[k].src == ',':
            commas.append((depth, k))

        k += 1
    k -= 1

    assert coding_depth is not None
    assert not open_parens, open_parens
    comma_depth = min((depth for depth, _ in commas), default=sys.maxsize)
    min_depth = min(comma_depth, coding_depth)

    to_delete = [
        paren
        for depth, positions in parens_done
        if depth < min_depth
        for paren in positions
    ]

    if comma_depth <= coding_depth:
        comma_positions = [k for depth, k in commas if depth == comma_depth]
        if len(comma_positions) == arg_count:
            to_delete.append(comma_positions.pop())
    else:
        comma_positions = []

    to_delete.sort()

    if tokens[j].line == tokens[k].line:
        del tokens[k]
        for comma in comma_positions:
            tokens[comma] = Token('CODE', ' |')
        for paren in reversed(to_delete):
            del tokens[paren]
        del tokens[i:j + 1]
    else:
        tokens[j] = tokens[j]._replace(src='(')
        tokens[k] = tokens[k]._replace(src=')')

        for comma in comma_positions:
            tokens[comma] = Token('CODE', ' |')
        for paren in reversed(to_delete):
            del tokens[paren]
        del tokens[i:j]


def _supported_version(state: State) -> bool:
    return (
        state.in_annotation and (
            state.settings.min_version >= (3, 10) or (
                not state.settings.keep_runtime_typing and
                'annotations' in state.from_imports['__future__']
            )
        )
    )


@register(ast.Subscript)
def visit_Subscript(
        state: State,
        node: ast.Subscript,
        parent: ast.AST,
) -> Iterable[Tuple[Offset, TokenFunc]]:
    if not _supported_version(state):
        return

    if is_name_attr(node.value, state.from_imports, 'typing', ('Optional',)):
        yield ast_to_offset(node), _fix_optional
    elif is_name_attr(node.value, state.from_imports, 'typing', ('Union',)):
        if sys.version_info >= (3, 9):  # pragma: no cover (py39+)
            node_slice: ast.expr = node.slice
        elif isinstance(node.slice, ast.Index):  # pragma: no cover (<py39)
            node_slice = node.slice.value
        else:  # pragma: no cover (<py39)
            return  # unexpected slice type

        if isinstance(node_slice, ast.Tuple):
            if node_slice.elts:
                arg_count = len(node_slice.elts)
            else:
                return  # empty Union
        else:
            arg_count = 1

        func = functools.partial(_fix_union, arg_count=arg_count)
        yield ast_to_offset(node), func
