# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class WorkspaceCumulativeStatisticsTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.taskrouter.v1.workspaces(sid="WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .cumulative_statistics().fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://taskrouter.twilio.com/v1/Workspaces/WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/CumulativeStatistics',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "reservations_accepted": 100,
                "tasks_completed": 100,
                "start_time": "2015-07-30T20:00:00Z",
                "reservations_rescinded": 100,
                "tasks_timed_out_in_workflow": 100,
                "end_time": "2015-07-30T20:00:00Z",
                "avg_task_acceptance_time": 100,
                "tasks_canceled": 100,
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CumulativeStatistics",
                "tasks_moved": 100,
                "tasks_deleted": 100,
                "tasks_created": 100,
                "reservations_canceled": 100,
                "reservations_timed_out": 100,
                "wait_duration_until_canceled": {
                    "avg": 0,
                    "min": 0,
                    "max": 0,
                    "total": 0
                },
                "wait_duration_until_accepted": {
                    "avg": 0,
                    "min": 0,
                    "max": 0,
                    "total": 0
                },
                "split_by_wait_time": {
                    "5": {
                        "above": {
                            "tasks_canceled": 0,
                            "reservations_accepted": 0
                        },
                        "below": {
                            "tasks_canceled": 0,
                            "reservations_accepted": 0
                        }
                    },
                    "10": {
                        "above": {
                            "tasks_canceled": 0,
                            "reservations_accepted": 0
                        },
                        "below": {
                            "tasks_canceled": 0,
                            "reservations_accepted": 0
                        }
                    }
                },
                "reservations_created": 100,
                "reservations_rejected": 100,
                "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.taskrouter.v1.workspaces(sid="WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .cumulative_statistics().fetch()

        self.assertIsNotNone(actual)
