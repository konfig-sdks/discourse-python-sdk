# coding: utf-8

"""
    Discourse API Documentation

    This page contains the documentation on how to use Discourse through API calls.  > Note: For any endpoints not listed you can follow the [reverse engineer the Discourse API](https://meta.discourse.org/t/-/20576) guide to figure out how to use an API endpoint.  ### Request Content-Type  The Content-Type for POST and PUT requests can be set to `application/x-www-form-urlencoded`, `multipart/form-data`, or `application/json`.  ### Endpoint Names and Response Content-Type  Most API endpoints provide the same content as their HTML counterparts. For example the URL `/categories` serves a list of categories, the `/categories.json` API provides the same information in JSON format.  Instead of sending API requests to `/categories.json` you may also send them to `/categories` and add an `Accept: application/json` header to the request to get the JSON response. Sending requests with the `Accept` header is necessary if you want to use URLs for related endpoints returned by the API, such as pagination URLs. These URLs are returned without the `.json` prefix so you need to add the header in order to get the correct response format.  ### Authentication  Some endpoints do not require any authentication, pretty much anything else will require you to be authenticated.  To become authenticated you will need to create an API Key from the admin panel.  Once you have your API Key you can pass it in along with your API Username as an HTTP header like this:  ``` curl -X GET \"http://127.0.0.1:3000/admin/users/list/active.json\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" ```  and this is how POST requests will look:  ``` curl -X POST \"http://127.0.0.1:3000/categories\" \\ -H \"Content-Type: multipart/form-data;\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" \\ -F \"name=89853c20-4409-e91a-a8ea-f6cdff96aaaa\" \\ -F \"color=49d9e9\" \\ -F \"text_color=f0fcfd\" ```  ### Boolean values  If an endpoint accepts a boolean be sure to specify it as a lowercase `true` or `false` value unless noted otherwise. 

    The version of the OpenAPI document: latest
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from discourse_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from discourse_python_sdk.api_response import AsyncGeneratorResponse
from discourse_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from discourse_python_sdk import schemas  # noqa: F401

from discourse_python_sdk.model.uploads_complete_external_upload_response import UploadsCompleteExternalUploadResponse as UploadsCompleteExternalUploadResponseSchema
from discourse_python_sdk.model.uploads_complete_external_upload_request import UploadsCompleteExternalUploadRequest as UploadsCompleteExternalUploadRequestSchema

from discourse_python_sdk.type.uploads_complete_external_upload_response import UploadsCompleteExternalUploadResponse
from discourse_python_sdk.type.uploads_complete_external_upload_request import UploadsCompleteExternalUploadRequest

from ...api_client import Dictionary
from discourse_python_sdk.pydantic.uploads_complete_external_upload_response import UploadsCompleteExternalUploadResponse as UploadsCompleteExternalUploadResponsePydantic
from discourse_python_sdk.pydantic.uploads_complete_external_upload_request import UploadsCompleteExternalUploadRequest as UploadsCompleteExternalUploadRequestPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = UploadsCompleteExternalUploadRequestSchema


request_body_uploads_complete_external_upload_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = UploadsCompleteExternalUploadResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: UploadsCompleteExternalUploadResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: UploadsCompleteExternalUploadResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _complete_external_upload_mapped_args(
        self,
        unique_identifier: str,
        for_private_message: typing.Optional[str] = None,
        for_site_setting: typing.Optional[str] = None,
        pasted: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if unique_identifier is not None:
            _body["unique_identifier"] = unique_identifier
        if for_private_message is not None:
            _body["for_private_message"] = for_private_message
        if for_site_setting is not None:
            _body["for_site_setting"] = for_site_setting
        if pasted is not None:
            _body["pasted"] = pasted
        args.body = _body
        return args

    async def _acomplete_external_upload_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Completes a direct external upload
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/uploads/complete-external-upload.json',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_uploads_complete_external_upload_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _complete_external_upload_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Completes a direct external upload
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/uploads/complete-external-upload.json',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_uploads_complete_external_upload_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CompleteExternalUploadRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acomplete_external_upload(
        self,
        unique_identifier: str,
        for_private_message: typing.Optional[str] = None,
        for_site_setting: typing.Optional[str] = None,
        pasted: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._complete_external_upload_mapped_args(
            unique_identifier=unique_identifier,
            for_private_message=for_private_message,
            for_site_setting=for_site_setting,
            pasted=pasted,
        )
        return await self._acomplete_external_upload_oapg(
            body=args.body,
            **kwargs,
        )
    
    def complete_external_upload(
        self,
        unique_identifier: str,
        for_private_message: typing.Optional[str] = None,
        for_site_setting: typing.Optional[str] = None,
        pasted: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._complete_external_upload_mapped_args(
            unique_identifier=unique_identifier,
            for_private_message=for_private_message,
            for_site_setting=for_site_setting,
            pasted=pasted,
        )
        return self._complete_external_upload_oapg(
            body=args.body,
        )

class CompleteExternalUpload(BaseApi):

    async def acomplete_external_upload(
        self,
        unique_identifier: str,
        for_private_message: typing.Optional[str] = None,
        for_site_setting: typing.Optional[str] = None,
        pasted: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> UploadsCompleteExternalUploadResponsePydantic:
        raw_response = await self.raw.acomplete_external_upload(
            unique_identifier=unique_identifier,
            for_private_message=for_private_message,
            for_site_setting=for_site_setting,
            pasted=pasted,
            **kwargs,
        )
        if validate:
            return UploadsCompleteExternalUploadResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(UploadsCompleteExternalUploadResponsePydantic, raw_response.body)
    
    
    def complete_external_upload(
        self,
        unique_identifier: str,
        for_private_message: typing.Optional[str] = None,
        for_site_setting: typing.Optional[str] = None,
        pasted: typing.Optional[str] = None,
        validate: bool = False,
    ) -> UploadsCompleteExternalUploadResponsePydantic:
        raw_response = self.raw.complete_external_upload(
            unique_identifier=unique_identifier,
            for_private_message=for_private_message,
            for_site_setting=for_site_setting,
            pasted=pasted,
        )
        if validate:
            return UploadsCompleteExternalUploadResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(UploadsCompleteExternalUploadResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        unique_identifier: str,
        for_private_message: typing.Optional[str] = None,
        for_site_setting: typing.Optional[str] = None,
        pasted: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._complete_external_upload_mapped_args(
            unique_identifier=unique_identifier,
            for_private_message=for_private_message,
            for_site_setting=for_site_setting,
            pasted=pasted,
        )
        return await self._acomplete_external_upload_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        unique_identifier: str,
        for_private_message: typing.Optional[str] = None,
        for_site_setting: typing.Optional[str] = None,
        pasted: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._complete_external_upload_mapped_args(
            unique_identifier=unique_identifier,
            for_private_message=for_private_message,
            for_site_setting=for_site_setting,
            pasted=pasted,
        )
        return self._complete_external_upload_oapg(
            body=args.body,
        )

