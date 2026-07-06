=============
ckanext-theme-ldm-tib
=============

This CKAN extension provides the theme of the main instance of the Leibniz Data Manager (LDM) as hosted by the Technische Informationsbibliothek (TIB).


------------
Requirements
------------

This extension has been tested with CKAN 2.9.


------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-theme-ldm-tib:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-theme-ldm-tib Python package into your virtual environment::

    git clone https://github.com/SDM-TIB/ckanext-theme-ldm-tib.git
    cd ckanext-theme-ldm-tib
    pip install -e .

3. Add ``TIBtheme`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload

