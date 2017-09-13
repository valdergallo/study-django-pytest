# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.test import TestCase
from wars.models import Weapow
from wars.models import StarShip


class TestCreateItemsTrasaction(TestCase):

    def test_create_ship(self):
        wp = Weapow.objects.create(name='laser', damage=100)

        s1 = StarShip.objects.create(name='s1')
        s1.save()
        s1.weapows.add(wp)

        assert s1.name == 's1'
        assert s1.weapows.count() == 1

        self.assertEqual(s1.name, 's1')
        self.assertEqual(s1.weapows.count(), 1)

    def test_create_ship2(self):
        wp = Weapow.objects.create(name='laser', damage=100)

        s1 = StarShip.objects.create(name='s1')
        s1.save()
        s1.weapows.add(wp)

        assert s1.name == 's1'
        assert s1.weapows.count() == 1

        self.assertEqual(s1.name, 's1')
        self.assertEqual(s1.weapows.count(), 1)
