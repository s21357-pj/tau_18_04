import unittest

from zadanie1 import statement


class StatementTest(unittest.TestCase):
    def test_performances(self):
        invoice = {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "hamlet",
                    "audience": 55
                },
                {
                    "playID": "as-like",
                    "audience": 35
                },
                {
                    "playID": "othello",
                    "audience": 40
                }
            ]
        }

        plays = {
            "hamlet": {"name": "Hamlet", "type": "tragedy"},
            "as-like": {"name": "As You Like It", "type": "comedy"},
            "othello": {"name": "Othello", "type": "tragedy"}
        }

        result = "Statement for BigCo\n Hamlet: $650.00 (55 seats)\n " \
                 "As You Like It: $580.00 (35 seats)\n Othello: $500.00 " \
                 "(40 seats)\nAmount owed is $1,730.00\n" \
                 "You earned 47 credits\n"

        self.assertEqual(statement(invoice, plays), result)

    def test_no_performances(self):
        invoice = {
          "customer": "BigCo",
          "performances": []
        }

        result = "Statement for BigCo\nAmount owed is $0.00\nYou " \
                 "earned 0 credits\n"

        self.assertEqual(statement(invoice, {}), result)

    def test_tragedy_audience_30(self):
        invoice = {
          "customer": "BigCo",
          "performances": [
            {
              "playID": "hamlet",
              "audience": 30
            }
          ]
        }

        plays = {
          "hamlet": {"name": "Hamlet", "type": "tragedy"}
        }

        result = "Statement for BigCo\n Hamlet: $400.00 (30 seats)\n" \
                 "Amount owed is $400.00\nYou earned 0 credits\n"

        self.assertEqual(statement(invoice, plays), result)

    def test_comedy_audience_30(self):
        invoice = {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "as-like",
                    "audience": 35
                }
            ]
        }

        plays = {
            "as-like": {"name": "As You Like It", "type": "comedy"}
        }

        result = "Statement for BigCo\n As You Like It: $580.00 " \
                 "(35 seats)\nAmount owed is $580.00\nYou earned 12 credits\n"

        self.assertEqual(statement(invoice, plays), result)

    def test_unknown_type_of_play(self):
        invoice = {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "hamlet",
                    "audience": 55
                },
                {
                    "playID": "as-like",
                    "audience": 35
                },
                {
                    "playID": "henry-v",
                    "audience": 20
                }
            ]
        }

        plays = {
            "hamlet": {"name": "Hamlet", "type": "tragedy"},
            "as-like": {"name": "As You Like It", "type": "comedy"},
            "henry-v": {"name": "Henry V", "type": "history"}
        }

        with self.assertRaises(ValueError):
            statement(invoice, plays)
