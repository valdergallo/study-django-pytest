# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from wars.models import Weapow
from wars.models import StarShip
import pytest


@pytest.mark.django_db(transaction=True)
def test_create_start_ships_with_transaction():
    wp = Weapow.objects.create(name='laser', damage=100)

    s1 = StarShip.objects.create(name='s1')
    s1.save()
    s1.weapows.add(wp)

    assert s1.name == 's1'
    assert s1.weapows.count() == 1


@pytest.mark.django_db(transaction=False)
def test_create_start_ships_without_transaction():
    wp = Weapow.objects.create(name='laser', damage=100)

    s1 = StarShip.objects.create(name='s1')
    s1.save()
    s1.weapows.add(wp)

    assert s1.name == 's1'
    assert s1.weapows.count() == 1
