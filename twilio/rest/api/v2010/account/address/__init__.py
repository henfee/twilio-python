# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.api.v2010.account.address.dependent_phone_number import DependentPhoneNumberList
from twilio.rest.api.v2010.account.address.dependent_phone_number import dependent_phone_numbers
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class AddressList(ListResource):

    def __init__(self, version, account_sid):
        """
        Initialize the AddressList
        
        :param Version version: Version that contains the resource
        :param account_sid: Contextual account_sid
        
        :returns: AddressList
        :rtype: AddressList
        """
        super(AddressList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
        }
        self._uri = '/Accounts/{account_sid}/Addresses.json'.format(**self._kwargs)

    def create(self, customer_name, street, city, region, postal_code, iso_country,
               friendly_name=values.unset):
        data = values.of({
            'CustomerName': customer_name,
            'Street': street,
            'City': city,
            'Region': region,
            'PostalCode': postal_code,
            'IsoCountry': iso_country,
            'FriendlyName': friendly_name,
        })
        
        return self._version.create(
            AddressInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def read(self, customer_name=values.unset, friendly_name=values.unset,
             iso_country=values.unset, limit=None, page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'CustomerName': customer_name,
            'FriendlyName': friendly_name,
            'IsoCountry': iso_country,
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            AddressInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, customer_name=values.unset, friendly_name=values.unset,
             iso_country=values.unset, page_token=None, page_number=None,
             page_size=None, **kwargs):
        params = values.of({
            'CustomerName': customer_name,
            'FriendlyName': friendly_name,
            'IsoCountry': iso_country,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            AddressInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __call__(self, sid):
        """
        Constructs a AddressContext
        
        :param sid: Contextual sid
        
        :returns: AddressContext
        :rtype: AddressContext
        """
        return AddressContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AddressList>'


class AddressContext(InstanceContext):

    def __init__(self, version, account_sid, sid):
        """
        Initialize the AddressContext
        
        :param Version version
        :param account_sid: Contextual account_sid
        :param sid: Contextual sid
        
        :returns: AddressContext
        :rtype: AddressContext
        """
        super(AddressContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/Addresses/{sid}.json'.format(**self._kwargs)
        
        # Dependents
        self._dependent_phone_numbers = None

    def delete(self):
        return self._version.delete('delete', self._uri)

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            AddressInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def update(self, friendly_name=values.unset, customer_name=values.unset,
               street=values.unset, city=values.unset, region=values.unset,
               postal_code=values.unset):
        data = values.of({
            'FriendlyName': friendly_name,
            'CustomerName': customer_name,
            'Street': street,
            'City': city,
            'Region': region,
            'PostalCode': postal_code,
        })
        
        return self._version.update(
            AddressInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    @property
    def dependent_phone_numbers(self):
        """
        Access the dependent_phone_numbers
        
        :returns: DependentPhoneNumberList
        :rtype: DependentPhoneNumberList
        """
        if self._dependent_phone_numbers is None:
            self._dependent_phone_numbers = DependentPhoneNumberList(
                self._version,
                account_sid=self._kwargs['account_sid'],
                address_sid=self._kwargs['sid'],
            )
        return self._dependent_phone_numbers

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Api.V2010.AddressContext {}>'.format(context)


class AddressInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, sid=None):
        """
        Initialize the AddressInstance
        
        :returns: AddressInstance
        :rtype: AddressInstance
        """
        super(AddressInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'city': payload['city'],
            'customer_name': payload['customer_name'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'friendly_name': payload['friendly_name'],
            'iso_country': payload['iso_country'],
            'postal_code': payload['postal_code'],
            'region': payload['region'],
            'sid': payload['sid'],
            'street': payload['street'],
            'uri': payload['uri'],
        }
        
        # Context
        self._instance_context = None
        self._kwargs = {
            'account_sid': account_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: AddressContext for this AddressInstance
        :rtype: AddressContext
        """
        if self._instance_context is None:
            self._instance_context = AddressContext(
                self._version,
                self._kwargs['account_sid'],
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
    def city(self):
        """
        :returns: The city
        :rtype: str
        """
        return self._properties['city']

    @property
    def customer_name(self):
        """
        :returns: The customer_name
        :rtype: str
        """
        return self._properties['customer_name']

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
    def friendly_name(self):
        """
        :returns: The friendly_name
        :rtype: str
        """
        return self._properties['friendly_name']

    @property
    def iso_country(self):
        """
        :returns: The iso_country
        :rtype: str
        """
        return self._properties['iso_country']

    @property
    def postal_code(self):
        """
        :returns: The postal_code
        :rtype: str
        """
        return self._properties['postal_code']

    @property
    def region(self):
        """
        :returns: The region
        :rtype: str
        """
        return self._properties['region']

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: str
        """
        return self._properties['sid']

    @property
    def street(self):
        """
        :returns: The street
        :rtype: str
        """
        return self._properties['street']

    @property
    def uri(self):
        """
        :returns: The uri
        :rtype: str
        """
        return self._properties['uri']

    def delete(self):
        self._context.delete()

    def fetch(self):
        self._context.fetch()

    def update(self, friendly_name=values.unset, customer_name=values.unset,
               street=values.unset, city=values.unset, region=values.unset,
               postal_code=values.unset):
        self._context.update(
            friendly_name=friendly_name,
            customer_name=customer_name,
            street=street,
            city=city,
            region=region,
            postal_code=postal_code,
        )

    @property
    def dependent_phone_numbers(self):
        """
        Access the dependent_phone_numbers
        
        :returns: dependent_phone_numbers
        :rtype: dependent_phone_numbers
        """
        return self._context.dependent_phone_numbers

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Api.V2010.AddressInstance {}>'.format(context)
