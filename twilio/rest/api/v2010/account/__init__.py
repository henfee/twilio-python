# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.api.v2010.account.address import AddressList
from twilio.rest.api.v2010.account.address import addresses
from twilio.rest.api.v2010.account.application import ApplicationList
from twilio.rest.api.v2010.account.application import applications
from twilio.rest.api.v2010.account.authorized_connect_app import AuthorizedConnectAppList
from twilio.rest.api.v2010.account.authorized_connect_app import authorized_connect_apps
from twilio.rest.api.v2010.account.available_phone_number import AvailablePhoneNumberCountryList
from twilio.rest.api.v2010.account.available_phone_number import available_phone_numbers
from twilio.rest.api.v2010.account.call import CallList
from twilio.rest.api.v2010.account.call import calls
from twilio.rest.api.v2010.account.conference import ConferenceList
from twilio.rest.api.v2010.account.conference import conferences
from twilio.rest.api.v2010.account.connect_app import ConnectAppList
from twilio.rest.api.v2010.account.connect_app import connect_apps
from twilio.rest.api.v2010.account.incoming_phone_number import IncomingPhoneNumberList
from twilio.rest.api.v2010.account.incoming_phone_number import incoming_phone_numbers
from twilio.rest.api.v2010.account.message import MessageList
from twilio.rest.api.v2010.account.message import messages
from twilio.rest.api.v2010.account.notification import NotificationList
from twilio.rest.api.v2010.account.notification import notifications
from twilio.rest.api.v2010.account.outgoing_caller_id import OutgoingCallerIdList
from twilio.rest.api.v2010.account.outgoing_caller_id import outgoing_caller_ids
from twilio.rest.api.v2010.account.queue import QueueList
from twilio.rest.api.v2010.account.queue import queues
from twilio.rest.api.v2010.account.recording import RecordingList
from twilio.rest.api.v2010.account.recording import recordings
from twilio.rest.api.v2010.account.sandbox import SandboxContext
from twilio.rest.api.v2010.account.sandbox import sandbox
from twilio.rest.api.v2010.account.sip import SipContext
from twilio.rest.api.v2010.account.sip import sip
from twilio.rest.api.v2010.account.sms import SmsContext
from twilio.rest.api.v2010.account.sms import sms
from twilio.rest.api.v2010.account.token import TokenList
from twilio.rest.api.v2010.account.token import tokens
from twilio.rest.api.v2010.account.transcription import TranscriptionList
from twilio.rest.api.v2010.account.transcription import transcriptions
from twilio.rest.api.v2010.account.usage import UsageContext
from twilio.rest.api.v2010.account.usage import usage
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class AccountList(ListResource):

    def __init__(self, version):
        """
        Initialize the AccountList
        
        :param Version version: Version that contains the resource
        
        :returns: AccountList
        :rtype: AccountList
        """
        super(AccountList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {}
        self._uri = '/Accounts.json'.format(**self._kwargs)

    def create(self, friendly_name=values.unset):
        data = values.of({
            'FriendlyName': friendly_name,
        })
        
        return self._version.create(
            AccountInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def read(self, friendly_name=values.unset, status=values.unset, limit=None,
             page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'FriendlyName': friendly_name,
            'Status': status,
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            AccountInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, friendly_name=values.unset, status=values.unset, page_token=None,
             page_number=None, page_size=None, **kwargs):
        params = values.of({
            'FriendlyName': friendly_name,
            'Status': status,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            AccountInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __call__(self, sid):
        """
        Constructs a AccountContext
        
        :param sid: Contextual sid
        
        :returns: AccountContext
        :rtype: AccountContext
        """
        return AccountContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AccountList>'


class AccountContext(InstanceContext):

    def __init__(self, version, sid):
        """
        Initialize the AccountContext
        
        :param Version version
        :param sid: Contextual sid
        
        :returns: AccountContext
        :rtype: AccountContext
        """
        super(AccountContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'sid': sid,
        }
        self._uri = '/Accounts/{sid}.json'.format(**self._kwargs)
        
        # Dependents
        self._addresses = None
        self._applications = None
        self._authorized_connect_apps = None
        self._available_phone_numbers = None
        self._calls = None
        self._conferences = None
        self._connect_apps = None
        self._incoming_phone_numbers = None
        self._messages = None
        self._notifications = None
        self._outgoing_caller_ids = None
        self._queues = None
        self._recordings = None
        self._sandbox = None
        self._sip = None
        self._sms = None
        self._tokens = None
        self._transcriptions = None
        self._usage = None

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            AccountInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def update(self, friendly_name=values.unset, status=values.unset):
        data = values.of({
            'FriendlyName': friendly_name,
            'Status': status,
        })
        
        return self._version.update(
            AccountInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    @property
    def addresses(self):
        """
        Access the addresses
        
        :returns: AddressList
        :rtype: AddressList
        """
        if self._addresses is None:
            self._addresses = AddressList(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._addresses

    @property
    def applications(self):
        """
        Access the applications
        
        :returns: ApplicationList
        :rtype: ApplicationList
        """
        if self._applications is None:
            self._applications = ApplicationList(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._applications

    @property
    def authorized_connect_apps(self):
        """
        Access the authorized_connect_apps
        
        :returns: AuthorizedConnectAppList
        :rtype: AuthorizedConnectAppList
        """
        if self._authorized_connect_apps is None:
            self._authorized_connect_apps = AuthorizedConnectAppList(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._authorized_connect_apps

    @property
    def available_phone_numbers(self):
        """
        Access the available_phone_numbers
        
        :returns: AvailablePhoneNumberCountryList
        :rtype: AvailablePhoneNumberCountryList
        """
        if self._available_phone_numbers is None:
            self._available_phone_numbers = AvailablePhoneNumberCountryList(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._available_phone_numbers

    @property
    def calls(self):
        """
        Access the calls
        
        :returns: CallList
        :rtype: CallList
        """
        if self._calls is None:
            self._calls = CallList(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._calls

    @property
    def conferences(self):
        """
        Access the conferences
        
        :returns: ConferenceList
        :rtype: ConferenceList
        """
        if self._conferences is None:
            self._conferences = ConferenceList(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._conferences

    @property
    def connect_apps(self):
        """
        Access the connect_apps
        
        :returns: ConnectAppList
        :rtype: ConnectAppList
        """
        if self._connect_apps is None:
            self._connect_apps = ConnectAppList(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._connect_apps

    @property
    def incoming_phone_numbers(self):
        """
        Access the incoming_phone_numbers
        
        :returns: IncomingPhoneNumberList
        :rtype: IncomingPhoneNumberList
        """
        if self._incoming_phone_numbers is None:
            self._incoming_phone_numbers = IncomingPhoneNumberList(
                self._version,
                owner_account_sid=self._kwargs['sid'],
            )
        return self._incoming_phone_numbers

    @property
    def messages(self):
        """
        Access the messages
        
        :returns: MessageList
        :rtype: MessageList
        """
        if self._messages is None:
            self._messages = MessageList(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._messages

    @property
    def notifications(self):
        """
        Access the notifications
        
        :returns: NotificationList
        :rtype: NotificationList
        """
        if self._notifications is None:
            self._notifications = NotificationList(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._notifications

    @property
    def outgoing_caller_ids(self):
        """
        Access the outgoing_caller_ids
        
        :returns: OutgoingCallerIdList
        :rtype: OutgoingCallerIdList
        """
        if self._outgoing_caller_ids is None:
            self._outgoing_caller_ids = OutgoingCallerIdList(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._outgoing_caller_ids

    @property
    def queues(self):
        """
        Access the queues
        
        :returns: QueueList
        :rtype: QueueList
        """
        if self._queues is None:
            self._queues = QueueList(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._queues

    @property
    def recordings(self):
        """
        Access the recordings
        
        :returns: RecordingList
        :rtype: RecordingList
        """
        if self._recordings is None:
            self._recordings = RecordingList(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._recordings

    @property
    def sandbox(self):
        """
        Access the sandbox
        
        :returns: SandboxContext
        :rtype: SandboxContext
        """
        if self._sandbox is None:
            self._sandbox = SandboxContext(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._sandbox

    @property
    def sip(self):
        """
        Access the sip
        
        :returns: SipContext
        :rtype: SipContext
        """
        if self._sip is None:
            self._sip = SipContext(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._sip

    @property
    def sms(self):
        """
        Access the sms
        
        :returns: SmsContext
        :rtype: SmsContext
        """
        if self._sms is None:
            self._sms = SmsContext(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._sms

    @property
    def tokens(self):
        """
        Access the tokens
        
        :returns: TokenList
        :rtype: TokenList
        """
        if self._tokens is None:
            self._tokens = TokenList(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._tokens

    @property
    def transcriptions(self):
        """
        Access the transcriptions
        
        :returns: TranscriptionList
        :rtype: TranscriptionList
        """
        if self._transcriptions is None:
            self._transcriptions = TranscriptionList(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._transcriptions

    @property
    def usage(self):
        """
        Access the usage
        
        :returns: UsageContext
        :rtype: UsageContext
        """
        if self._usage is None:
            self._usage = UsageContext(
                self._version,
                account_sid=self._kwargs['sid'],
            )
        return self._usage

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Api.V2010.AccountContext {}>'.format(context)


class AccountInstance(InstanceResource):

    def __init__(self, version, payload, sid=None):
        """
        Initialize the AccountInstance
        
        :returns: AccountInstance
        :rtype: AccountInstance
        """
        super(AccountInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'auth_token': payload['auth_token'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'friendly_name': payload['friendly_name'],
            'owner_account_sid': payload['owner_account_sid'],
            'sid': payload['sid'],
            'status': payload['status'],
            'subresource_uris': payload['subresource_uris'],
            'type': payload['type'],
            'uri': payload['uri'],
        }
        
        # Context
        self._instance_context = None
        self._kwargs = {
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: AccountContext for this AccountInstance
        :rtype: AccountContext
        """
        if self._instance_context is None:
            self._instance_context = AccountContext(
                self._version,
                self._kwargs['sid'],
            )
        return self._instance_context

    @property
    def auth_token(self):
        """
        :returns: The authorization token for this account
        :rtype: str
        """
        return self._properties['auth_token']

    @property
    def date_created(self):
        """
        :returns: The date this account was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this account was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def friendly_name(self):
        """
        :returns: A human readable description of this account
        :rtype: str
        """
        return self._properties['friendly_name']

    @property
    def owner_account_sid(self):
        """
        :returns: The unique 34 character id representing the parent of this account
        :rtype: str
        """
        return self._properties['owner_account_sid']

    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this resource.
        :rtype: str
        """
        return self._properties['sid']

    @property
    def status(self):
        """
        :returns: The status of this account
        :rtype: account.status
        """
        return self._properties['status']

    @property
    def subresource_uris(self):
        """
        :returns: Account Instance Subresources
        :rtype: str
        """
        return self._properties['subresource_uris']

    @property
    def type(self):
        """
        :returns: The type of this account
        :rtype: account.type
        """
        return self._properties['type']

    @property
    def uri(self):
        """
        :returns: The URI for this resource, relative to `https://api.twilio.com`
        :rtype: str
        """
        return self._properties['uri']

    def fetch(self):
        self._context.fetch()

    def update(self, friendly_name=values.unset, status=values.unset):
        self._context.update(
            friendly_name=friendly_name,
            status=status,
        )

    @property
    def addresses(self):
        """
        Access the addresses
        
        :returns: addresses
        :rtype: addresses
        """
        return self._context.addresses

    @property
    def applications(self):
        """
        Access the applications
        
        :returns: applications
        :rtype: applications
        """
        return self._context.applications

    @property
    def authorized_connect_apps(self):
        """
        Access the authorized_connect_apps
        
        :returns: authorized_connect_apps
        :rtype: authorized_connect_apps
        """
        return self._context.authorized_connect_apps

    @property
    def available_phone_numbers(self):
        """
        Access the available_phone_numbers
        
        :returns: available_phone_numbers
        :rtype: available_phone_numbers
        """
        return self._context.available_phone_numbers

    @property
    def calls(self):
        """
        Access the calls
        
        :returns: calls
        :rtype: calls
        """
        return self._context.calls

    @property
    def conferences(self):
        """
        Access the conferences
        
        :returns: conferences
        :rtype: conferences
        """
        return self._context.conferences

    @property
    def connect_apps(self):
        """
        Access the connect_apps
        
        :returns: connect_apps
        :rtype: connect_apps
        """
        return self._context.connect_apps

    @property
    def incoming_phone_numbers(self):
        """
        Access the incoming_phone_numbers
        
        :returns: incoming_phone_numbers
        :rtype: incoming_phone_numbers
        """
        return self._context.incoming_phone_numbers

    @property
    def messages(self):
        """
        Access the messages
        
        :returns: messages
        :rtype: messages
        """
        return self._context.messages

    @property
    def notifications(self):
        """
        Access the notifications
        
        :returns: notifications
        :rtype: notifications
        """
        return self._context.notifications

    @property
    def outgoing_caller_ids(self):
        """
        Access the outgoing_caller_ids
        
        :returns: outgoing_caller_ids
        :rtype: outgoing_caller_ids
        """
        return self._context.outgoing_caller_ids

    @property
    def queues(self):
        """
        Access the queues
        
        :returns: queues
        :rtype: queues
        """
        return self._context.queues

    @property
    def recordings(self):
        """
        Access the recordings
        
        :returns: recordings
        :rtype: recordings
        """
        return self._context.recordings

    @property
    def sandbox(self):
        """
        Access the sandbox
        
        :returns: sandbox
        :rtype: sandbox
        """
        return self._context.sandbox

    @property
    def sip(self):
        """
        Access the sip
        
        :returns: sip
        :rtype: sip
        """
        return self._context.sip

    @property
    def sms(self):
        """
        Access the sms
        
        :returns: sms
        :rtype: sms
        """
        return self._context.sms

    @property
    def tokens(self):
        """
        Access the tokens
        
        :returns: tokens
        :rtype: tokens
        """
        return self._context.tokens

    @property
    def transcriptions(self):
        """
        Access the transcriptions
        
        :returns: transcriptions
        :rtype: transcriptions
        """
        return self._context.transcriptions

    @property
    def usage(self):
        """
        Access the usage
        
        :returns: usage
        :rtype: usage
        """
        return self._context.usage

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Api.V2010.AccountInstance {}>'.format(context)
