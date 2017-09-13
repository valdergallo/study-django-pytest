# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.test import SimpleTestCase


class TestRequet(SimpleTestCase):

    def test_request_hello_word(self):
        response = self.client.get('/')
        self.assertEqual(response.content, b'Hello, world')
        assert response.content == b'Hello, world'
