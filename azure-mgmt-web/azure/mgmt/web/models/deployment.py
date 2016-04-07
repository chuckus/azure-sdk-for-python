# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class Deployment(Resource):
    """
    Represents user crendentials used for publishing activity

    :param id: Resource Id
    :type id: str
    :param name: Resource Name
    :type name: str
    :param location: Resource Location
    :type location: str
    :param type: Resource type
    :type type: str
    :param tags: Resource tags
    :type tags: dict
    :param deployment_id: Id
    :type deployment_id: str
    :param status: Status
    :type status: int
    :param message: Message
    :type message: str
    :param author: Author
    :type author: str
    :param deployer: Deployer
    :type deployer: str
    :param author_email: AuthorEmail
    :type author_email: str
    :param start_time: StartTime
    :type start_time: datetime
    :param end_time: EndTime
    :type end_time: datetime
    :param active: Active
    :type active: bool
    :param details: Detail
    :type details: str
    """ 

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'deployment_id': {'key': 'properties.id', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'int'},
        'message': {'key': 'properties.message', 'type': 'str'},
        'author': {'key': 'properties.author', 'type': 'str'},
        'deployer': {'key': 'properties.deployer', 'type': 'str'},
        'author_email': {'key': 'properties.author_email', 'type': 'str'},
        'start_time': {'key': 'properties.start_time', 'type': 'iso-8601'},
        'end_time': {'key': 'properties.end_time', 'type': 'iso-8601'},
        'active': {'key': 'properties.active', 'type': 'bool'},
        'details': {'key': 'properties.details', 'type': 'str'},
    }

    def __init__(self, location, id=None, name=None, type=None, tags=None, deployment_id=None, status=None, message=None, author=None, deployer=None, author_email=None, start_time=None, end_time=None, active=None, details=None):
        super(Deployment, self).__init__(id=id, name=name, location=location, type=type, tags=tags)
        self.deployment_id = deployment_id
        self.status = status
        self.message = message
        self.author = author
        self.deployer = deployer
        self.author_email = author_email
        self.start_time = start_time
        self.end_time = end_time
        self.active = active
        self.details = details
