# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.job_collections_operations import JobCollectionsOperations
from .operations.jobs_operations import JobsOperations
from . import models
from .patch import patch_client


class SchedulerManagementClientConfiguration(AzureConfiguration):
    """Configuration for SchedulerManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(SchedulerManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-scheduler/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class SchedulerManagementClient(SDKClient):
    """SchedulerManagementClient

    :ivar config: Configuration for client.
    :vartype config: SchedulerManagementClientConfiguration

    :ivar job_collections: JobCollections operations
    :vartype job_collections: azure.mgmt.scheduler.operations.JobCollectionsOperations
    :ivar jobs: Jobs operations
    :vartype jobs: azure.mgmt.scheduler.operations.JobsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = SchedulerManagementClientConfiguration(credentials, subscription_id, base_url)
        super(SchedulerManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2016-03-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.job_collections = JobCollectionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.jobs = JobsOperations(
            self._client, self.config, self._serialize, self._deserialize)

        patch_client(self)