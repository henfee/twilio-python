# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class ReservationList(ListResource):

    def __init__(self, version, workspace_sid, task_sid):
        """
        Initialize the ReservationList
        
        :param Version version: Version that contains the resource
        :param task_sid: Contextual task_sid
        :param workspace_sid: Contextual workspace_sid
        
        :returns: ReservationList
        :rtype: ReservationList
        """
        super(ReservationList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'workspace_sid': workspace_sid,
            'task_sid': task_sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Tasks/{task_sid}/Reservations'.format(**self._kwargs)

    def read(self, limit=None, page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            ReservationInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, page_token=None, page_number=None, page_size=None, **kwargs):
        params = values.of({
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            ReservationInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __call__(self, sid):
        """
        Constructs a ReservationContext
        
        :param sid: Contextual sid
        
        :returns: ReservationContext
        :rtype: ReservationContext
        """
        return ReservationContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.ReservationList>'


class ReservationContext(InstanceContext):

    def __init__(self, version, workspace_sid, task_sid, sid):
        """
        Initialize the ReservationContext
        
        :param Version version
        :param sid: Contextual sid
        :param task_sid: Contextual task_sid
        :param workspace_sid: Contextual workspace_sid
        
        :returns: ReservationContext
        :rtype: ReservationContext
        """
        super(ReservationContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'workspace_sid': workspace_sid,
            'task_sid': task_sid,
            'sid': sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Tasks/{task_sid}/Reservations/{sid}'.format(**self._kwargs)

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            ReservationInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def update(self, reservation_status, worker_activity_sid=values.unset):
        data = values.of({
            'ReservationStatus': reservation_status,
            'WorkerActivitySid': worker_activity_sid,
        })
        
        return self._version.update(
            ReservationInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Taskrouter.V1.ReservationContext {}>'.format(context)


class ReservationInstance(InstanceResource):

    def __init__(self, version, payload, workspace_sid, task_sid, sid=None):
        """
        Initialize the ReservationInstance
        
        :returns: ReservationInstance
        :rtype: ReservationInstance
        """
        super(ReservationInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'reservation_status': payload['reservation_status'],
            'sid': payload['sid'],
            'task_sid': payload['task_sid'],
            'worker_name': payload['worker_name'],
            'worker_sid': payload['worker_sid'],
            'workspace_sid': payload['workspace_sid'],
        }
        
        # Context
        self._instance_context = None
        self._kwargs = {
            'workspace_sid': workspace_sid,
            'task_sid': task_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: ReservationContext for this ReservationInstance
        :rtype: ReservationContext
        """
        if self._instance_context is None:
            self._instance_context = ReservationContext(
                self._version,
                self._kwargs['workspace_sid'],
                self._kwargs['task_sid'],
                self._kwargs['sid'],
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
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def reservation_status(self):
        """
        :returns: The reservation_status
        :rtype: str
        """
        return self._properties['reservation_status']

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: str
        """
        return self._properties['sid']

    @property
    def task_sid(self):
        """
        :returns: The task_sid
        :rtype: str
        """
        return self._properties['task_sid']

    @property
    def worker_name(self):
        """
        :returns: The worker_name
        :rtype: str
        """
        return self._properties['worker_name']

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

    def fetch(self):
        self._context.fetch()

    def update(self, reservation_status, worker_activity_sid=values.unset):
        self._context.update(
            reservation_status,
            worker_activity_sid=worker_activity_sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Taskrouter.V1.ReservationInstance {}>'.format(context)
