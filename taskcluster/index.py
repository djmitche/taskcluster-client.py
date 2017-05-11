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


class Index(BaseClient):
    """
    The task index, typically available at `index.taskcluster.net`, is
    responsible for indexing tasks. The service ensures that tasks can be
    located by recency and/or arbitrary strings. Common use-cases include:

     * Locate tasks by git or mercurial `<revision>`, or
     * Locate latest task from given `<branch>`, such as a release.

    **Index hierarchy**, tasks are indexed in a dot (`.`) separated hierarchy
    called a namespace. For example a task could be indexed with the index path
    `some-app.<revision>.linux-64.release-build`. In this case the following
    namespaces is created.

     1. `some-app`,
     1. `some-app.<revision>`, and,
     2. `some-app.<revision>.linux-64`

    Inside the namespace `some-app.<revision>` you can find the namespace
    `some-app.<revision>.linux-64` inside which you can find the indexed task
    `some-app.<revision>.linux-64.release-build`. This is an example of indexing
    builds for a given platform and revision.

    **Task Rank**, when a task is indexed, it is assigned a `rank` (defaults
    to `0`). If another task is already indexed in the same namespace with
    lower or equal `rank`, the index for that task will be overwritten. For example
    consider index path `mozilla-central.linux-64.release-build`. In
    this case one might choose to use a UNIX timestamp or mercurial revision
    number as `rank`. This way the latest completed linux 64 bit release
    build is always available at `mozilla-central.linux-64.release-build`.

    Note that this does mean index paths are not immutable: the same path may
    point to a different task now than it did a moment ago.

    **Indexed Data**, when a task is retrieved from the index the result includes
    a `taskId` and an additional user-defined JSON blob that was indexed with
    the task.

    **Entry Expiration**, all indexed entries must have an expiration date.
    Typically this defaults to one year, if not specified. If you are
    indexing tasks to make it easy to find artifacts, consider using the
    artifact's expiration date.

    **Valid Characters**, all keys in a namespace `<key1>.<key2>` must be
    in the form `/[a-zA-Z0-9_!~*'()%-]+/`. Observe that this is URL-safe and
    that if you strictly want to put another character you can URL encode it.

    **Indexing Routes**, tasks can be indexed using the API below, but the
    most common way to index tasks is adding a custom route to `task.routes` of the
    form `index.<namespace>`. In order to add this route to a task you'll
    need the scope `queue:route:index.<namespace>`. When a task has
    this route, it will be indexed when the task is **completed successfully**.
    The task will be indexed with `rank`, `data` and `expires` as specified
    in `task.extra.index`. See the example below:

    ```
    {
      payload:  { /* ... */ },
      routes: [
        // index.<namespace> prefixed routes, tasks CC'ed such a route will
        // be indexed under the given <namespace>
        "index.mozilla-central.linux-64.release-build",
        "index.<revision>.linux-64.release-build"
      ],
      extra: {
        // Optional details for indexing service
        index: {
          // Ordering, this taskId will overwrite any thing that has
          // rank <= 4000 (defaults to zero)
          rank:       4000,

          // Specify when the entries expire (Defaults to 1 year)
          expires:          new Date().toJSON(),

          // A little informal data to store along with taskId
          // (less 16 kb when encoded as JSON)
          data: {
            hgRevision:   "...",
            commitMessae: "...",
            whatever...
          }
        },
        // Extra properties for other services...
      }
      // Other task properties...
    }
    ```

    **Remark**, when indexing tasks using custom routes, it's also possible
    to listen for messages about these tasks. For
    example one could bind to `route.index.some-app.*.release-build`,
    and pick up all messages about release builds. Hence, it is a
    good idea to document task index hierarchies, as these make up extension
    points in their own.
    """

    classOptions = {
        "baseUrl": "https://index.taskcluster.net/v1"
    }

    def findTask(self, *args, **kwargs):
        """
        Find Indexed Task

        Find a task by index path, returning the highest-rank task with that path. If no
        task exists for the given path, this API end-point will respond with a 404 status.

        This method takes output: ``http://schemas.taskcluster.net/index/v1/indexed-task-response.json#``

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["findTask"], *args, **kwargs)

    def listNamespaces(self, *args, **kwargs):
        """
        List Namespaces

        List the namespaces immediately under a given namespace.

        This endpoint
        lists up to 1000 namespaces. If more namespaces are present, a
        `continuationToken` will be returned, which can be given in the next
        request. For the initial request, the payload should be an empty JSON
        object.

        This method takes input: ``http://schemas.taskcluster.net/index/v1/list-namespaces-request.json#``

        This method takes output: ``http://schemas.taskcluster.net/index/v1/list-namespaces-response.json#``

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["listNamespaces"], *args, **kwargs)

    def listTasks(self, *args, **kwargs):
        """
        List Tasks

        List the tasks immediately under a given namespace.

        This endpoint
        lists up to 1000 tasks. If more tasks are present, a
        `continuationToken` will be returned, which can be given in the next
        request. For the initial request, the payload should be an empty JSON
        object.

        **Remark**, this end-point is designed for humans browsing for tasks, not
        services, as that makes little sense.

        This method takes input: ``http://schemas.taskcluster.net/index/v1/list-tasks-request.json#``

        This method takes output: ``http://schemas.taskcluster.net/index/v1/list-tasks-response.json#``

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["listTasks"], *args, **kwargs)

    def insertTask(self, *args, **kwargs):
        """
        Insert Task into Index

        Insert a task into the index.  If the new rank is less than the existing rank
        at the given index path, the task is not indexed but the response is still 200 OK.

        Please see the introduction above for information
        about indexing successfully completed tasks automatically using custom routes.

        This method takes input: ``http://schemas.taskcluster.net/index/v1/insert-task-request.json#``

        This method takes output: ``http://schemas.taskcluster.net/index/v1/indexed-task-response.json#``

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["insertTask"], *args, **kwargs)

    def findArtifactFromTask(self, *args, **kwargs):
        """
        Get Artifact From Indexed Task

        Find a task by index path and redirect to the artifact on the most recent
        run with the given `name`.

        Note that multiple calls to this endpoint may return artifacts from differen tasks
        if a new task is inserted into the index between calls. Avoid using this method as
        a stable link to multiple, connected files if the index path does not contain a
        unique identifier.  For example, the following two links may return unrelated files:
        * https://index.taskcluster.net/task/some-app.win64.latest.installer/artifacts/public/installer.exe`
        * https://index.taskcluster.net/task/some-app.win64.latest.installer/artifacts/public/debug-symbols.zip`

        This problem be remedied by including the revision in the index path or by bundling both
        installer and debug symbols into a single artifact.

        If no task exists for the given index path, this API end-point responds with 404.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["findArtifactFromTask"], *args, **kwargs)

    def ping(self, *args, **kwargs):
        """
        Ping Server

        Respond without doing anything.
        This endpoint is used to check that the service is up.

        This method is ``stable``
        """

        return self._makeApiCall(self.funcinfo["ping"], *args, **kwargs)

    funcinfo = {
        "findArtifactFromTask": {           'args': ['indexPath', 'name'],
            'method': 'get',
            'name': 'findArtifactFromTask',
            'route': '/task/<indexPath>/artifacts/<name>',
            'stability': 'stable'},
        "findTask": {           'args': ['indexPath'],
            'method': 'get',
            'name': 'findTask',
            'output': 'http://schemas.taskcluster.net/index/v1/indexed-task-response.json#',
            'route': '/task/<indexPath>',
            'stability': 'stable'},
        "insertTask": {           'args': ['namespace'],
            'input': 'http://schemas.taskcluster.net/index/v1/insert-task-request.json#',
            'method': 'put',
            'name': 'insertTask',
            'output': 'http://schemas.taskcluster.net/index/v1/indexed-task-response.json#',
            'route': '/task/<namespace>',
            'stability': 'stable'},
        "listNamespaces": {           'args': ['namespace'],
            'input': 'http://schemas.taskcluster.net/index/v1/list-namespaces-request.json#',
            'method': 'post',
            'name': 'listNamespaces',
            'output': 'http://schemas.taskcluster.net/index/v1/list-namespaces-response.json#',
            'route': '/namespaces/<namespace>',
            'stability': 'stable'},
        "listTasks": {           'args': ['namespace'],
            'input': 'http://schemas.taskcluster.net/index/v1/list-tasks-request.json#',
            'method': 'post',
            'name': 'listTasks',
            'output': 'http://schemas.taskcluster.net/index/v1/list-tasks-response.json#',
            'route': '/tasks/<namespace>',
            'stability': 'stable'},
        "ping": {           'args': [],
            'method': 'get',
            'name': 'ping',
            'route': '/ping',
            'stability': 'stable'},
    }


__all__ = ['createTemporaryCredentials', 'config', '_defaultConfig', 'createApiClient', 'createSession', 'Index']