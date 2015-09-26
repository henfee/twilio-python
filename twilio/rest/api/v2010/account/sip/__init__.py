# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource


class SipContext(InstanceContext):

    def __init__(self, version):
        """
        Initialize the SipContext
        
        :param Version version
        
        :returns: SipContext
        :rtype: SipContext
        """
        super(SipContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {}
        self._uri = 'None'.format(**self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Api.V2010.SipContext {}>'.format(context)


class SipInstance(InstanceResource):

    def __init__(self, version, payload, account_sid):
        """
        Initialize the SipInstance
        
        :returns: SipInstance
        :rtype: SipInstance
        """
        super(SipInstance, self).__init__(version)
        # Context
        self._instance_context = None
        self._kwargs = {
            'account_sid': account_sid,
        }

    @property
    def _context(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: SipContext for this SipInstance
        :rtype: SipContext
        """
        if self._instance_context is None:
            self._instance_context = SipContext(
                self._version,
            )
        return self._instance_context

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Api.V2010.SipInstance {}>'.format(context)
