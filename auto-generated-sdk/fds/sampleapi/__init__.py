# coding: utf-8

# flake8: noqa

"""
    Swagger Petstore

    This is a sample server Petstore server.  You can find out more about     Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).      For this sample, you can use the api key `special-key` to test the authorization     filters.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "0.0.0"

# import apis into sdk package
from fds.sampleapi.api.pet_api import PetApi
from fds.sampleapi.api.store_api import StoreApi
from fds.sampleapi.api.user_api import UserApi

# import ApiClient
from fds.sampleapi.api_client import ApiClient
from fds.sampleapi.configuration import Configuration
from fds.sampleapi.exceptions import OpenApiException
from fds.sampleapi.exceptions import ApiTypeError
from fds.sampleapi.exceptions import ApiValueError
from fds.sampleapi.exceptions import ApiKeyError
from fds.sampleapi.exceptions import ApiException
# import models into sdk package
from fds.sampleapi.models.api_response import ApiResponse
from fds.sampleapi.models.category import Category
from fds.sampleapi.models.order import Order
from fds.sampleapi.models.pet import Pet
from fds.sampleapi.models.tag import Tag
from fds.sampleapi.models.user import User

