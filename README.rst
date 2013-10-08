Django FileBrowser
==================

**Media-Management**. (based on https://github.com/sehmaschine/django-filebrowser)

The FileBrowser is an extension to the `Django <http://www.djangoproject.com>`_ administration interface in order to:

* browse directories on your server and upload/delete/edit/rename files.
* include images/documents to your models/database using the ``FileBrowseField``.
* select images/documents with TinyMCE.

Requirements
------------

FileBrowser 3.5 requires

* Django 1.4+ (http://www.djangoproject.com)
* Pillow (https://github.com/python-imaging/Pillow)

No Grapelli
-----------

This fork removes the dependency on Grappeli.

Installation
------------

    pip install -e git+git://github.com/smacker/django-filebrowser-no-grappelli.git#egg=django-filebrowser

Documentation
-------------

http://readthedocs.org/docs/django-filebrowser/

Translation
-----------

https://www.transifex.com/projects/p/django-filebrowser/

Releases
--------

* FileBrowser 3.5.3 (Development Version, not yet released)
* FileBrowser 3.4.3: Compatible with Django 1.3/1.4
