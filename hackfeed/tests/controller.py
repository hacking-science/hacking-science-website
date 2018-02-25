# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from django.test import Client

class SimpleControllerTest(unittest.TestCase):
    def test_details(self):
        client = Client()
        response = client.get('/admin')
        self.assertEqual(response.status_code, 301)

    def test_index(self):
        client = Client()
        response = client.get('/feed')
        self.assertEqual(response.status_code, 301)
