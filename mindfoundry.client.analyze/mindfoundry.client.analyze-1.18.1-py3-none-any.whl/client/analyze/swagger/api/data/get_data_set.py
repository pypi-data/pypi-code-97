from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.data_set_response import DataSetResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    id: int,

) -> Dict[str, Any]:
    url = "{}/v1/dataSets/{id}".format(
        client.base_url,id=id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[
    DataSetResponse,
    None,
    None,
    None
]]:
    if response.status_code == 200:
        response_200 = DataSetResponse.from_dict(response.json())



        return response_200
    if response.status_code == 401:
        response_401 = None

        return response_401
    if response.status_code == 403:
        response_403 = None

        return response_403
    if response.status_code == 404:
        response_404 = None

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[
    DataSetResponse,
    None,
    None,
    None
]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    id: int,

) -> Response[Union[
    DataSetResponse,
    None,
    None,
    None
]]:
    kwargs = _get_kwargs(
        client=client,
id=id,

    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    *,
    client: Client,
    id: int,

) -> Optional[Union[
    DataSetResponse,
    None,
    None,
    None
]]:
    """ Gets general information about the data set """

    return sync_detailed(
        client=client,
id=id,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    id: int,

) -> Response[Union[
    DataSetResponse,
    None,
    None,
    None
]]:
    kwargs = _get_kwargs(
        client=client,
id=id,

    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    *,
    client: Client,
    id: int,

) -> Optional[Union[
    DataSetResponse,
    None,
    None,
    None
]]:
    """ Gets general information about the data set """

    return (await asyncio_detailed(
        client=client,
id=id,

    )).parsed
