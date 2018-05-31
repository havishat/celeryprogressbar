==============================================================
 Example Django project using Celery
==============================================================

Contents
========

``proj/``
---------

This is the celery module

``proj/celery.py``
----------

This module contains the Celery application instance for this project,
we take configuration from Django settings and use ``autodiscover_tasks`` to
find task modules inside all packages listed in ``INSTALLED_APPS``.

``sampleapp/``
------------

Example sample app.  This is decoupled from the rest of the project by using
the ``@shared_task`` decorator.  This decorator returns a proxy that always
points to the currently active Celery instance.

Installing requirements
=======================

The settings file assumes that ``rabbitmq-server`` is running on ``localhost``
using the default ports. More information here:

wget https://dl.bintray.com/rabbitmq/all/rabbitmq-server/3.7.5/rabbitmq-server-mac-standalone-3.7.5.tar.xz

tar -xvf rabbitmq-server-mac-standalone-3.7.5.tar.xz

cd rabbitmq_server-3.7.5/

To start the server -

.. code-block:: console

    $ sbin/rabbitmq-server -detached

To check the status -

.. code-block:: console

    $ sbin/rabbitmqctl status

To stop the server -

.. code-block:: console

    $ sbin/rabbitmqctl stop


In addition, some Python requirements must also be satisfied:

.. code-block:: console

    $ python -m pip install -r requirements.txt

Starting the  celery worker
===================

.. code-block:: console

    $ celery -A proj worker -l info

Starting the Django Server
==========================

.. code-block:: console

    $ python manage.py runserver

Accessing the App
===================

http://localhost:8000/sampleapp/
For progress bar - http://localhost:8000/sampleapp/index


