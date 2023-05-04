# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class UserChannelList(ListResource):
    """  """

    def __init__(self, version, service_sid, user_sid):
        """
        Initialize the UserChannelList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service that the resource is associated with
        :param user_sid: The SID of the User the User Channel belongs to

        :returns: twilio.rest.chat.v2.service.user.user_channel.UserChannelList
        :rtype: twilio.rest.chat.v2.service.user.user_channel.UserChannelList
        """
        super(UserChannelList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'user_sid': user_sid, }
        self._uri = '/Services/{service_sid}/Users/{user_sid}/Channels'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams UserChannelInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.chat.v2.service.user.user_channel.UserChannelInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists UserChannelInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.chat.v2.service.user.user_channel.UserChannelInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of UserChannelInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of UserChannelInstance
        :rtype: twilio.rest.chat.v2.service.user.user_channel.UserChannelPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return UserChannelPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of UserChannelInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of UserChannelInstance
        :rtype: twilio.rest.chat.v2.service.user.user_channel.UserChannelPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return UserChannelPage(self._version, response, self._solution)

    def get(self, channel_sid):
        """
        Constructs a UserChannelContext

        :param channel_sid: The SID of the Channel that has the User Channel to fetch

        :returns: twilio.rest.chat.v2.service.user.user_channel.UserChannelContext
        :rtype: twilio.rest.chat.v2.service.user.user_channel.UserChannelContext
        """
        return UserChannelContext(
            self._version,
            service_sid=self._solution['service_sid'],
            user_sid=self._solution['user_sid'],
            channel_sid=channel_sid,
        )

    def __call__(self, channel_sid):
        """
        Constructs a UserChannelContext

        :param channel_sid: The SID of the Channel that has the User Channel to fetch

        :returns: twilio.rest.chat.v2.service.user.user_channel.UserChannelContext
        :rtype: twilio.rest.chat.v2.service.user.user_channel.UserChannelContext
        """
        return UserChannelContext(
            self._version,
            service_sid=self._solution['service_sid'],
            user_sid=self._solution['user_sid'],
            channel_sid=channel_sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Chat.V2.UserChannelList>'


class UserChannelPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the UserChannelPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The SID of the Service that the resource is associated with
        :param user_sid: The SID of the User the User Channel belongs to

        :returns: twilio.rest.chat.v2.service.user.user_channel.UserChannelPage
        :rtype: twilio.rest.chat.v2.service.user.user_channel.UserChannelPage
        """
        super(UserChannelPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of UserChannelInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.chat.v2.service.user.user_channel.UserChannelInstance
        :rtype: twilio.rest.chat.v2.service.user.user_channel.UserChannelInstance
        """
        return UserChannelInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            user_sid=self._solution['user_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Chat.V2.UserChannelPage>'


class UserChannelContext(InstanceContext):
    """  """

    def __init__(self, version, service_sid, user_sid, channel_sid):
        """
        Initialize the UserChannelContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service to fetch the User Channel resource from
        :param user_sid: The SID of the User to fetch the User Channel resource from
        :param channel_sid: The SID of the Channel that has the User Channel to fetch

        :returns: twilio.rest.chat.v2.service.user.user_channel.UserChannelContext
        :rtype: twilio.rest.chat.v2.service.user.user_channel.UserChannelContext
        """
        super(UserChannelContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'user_sid': user_sid, 'channel_sid': channel_sid, }
        self._uri = '/Services/{service_sid}/Users/{user_sid}/Channels/{channel_sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a UserChannelInstance

        :returns: Fetched UserChannelInstance
        :rtype: twilio.rest.chat.v2.service.user.user_channel.UserChannelInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return UserChannelInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            user_sid=self._solution['user_sid'],
            channel_sid=self._solution['channel_sid'],
        )

    def update(self, notification_level):
        """
        Update the UserChannelInstance

        :param UserChannelInstance.NotificationLevel notification_level: The push notification level to assign to the User Channel

        :returns: Updated UserChannelInstance
        :rtype: twilio.rest.chat.v2.service.user.user_channel.UserChannelInstance
        """
        data = values.of({'NotificationLevel': notification_level, })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return UserChannelInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            user_sid=self._solution['user_sid'],
            channel_sid=self._solution['channel_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Chat.V2.UserChannelContext {}>'.format(context)


class UserChannelInstance(InstanceResource):
    """  """

    class ChannelStatus(object):
        JOINED = "joined"
        INVITED = "invited"
        NOT_PARTICIPATING = "not_participating"

    class NotificationLevel(object):
        DEFAULT = "default"
        MUTED = "muted"

    def __init__(self, version, payload, service_sid, user_sid, channel_sid=None):
        """
        Initialize the UserChannelInstance

        :returns: twilio.rest.chat.v2.service.user.user_channel.UserChannelInstance
        :rtype: twilio.rest.chat.v2.service.user.user_channel.UserChannelInstance
        """
        super(UserChannelInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'service_sid': payload['service_sid'],
            'channel_sid': payload['channel_sid'],
            'user_sid': payload['user_sid'],
            'member_sid': payload['member_sid'],
            'status': payload['status'],
            'last_consumed_message_index': deserialize.integer(payload['last_consumed_message_index']),
            'unread_messages_count': deserialize.integer(payload['unread_messages_count']),
            'links': payload['links'],
            'url': payload['url'],
            'notification_level': payload['notification_level'],
        }

        # Context
        self._context = None
        self._solution = {
            'service_sid': service_sid,
            'user_sid': user_sid,
            'channel_sid': channel_sid or self._properties['channel_sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: UserChannelContext for this UserChannelInstance
        :rtype: twilio.rest.chat.v2.service.user.user_channel.UserChannelContext
        """
        if self._context is None:
            self._context = UserChannelContext(
                self._version,
                service_sid=self._solution['service_sid'],
                user_sid=self._solution['user_sid'],
                channel_sid=self._solution['channel_sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: The SID of the Service that the resource is associated with
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def channel_sid(self):
        """
        :returns: The SID of the Channel the resource belongs to
        :rtype: unicode
        """
        return self._properties['channel_sid']

    @property
    def user_sid(self):
        """
        :returns: The SID of the User the User Channel belongs to
        :rtype: unicode
        """
        return self._properties['user_sid']

    @property
    def member_sid(self):
        """
        :returns: The SID of the User as a Member in the Channel
        :rtype: unicode
        """
        return self._properties['member_sid']

    @property
    def status(self):
        """
        :returns: The status of the User on the Channel
        :rtype: UserChannelInstance.ChannelStatus
        """
        return self._properties['status']

    @property
    def last_consumed_message_index(self):
        """
        :returns: The index of the last Message in the Channel the Member has read
        :rtype: unicode
        """
        return self._properties['last_consumed_message_index']

    @property
    def unread_messages_count(self):
        """
        :returns: The number of unread Messages in the Channel for the User
        :rtype: unicode
        """
        return self._properties['unread_messages_count']

    @property
    def links(self):
        """
        :returns: Absolute URLs to access the Members, Messages , Invites and, if it exists, the last Message for the Channel
        :rtype: unicode
        """
        return self._properties['links']

    @property
    def url(self):
        """
        :returns: The absolute URL of the resource
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def notification_level(self):
        """
        :returns: The push notification level of the User for the Channel
        :rtype: UserChannelInstance.NotificationLevel
        """
        return self._properties['notification_level']

    def fetch(self):
        """
        Fetch a UserChannelInstance

        :returns: Fetched UserChannelInstance
        :rtype: twilio.rest.chat.v2.service.user.user_channel.UserChannelInstance
        """
        return self._proxy.fetch()

    def update(self, notification_level):
        """
        Update the UserChannelInstance

        :param UserChannelInstance.NotificationLevel notification_level: The push notification level to assign to the User Channel

        :returns: Updated UserChannelInstance
        :rtype: twilio.rest.chat.v2.service.user.user_channel.UserChannelInstance
        """
        return self._proxy.update(notification_level, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Chat.V2.UserChannelInstance {}>'.format(context)
