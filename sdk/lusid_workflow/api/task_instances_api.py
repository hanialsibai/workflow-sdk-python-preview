# coding: utf-8

"""
    FINBOURNE Workflow API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.131
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from lusid_workflow.api_client import ApiClient
from lusid_workflow.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)
from lusid_workflow.models.lusid_problem_details import LusidProblemDetails
from lusid_workflow.models.lusid_validation_problem_details import LusidValidationProblemDetails
from lusid_workflow.models.task_instance import TaskInstance


class TaskInstancesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_task_instance(self, id, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] GetTaskInstance: Get a Task Instance.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_task_instance(id, async_req=True)
        >>> result = thread.get()

        :param id: Id of the task instance to retrieve (required)
        :type id: str
        :param as_at:
        :type as_at: datetime
        :param task_instance_scope: The scope of the task instance to retrieve from; 'default' if not provided.
        :type task_instance_scope: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: TaskInstance
        """
        kwargs['_return_http_data_only'] = True
        return self.get_task_instance_with_http_info(id, **kwargs)  # noqa: E501

    def get_task_instance_with_http_info(self, id, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] GetTaskInstance: Get a Task Instance.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_task_instance_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param id: Id of the task instance to retrieve (required)
        :type id: str
        :param as_at:
        :type as_at: datetime
        :param task_instance_scope: The scope of the task instance to retrieve from; 'default' if not provided.
        :type task_instance_scope: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object, the HTTP status code, and the headers.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: (TaskInstance, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'id',
            'as_at',
            'task_instance_scope'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_task_instance" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `get_task_instance`")  # noqa: E501

        if self.api_client.client_side_validation and ('id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['id']) > 40):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `id` when calling `get_task_instance`, length must be less than or equal to `40`")  # noqa: E501
        if self.api_client.client_side_validation and ('id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['id']) < 30):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `id` when calling `get_task_instance`, length must be greater than or equal to `30`")  # noqa: E501
        if self.api_client.client_side_validation and 'id' in local_var_params and not re.search(r'^[a-zA-Z0-9\-]+$', local_var_params['id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `id` when calling `get_task_instance`, must conform to the pattern `/^[a-zA-Z0-9\-]+$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('task_instance_scope' in local_var_params and  # noqa: E501
                                                        len(local_var_params['task_instance_scope']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `task_instance_scope` when calling `get_task_instance`, length must be less than or equal to `64`")  # noqa: E501
        if self.api_client.client_side_validation and ('task_instance_scope' in local_var_params and  # noqa: E501
                                                        len(local_var_params['task_instance_scope']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `task_instance_scope` when calling `get_task_instance`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'task_instance_scope' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['task_instance_scope']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `task_instance_scope` when calling `get_task_instance`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []
        if 'as_at' in local_var_params and local_var_params['as_at'] is not None:  # noqa: E501
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501
        if 'task_instance_scope' in local_var_params and local_var_params['task_instance_scope'] is not None:  # noqa: E501
            query_params.append(('taskInstanceScope', local_var_params['task_instance_scope']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"


        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.1.131'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "TaskInstance",
            400: "LusidValidationProblemDetails",
            404: "str",
        }

        return self.api_client.call_api(
            '/api/taskinstances/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
