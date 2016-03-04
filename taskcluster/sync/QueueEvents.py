#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
'''
Queue AMQP Exchanges
'''
from __future__ import absolute_import, division, print_function

import logging
from taskcluster.sync.syncclient import SyncClient

log = logging.getLogger(__name__)


class QueueEvents(SyncClient):
    '''
    Queue AMQP Exchanges
    The queue, typically available at `queue.taskcluster.net`, is responsible
    for accepting tasks and track their state as they are executed by
    workers. In order ensure they are eventually resolved.

    This document describes AMQP exchanges offered by the queue, which allows
    third-party listeners to monitor tasks as they progress to resolution.
    These exchanges targets the following audience:
     * Schedulers, who takes action after tasks are completed,
     * Workers, who wants to listen for new or canceled tasks (optional),
     * Tools, that wants to update their view as task progress.

    You'll notice that all the exchanges in the document shares the same
    routing key pattern. This makes it very easy to bind to all messages
    about a certain kind tasks.

    **Task-graphs**, if the task-graph scheduler, documented elsewhere, is
    used to schedule a task-graph, the task submitted will have their
    `schedulerId` set to `'task-graph-scheduler'`, and their `taskGroupId` to
    the `taskGraphId` as given to the task-graph scheduler. This is useful if
    you wish to listen for all messages in a specific task-graph.

    **Task specific routes**, a task can define a task specific route using
    the `task.routes` property. See task creation documentation for details
    on permissions required to provide task specific routes. If a task has
    the entry `'notify.by-email'` in as task specific route defined in
    `task.routes` all messages about this task will be CC'ed with the
    routing-key `'route.notify.by-email'`.

    These routes will always be prefixed `route.`, so that cannot interfere
    with the _primary_ routing key as documented here. Notice that the
    _primary_ routing key is alwasys prefixed `primary.`. This is ensured
    in the routing key reference, so API clients will do this automatically.

    Please, note that the way RabbitMQ works, the message will only arrive
    in your queue once, even though you may have bound to the exchange with
    multiple routing key patterns that matches more of the CC'ed routing
    routing keys.

    **Delivery guarantees**, most operations on the queue are idempotent,
    which means that if repeated with the same arguments then the requests
    will ensure completion of the operation and return the same response.
    This is useful if the server crashes or the TCP connection breaks, but
    when re-executing an idempotent operation, the queue will also resend
    any related AMQP messages. Hence, messages may be repeated.

    This shouldn't be much of a problem, as the best you can achieve using
    confirm messages with AMQP is at-least-once delivery semantics. Hence,
    this only prevents you from obtaining at-most-once delivery semantics.

    **Remark**, some message generated by timeouts maybe dropped if the
    server crashes at wrong time. Ideally, we'll address this in the
    future. For now we suggest you ignore this corner case, and notify us
    if this corner case is of concern to you.
    '''
    version = 0
    referenceUrl = 'http://references.taskcluster.net/queue/v1/exchanges.json'
    routingKeys = {
        'taskDefined': [
            {
                'constant': 'primary',
                'multipleWords': False,
                'name': 'routingKeyKind',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'taskId',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'runId',
                'required': False,
            },
            {
                'multipleWords': False,
                'name': 'workerGroup',
                'required': False,
            },
            {
                'multipleWords': False,
                'name': 'workerId',
                'required': False,
            },
            {
                'multipleWords': False,
                'name': 'provisionerId',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'workerType',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'schedulerId',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'taskGroupId',
                'required': True,
            },
            {
                'multipleWords': True,
                'name': 'reserved',
                'required': False,
            },
        ],
        'taskPending': [
            {
                'constant': 'primary',
                'multipleWords': False,
                'name': 'routingKeyKind',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'taskId',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'runId',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'workerGroup',
                'required': False,
            },
            {
                'multipleWords': False,
                'name': 'workerId',
                'required': False,
            },
            {
                'multipleWords': False,
                'name': 'provisionerId',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'workerType',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'schedulerId',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'taskGroupId',
                'required': True,
            },
            {
                'multipleWords': True,
                'name': 'reserved',
                'required': False,
            },
        ],
        'taskRunning': [
            {
                'constant': 'primary',
                'multipleWords': False,
                'name': 'routingKeyKind',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'taskId',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'runId',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'workerGroup',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'workerId',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'provisionerId',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'workerType',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'schedulerId',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'taskGroupId',
                'required': True,
            },
            {
                'multipleWords': True,
                'name': 'reserved',
                'required': False,
            },
        ],
        'artifactCreated': [
            {
                'constant': 'primary',
                'multipleWords': False,
                'name': 'routingKeyKind',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'taskId',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'runId',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'workerGroup',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'workerId',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'provisionerId',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'workerType',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'schedulerId',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'taskGroupId',
                'required': True,
            },
            {
                'multipleWords': True,
                'name': 'reserved',
                'required': False,
            },
        ],
        'taskCompleted': [
            {
                'constant': 'primary',
                'multipleWords': False,
                'name': 'routingKeyKind',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'taskId',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'runId',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'workerGroup',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'workerId',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'provisionerId',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'workerType',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'schedulerId',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'taskGroupId',
                'required': True,
            },
            {
                'multipleWords': True,
                'name': 'reserved',
                'required': False,
            },
        ],
        'taskFailed': [
            {
                'constant': 'primary',
                'multipleWords': False,
                'name': 'routingKeyKind',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'taskId',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'runId',
                'required': False,
            },
            {
                'multipleWords': False,
                'name': 'workerGroup',
                'required': False,
            },
            {
                'multipleWords': False,
                'name': 'workerId',
                'required': False,
            },
            {
                'multipleWords': False,
                'name': 'provisionerId',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'workerType',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'schedulerId',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'taskGroupId',
                'required': True,
            },
            {
                'multipleWords': True,
                'name': 'reserved',
                'required': False,
            },
        ],
        'taskException': [
            {
                'constant': 'primary',
                'multipleWords': False,
                'name': 'routingKeyKind',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'taskId',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'runId',
                'required': False,
            },
            {
                'multipleWords': False,
                'name': 'workerGroup',
                'required': False,
            },
            {
                'multipleWords': False,
                'name': 'workerId',
                'required': False,
            },
            {
                'multipleWords': False,
                'name': 'provisionerId',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'workerType',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'schedulerId',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'taskGroupId',
                'required': True,
            },
            {
                'multipleWords': True,
                'name': 'reserved',
                'required': False,
            },
        ],
    }

    def __init__(self, *args, **kwargs):
        self.classOptions = {}
        self.classOptions['exchangePrefix'] = 'exchange/taskcluster-queue/v1/'
        super(QueueEvents, self).__init__(*args, **kwargs)

    def taskDefined(self, routingKeyPattern=None):
        '''
        Task Defined Messages

        When a task is created or just defined a message is posted to this
        exchange.

        This message exchange is mainly useful when tasks are scheduled by a
        scheduler that uses `defineTask` as this does not make the task
        `pending`. Thus, no `taskPending` message is published.
        Please, note that messages are also published on this exchange if defined
        using `createTask`.

        Generate a routing key pattern for the task-defined exchange.
        This method takes a given routing key as a string or a dictionary.  For each given
        dictionary key, the corresponding routing key token takes its value.  For routing key
        tokens which are not specified by the dictionary, the * or # character is used depending
        on whether or not the key allows multiple words.

        This exchange takes the following keys:
        - ``routingKeyKind``
        - ``taskId``
        - ``runId``
        - ``workerGroup``
        - ``workerId``
        - ``provisionerId``
        - ``workerType``
        - ``schedulerId``
        - ``taskGroupId``
        - ``reserved``
        '''
        exchangeUrl = '%s/%s' % (self.options['exchangePrefix'].rstrip('/'),
                                 "task-defined".lstrip('/'))
        return self._makeTopicExchange(
            exchangeUrl,
            self.routingKeys['taskDefined'],
            routingKeyPattern
        )

    def taskPending(self, routingKeyPattern=None):
        '''
        Task Pending Messages

        When a task becomes `pending` a message is posted to this exchange.

        This is useful for workers who doesn't want to constantly poll the queue
        for new tasks. The queue will also be authority for task states and
        claims. But using this exchange workers should be able to distribute work
        efficiently and they would be able to reduce their polling interval
        significantly without affecting general responsiveness.

        Generate a routing key pattern for the task-pending exchange.
        This method takes a given routing key as a string or a dictionary.  For each given
        dictionary key, the corresponding routing key token takes its value.  For routing key
        tokens which are not specified by the dictionary, the * or # character is used depending
        on whether or not the key allows multiple words.

        This exchange takes the following keys:
        - ``routingKeyKind``
        - ``taskId``
        - ``runId``
        - ``workerGroup``
        - ``workerId``
        - ``provisionerId``
        - ``workerType``
        - ``schedulerId``
        - ``taskGroupId``
        - ``reserved``
        '''
        exchangeUrl = '%s/%s' % (self.options['exchangePrefix'].rstrip('/'),
                                 "task-pending".lstrip('/'))
        return self._makeTopicExchange(
            exchangeUrl,
            self.routingKeys['taskPending'],
            routingKeyPattern
        )

    def taskRunning(self, routingKeyPattern=None):
        '''
        Task Running Messages

        Whenever a task is claimed by a worker, a run is started on the worker,
        and a message is posted on this exchange.

        Generate a routing key pattern for the task-running exchange.
        This method takes a given routing key as a string or a dictionary.  For each given
        dictionary key, the corresponding routing key token takes its value.  For routing key
        tokens which are not specified by the dictionary, the * or # character is used depending
        on whether or not the key allows multiple words.

        This exchange takes the following keys:
        - ``routingKeyKind``
        - ``taskId``
        - ``runId``
        - ``workerGroup``
        - ``workerId``
        - ``provisionerId``
        - ``workerType``
        - ``schedulerId``
        - ``taskGroupId``
        - ``reserved``
        '''
        exchangeUrl = '%s/%s' % (self.options['exchangePrefix'].rstrip('/'),
                                 "task-running".lstrip('/'))
        return self._makeTopicExchange(
            exchangeUrl,
            self.routingKeys['taskRunning'],
            routingKeyPattern
        )

    def artifactCreated(self, routingKeyPattern=None):
        '''
        Artifact Creation Messages

        Whenever the `createArtifact` end-point is called, the queue will create
        a record of the artifact and post a message on this exchange. All of this
        happens before the queue returns a signed URL for the caller to upload
        the actual artifact with (pending on `storageType`).

        This means that the actual artifact is rarely available when this message
        is posted. But it is not unreasonable to assume that the artifact will
        will become available at some point later. Most signatures will expire in
        30 minutes or so, forcing the uploader to call `createArtifact` with
        the same payload again in-order to continue uploading the artifact.

        However, in most cases (especially for small artifacts) it's very
        reasonable assume the artifact will be available within a few minutes.
        This property means that this exchange is mostly useful for tools
        monitoring task evaluation. One could also use it count number of
        artifacts per task, or _index_ artifacts though in most cases it'll be
        smarter to index artifacts after the task in question have completed
        successfully.

        Generate a routing key pattern for the artifact-created exchange.
        This method takes a given routing key as a string or a dictionary.  For each given
        dictionary key, the corresponding routing key token takes its value.  For routing key
        tokens which are not specified by the dictionary, the * or # character is used depending
        on whether or not the key allows multiple words.

        This exchange takes the following keys:
        - ``routingKeyKind``
        - ``taskId``
        - ``runId``
        - ``workerGroup``
        - ``workerId``
        - ``provisionerId``
        - ``workerType``
        - ``schedulerId``
        - ``taskGroupId``
        - ``reserved``
        '''
        exchangeUrl = '%s/%s' % (self.options['exchangePrefix'].rstrip('/'),
                                 "artifact-created".lstrip('/'))
        return self._makeTopicExchange(
            exchangeUrl,
            self.routingKeys['artifactCreated'],
            routingKeyPattern
        )

    def taskCompleted(self, routingKeyPattern=None):
        '''
        Task Completed Messages

        When a task is successfully completed by a worker a message is posted
        this exchange.
        This message is routed using the `runId`, `workerGroup` and `workerId`
        that completed the task. But information about additional runs is also
        available from the task status structure.

        Generate a routing key pattern for the task-completed exchange.
        This method takes a given routing key as a string or a dictionary.  For each given
        dictionary key, the corresponding routing key token takes its value.  For routing key
        tokens which are not specified by the dictionary, the * or # character is used depending
        on whether or not the key allows multiple words.

        This exchange takes the following keys:
        - ``routingKeyKind``
        - ``taskId``
        - ``runId``
        - ``workerGroup``
        - ``workerId``
        - ``provisionerId``
        - ``workerType``
        - ``schedulerId``
        - ``taskGroupId``
        - ``reserved``
        '''
        exchangeUrl = '%s/%s' % (self.options['exchangePrefix'].rstrip('/'),
                                 "task-completed".lstrip('/'))
        return self._makeTopicExchange(
            exchangeUrl,
            self.routingKeys['taskCompleted'],
            routingKeyPattern
        )

    def taskFailed(self, routingKeyPattern=None):
        '''
        Task Failed Messages

        When a task ran, but failed to complete successfully a message is posted
        to this exchange. This is same as worker ran task-specific code, but the
        task specific code exited non-zero.

        Generate a routing key pattern for the task-failed exchange.
        This method takes a given routing key as a string or a dictionary.  For each given
        dictionary key, the corresponding routing key token takes its value.  For routing key
        tokens which are not specified by the dictionary, the * or # character is used depending
        on whether or not the key allows multiple words.

        This exchange takes the following keys:
        - ``routingKeyKind``
        - ``taskId``
        - ``runId``
        - ``workerGroup``
        - ``workerId``
        - ``provisionerId``
        - ``workerType``
        - ``schedulerId``
        - ``taskGroupId``
        - ``reserved``
        '''
        exchangeUrl = '%s/%s' % (self.options['exchangePrefix'].rstrip('/'),
                                 "task-failed".lstrip('/'))
        return self._makeTopicExchange(
            exchangeUrl,
            self.routingKeys['taskFailed'],
            routingKeyPattern
        )

    def taskException(self, routingKeyPattern=None):
        '''
        Task Exception Messages

        Whenever TaskCluster fails to run a message is posted to this exchange.
        This happens if the task isn't completed before its `deadlìne`,
        all retries failed (i.e. workers stopped responding), the task was
        canceled by another entity, or the task carried a malformed payload.

        The specific _reason_ is evident from that task status structure, refer
        to the `reasonResolved` property for the last run.

        Generate a routing key pattern for the task-exception exchange.
        This method takes a given routing key as a string or a dictionary.  For each given
        dictionary key, the corresponding routing key token takes its value.  For routing key
        tokens which are not specified by the dictionary, the * or # character is used depending
        on whether or not the key allows multiple words.

        This exchange takes the following keys:
        - ``routingKeyKind``
        - ``taskId``
        - ``runId``
        - ``workerGroup``
        - ``workerId``
        - ``provisionerId``
        - ``workerType``
        - ``schedulerId``
        - ``taskGroupId``
        - ``reserved``
        '''
        exchangeUrl = '%s/%s' % (self.options['exchangePrefix'].rstrip('/'),
                                 "task-exception".lstrip('/'))
        return self._makeTopicExchange(
            exchangeUrl,
            self.routingKeys['taskException'],
            routingKeyPattern
        )
