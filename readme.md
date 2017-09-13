## BenchMark with Pytest using UnitestDefaults and Pytest Funcions

(env) deathstar:rocky valdergallo$ python manage.py test wars -v2
Creating test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
Operations to perform:
  Synchronize unmigrated apps: messages, staticfiles
  Apply all migrations: admin, auth, contenttypes, sessions, wars
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying sessions.0001_initial... OK
  Applying wars.0001_initial... OK
System check identified no issues (0 silenced).
test_create_ship (wars.tests.tests_with_db_unitest.TestCreateItemsTrasaction) ... ok
test_create_ship2 (wars.tests.tests_with_db_unitest.TestCreateItemsTrasaction) ... ok
test_request_hello_word (wars.tests.tests_with_unitest.TestRequet) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.022s

OK
Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
(env) deathstar:rocky valdergallo$ pytest -v
======================================= test session starts ========================================
platform darwin -- Python 3.6.2, pytest-3.2.2, py-1.4.34, pluggy-0.4.0 -- /Users/valdergallo/www/test-fight-pack/env/bin/python3.6
cachedir: .cache
Django settings: rocky.settings (from ini file)
rootdir: /Users/valdergallo/www/test-fight-pack/rocky, inifile: pytest.ini
plugins: django-3.1.2
collected 3 items

wars/tests/with_db_tests.py::test_create_start_ships_with_transaction PASSED
wars/tests/with_db_tests.py::test_create_start_ships_without_transaction PASSED
wars/tests/without_db_tests.py::test_index PASSED

===================================== 3 passed in 0.36 seconds =====================================
(env) deathstar:rocky valdergallo$



KEEPDB ---------------------------------------------------------------------------------------------

(env) deathstar:rocky valdergallo$ python manage.py test wars -v2 --keepdb
Using existing test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
Operations to perform:
  Synchronize unmigrated apps: messages, staticfiles
  Apply all migrations: admin, auth, contenttypes, sessions, wars
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying sessions.0001_initial... OK
  Applying wars.0001_initial... OK
System check identified no issues (0 silenced).
test_create_ship (wars.tests.tests_with_db_unitest.TestCreateItemsTrasaction) ... ok
test_create_ship2 (wars.tests.tests_with_db_unitest.TestCreateItemsTrasaction) ... ok
test_request_hello_word (wars.tests.tests_with_unitest.TestRequet) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.017s

OK
Preserving test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...

