# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import pytest


@pytest.mark.urls('wars.urls')
def test_index(client):
    assert b"Hello, world" in client.get('/').content
