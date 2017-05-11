# coding=utf-8
#####################################################
# THIS FILE IS AUTOMATICALLY GENERATED. DO NOT EDIT #
#####################################################
# noqa: E128,E201
from .client import BaseClient
from .client import createApiClient
from .client import config
from .client import createTemporaryCredentials
from .client import createSession
_defaultConfig = config


class GithubEvents(BaseClient):
    """
    The github service, typically available at
    `github.taskcluster.net`, is responsible for publishing a pulse
    message for supported github events.

    This document describes the exchange offered by the taskcluster
    github service
    """

    classOptions = {
        "exchangePrefix": "exchange/taskcluster-github/v1/"
    }

    """
    GitHub Pull Request Event

    When a GitHub pull request event is posted it will be broadcast on this
    exchange with the designated `organization` and `repository`
    in the routing-key along with event specific metadata in the payload.

    This exchange outputs: ``http://schemas.taskcluster.net/github/v1/github-pull-request-message.json#``This exchange takes the following keys:

     * routingKeyKind: Identifier for the routing-key kind. This is always `"primary"` for the formalized routing key. (required)

     * organization: The GitHub `organization` which had an event. All periods have been replaced by % - such that foo.bar becomes foo%bar - and all other special characters aside from - and _ have been stripped. (required)

     * repository: The GitHub `repository` which had an event.All periods have been replaced by % - such that foo.bar becomes foo%bar - and all other special characters aside from - and _ have been stripped. (required)

     * action: The GitHub `action` which triggered an event. See for possible values see the payload actions property. (required)
    """

    def pullRequest(self, *args, **kwargs):
        return self._makeTopicExchange({'schema': 'http://schemas.taskcluster.net/github/v1/github-pull-request-message.json#', 'exchange': 'pull-request', 'name': 'pullRequest', 'routingKey': [{'constant': 'primary', 'multipleWords': False, 'name': 'routingKeyKind', 'required': True, 'summary': 'Identifier for the routing-key kind. This is always `"primary"` for the formalized routing key.'}, {'multipleWords': False, 'name': 'organization', 'required': True, 'summary': 'The GitHub `organization` which had an event. All periods have been replaced by % - such that foo.bar becomes foo%bar - and all other special characters aside from - and _ have been stripped.'}, {'multipleWords': False, 'name': 'repository', 'required': True, 'summary': 'The GitHub `repository` which had an event.All periods have been replaced by % - such that foo.bar becomes foo%bar - and all other special characters aside from - and _ have been stripped.'}, {'multipleWords': False, 'name': 'action', 'required': True, 'summary': 'The GitHub `action` which triggered an event. See for possible values see the payload actions property.'}]}, *args, **kwargs)

    """
    GitHub push Event

    When a GitHub push event is posted it will be broadcast on this
    exchange with the designated `organization` and `repository`
    in the routing-key along with event specific metadata in the payload.

    This exchange outputs: ``http://schemas.taskcluster.net/github/v1/github-push-message.json#``This exchange takes the following keys:

     * routingKeyKind: Identifier for the routing-key kind. This is always `"primary"` for the formalized routing key. (required)

     * organization: The GitHub `organization` which had an event. All periods have been replaced by % - such that foo.bar becomes foo%bar - and all other special characters aside from - and _ have been stripped. (required)

     * repository: The GitHub `repository` which had an event.All periods have been replaced by % - such that foo.bar becomes foo%bar - and all other special characters aside from - and _ have been stripped. (required)
    """

    def push(self, *args, **kwargs):
        return self._makeTopicExchange({'schema': 'http://schemas.taskcluster.net/github/v1/github-push-message.json#', 'exchange': 'push', 'name': 'push', 'routingKey': [{'constant': 'primary', 'multipleWords': False, 'name': 'routingKeyKind', 'required': True, 'summary': 'Identifier for the routing-key kind. This is always `"primary"` for the formalized routing key.'}, {'multipleWords': False, 'name': 'organization', 'required': True, 'summary': 'The GitHub `organization` which had an event. All periods have been replaced by % - such that foo.bar becomes foo%bar - and all other special characters aside from - and _ have been stripped.'}, {'multipleWords': False, 'name': 'repository', 'required': True, 'summary': 'The GitHub `repository` which had an event.All periods have been replaced by % - such that foo.bar becomes foo%bar - and all other special characters aside from - and _ have been stripped.'}]}, *args, **kwargs)

    """
    GitHub release Event

    When a GitHub release event is posted it will be broadcast on this
    exchange with the designated `organization` and `repository`
    in the routing-key along with event specific metadata in the payload.

    This exchange outputs: ``http://schemas.taskcluster.net/github/v1/github-release-message.json#``This exchange takes the following keys:

     * routingKeyKind: Identifier for the routing-key kind. This is always `"primary"` for the formalized routing key. (required)

     * organization: The GitHub `organization` which had an event. All periods have been replaced by % - such that foo.bar becomes foo%bar - and all other special characters aside from - and _ have been stripped. (required)

     * repository: The GitHub `repository` which had an event.All periods have been replaced by % - such that foo.bar becomes foo%bar - and all other special characters aside from - and _ have been stripped. (required)
    """

    def release(self, *args, **kwargs):
        return self._makeTopicExchange({'schema': 'http://schemas.taskcluster.net/github/v1/github-release-message.json#', 'exchange': 'release', 'name': 'release', 'routingKey': [{'constant': 'primary', 'multipleWords': False, 'name': 'routingKeyKind', 'required': True, 'summary': 'Identifier for the routing-key kind. This is always `"primary"` for the formalized routing key.'}, {'multipleWords': False, 'name': 'organization', 'required': True, 'summary': 'The GitHub `organization` which had an event. All periods have been replaced by % - such that foo.bar becomes foo%bar - and all other special characters aside from - and _ have been stripped.'}, {'multipleWords': False, 'name': 'repository', 'required': True, 'summary': 'The GitHub `repository` which had an event.All periods have been replaced by % - such that foo.bar becomes foo%bar - and all other special characters aside from - and _ have been stripped.'}]}, *args, **kwargs)

    funcinfo = {
    }


__all__ = ['createTemporaryCredentials', 'config', '_defaultConfig', 'createApiClient', 'createSession', 'GithubEvents']