from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.create_model_response import CreateModelResponse
from ...models.create_multi_forecasting_request import CreateMultiForecastingRequest
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CreateMultiForecastingRequest,

) -> Dict[str, Any]:
    url = "{}/v1/models/multiforecasting".format(
        client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    json_json_body = json_body.to_dict()



    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[
    CreateModelResponse,
    None,
    None,
    None,
    None
]]:
    if response.status_code == 201:
        response_201 = CreateModelResponse.from_dict(response.json())



        return response_201
    if response.status_code == 400:
        response_400 = None

        return response_400
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
    CreateModelResponse,
    None,
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
    json_body: CreateMultiForecastingRequest,

) -> Response[Union[
    CreateModelResponse,
    None,
    None,
    None,
    None
]]:
    kwargs = _get_kwargs(
        client=client,
json_body=json_body,

    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    *,
    client: Client,
    json_body: CreateMultiForecastingRequest,

) -> Optional[Union[
    CreateModelResponse,
    None,
    None,
    None,
    None
]]:
    """ Creates a new time-series multi-series forecasting model with the supplied configuration. """

    return sync_detailed(
        client=client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    *,
    client: Client,
    json_body: CreateMultiForecastingRequest,

) -> Response[Union[
    CreateModelResponse,
    None,
    None,
    None,
    None
]]:
    kwargs = _get_kwargs(
        client=client,
json_body=json_body,

    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    *,
    client: Client,
    json_body: CreateMultiForecastingRequest,

) -> Optional[Union[
    CreateModelResponse,
    None,
    None,
    None,
    None
]]:
    """ Creates a new time-series multi-series forecasting model with the supplied configuration. """

    return (await asyncio_detailed(
        client=client,
json_body=json_body,

    )).parsed
