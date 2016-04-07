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

from msrest.serialization import Model


class JobDefinition(Model):
    """JobDefinition

    :param id: Gets the job resource identifier.
    :type id: str
    :param type: Gets the job resource type.
    :type type: str
    :param name: Gets the job resource name.
    :type name: str
    :param properties: Gets or sets the job properties.
    :type properties: :class:`JobProperties
     <azure.mgmt.scheduler.models.JobProperties>`
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'JobProperties'},
    }

    def __init__(self, id=None, type=None, name=None, properties=None):
        self.id = id
        self.type = type
        self.name = name
        self.properties = properties
