# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource


class StatisticsContext(InstanceContext):

    def __init__(self, version, workspace_sid, task_queue_sid):
        """
        Initialize the StatisticsContext
        
        :param Version version
        :param task_queue_sid: Contextual task_queue_sid
        :param workspace_sid: Contextual workspace_sid
        
        :returns: StatisticsContext
        :rtype: StatisticsContext
        """
        super(StatisticsContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'workspace_sid': workspace_sid,
            'task_queue_sid': task_queue_sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/TaskQueues/{task_queue_sid}/Statistics'.format(**self._kwargs)

    def fetch(self, end_date=values.unset, friendly_name=values.unset,
              minutes=values.unset, start_date=values.unset):
        params = values.of({
            'EndDate': end_date,
            'FriendlyName': friendly_name,
            'Minutes': minutes,
            'StartDate': start_date,
        })
        
        return self._version.fetch(
            StatisticsInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Taskrouter.V1.StatisticsContext {}>'.format(context)


class StatisticsInstance(InstanceResource):

    def __init__(self, version, payload, workspace_sid=None, task_queue_sid=None):
        """
        Initialize the StatisticsInstance
        
        :returns: StatisticsInstance
        :rtype: StatisticsInstance
        """
        super(StatisticsInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'cumulative': payload['cumulative'],
            'realtime': payload['realtime'],
            'task_queue_sid': payload['task_queue_sid'],
            'worker_sid': payload['worker_sid'],
            'workspace_sid': payload['workspace_sid'],
        }
        
        # Context
        self._instance_context = None
        self._kwargs = {
            'workspace_sid': workspace_sid or self._properties['workspace_sid'],
            'task_queue_sid': task_queue_sid or self._properties['task_queue_sid'],
        }

    @property
    def _context(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: StatisticsContext for this StatisticsInstance
        :rtype: StatisticsContext
        """
        if self._instance_context is None:
            self._instance_context = StatisticsContext(
                self._version,
                self._kwargs['workspace_sid'],
                self._kwargs['task_queue_sid'],
            )
        return self._instance_context

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: str
        """
        return self._properties['account_sid']

    @property
    def cumulative(self):
        """
        :returns: The cumulative
        :rtype: str
        """
        return self._properties['cumulative']

    @property
    def realtime(self):
        """
        :returns: The realtime
        :rtype: str
        """
        return self._properties['realtime']

    @property
    def task_queue_sid(self):
        """
        :returns: The task_queue_sid
        :rtype: str
        """
        return self._properties['task_queue_sid']

    @property
    def worker_sid(self):
        """
        :returns: The worker_sid
        :rtype: str
        """
        return self._properties['worker_sid']

    @property
    def workspace_sid(self):
        """
        :returns: The workspace_sid
        :rtype: str
        """
        return self._properties['workspace_sid']

    def fetch(self, end_date=values.unset, friendly_name=values.unset,
              minutes=values.unset, start_date=values.unset):
        self._context.fetch(
            end_date=end_date,
            friendly_name=friendly_name,
            minutes=minutes,
            start_date=start_date,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Taskrouter.V1.StatisticsInstance {}>'.format(context)
