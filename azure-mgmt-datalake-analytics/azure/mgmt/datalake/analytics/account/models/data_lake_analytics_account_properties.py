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


class DataLakeAnalyticsAccountProperties(Model):
    """
    The account specific properties that are associated with an underlying
    Data Lake Analytics account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar provisioning_state: Gets the provisioning status of the Data Lake
     Analytics account. Possible values include: 'Failed', 'Creating',
     'Running', 'Succeeded', 'Patching', 'Suspending', 'Resuming',
     'Deleting', 'Deleted'
    :vartype provisioning_state: str or
     :class:`DataLakeAnalyticsAccountStatus <azure.mgmt.datalake.analytics.account.models.DataLakeAnalyticsAccountStatus>`
    :ivar state: Gets the state of the Data Lake Analytics account. Possible
     values include: 'active', 'suspended'
    :vartype state: str or :class:`DataLakeAnalyticsAccountState
     <azure.mgmt.datalake.analytics.account.models.DataLakeAnalyticsAccountState>`
    :param default_data_lake_store_account: Gets or sets the default data
     lake storage account associated with this Data Lake Analytics account.
    :type default_data_lake_store_account: str
    :param max_degree_of_parallelism: Gets or sets the maximum supported
     degree of parallelism for this acocunt.
    :type max_degree_of_parallelism: int
    :param max_job_count: Gets or sets the maximum supported jobs running
     under the account at the same time.
    :type max_job_count: int
    :param data_lake_store_accounts: Gets or sets the list of Data Lake
     storage accounts associated with this account.
    :type data_lake_store_accounts: list of :class:`DataLakeStoreAccountInfo
     <azure.mgmt.datalake.analytics.account.models.DataLakeStoreAccountInfo>`
    :param storage_accounts: Gets or sets the list of Azure Blob storage
     accounts associated with this account.
    :type storage_accounts: list of :class:`StorageAccountInfo
     <azure.mgmt.datalake.analytics.account.models.StorageAccountInfo>`
    :ivar creation_time: Gets or sets the account creation time.
    :vartype creation_time: datetime
    :ivar last_modified_time: Gets or sets the account last modified time.
    :vartype last_modified_time: datetime
    :ivar endpoint: Gets or sets the full CName endpoint for this account.
    :vartype endpoint: str
    """ 

    _validation = {
        'provisioning_state': {'readonly': True},
        'state': {'readonly': True},
        'creation_time': {'readonly': True},
        'last_modified_time': {'readonly': True},
        'endpoint': {'readonly': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'DataLakeAnalyticsAccountStatus'},
        'state': {'key': 'state', 'type': 'DataLakeAnalyticsAccountState'},
        'default_data_lake_store_account': {'key': 'defaultDataLakeStoreAccount', 'type': 'str'},
        'max_degree_of_parallelism': {'key': 'maxDegreeOfParallelism', 'type': 'int'},
        'max_job_count': {'key': 'maxJobCount', 'type': 'int'},
        'data_lake_store_accounts': {'key': 'dataLakeStoreAccounts', 'type': '[DataLakeStoreAccountInfo]'},
        'storage_accounts': {'key': 'storageAccounts', 'type': '[StorageAccountInfo]'},
        'creation_time': {'key': 'creationTime', 'type': 'iso-8601'},
        'last_modified_time': {'key': 'lastModifiedTime', 'type': 'iso-8601'},
        'endpoint': {'key': 'endpoint', 'type': 'str'},
    }

    def __init__(self, default_data_lake_store_account=None, max_degree_of_parallelism=None, max_job_count=None, data_lake_store_accounts=None, storage_accounts=None):
        self.provisioning_state = None
        self.state = None
        self.default_data_lake_store_account = default_data_lake_store_account
        self.max_degree_of_parallelism = max_degree_of_parallelism
        self.max_job_count = max_job_count
        self.data_lake_store_accounts = data_lake_store_accounts
        self.storage_accounts = storage_accounts
        self.creation_time = None
        self.last_modified_time = None
        self.endpoint = None
