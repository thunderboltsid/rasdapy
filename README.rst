RasPy - Talk RasQL using Python
===============================

TODO: Add build status here

Copyright 2003, 2004, 2005, 2006, 2007, 2008, 2009 Peter Baumann /
rasdaman GmbH.

RasPy is a client side interface for Rasdaman that enables execution of
RasQL queries using the python programming languae.

This directory contains the RasPy library.

Normally, this directory comes as part of the rasdaman package,
available from:

http://rasdaman.org

The complete package includes the rasdaman source code. If you
downloaded this package from PyPI or some other Python-specific source,
you may have received only the Python part of the code. In this case,
you will need to obtain the rasdaman database system from some other
source before you can use this package locally.

Development Warning
===================

The Python implementation of Protocol Buffers is not as mature as the
C++ and Java implementations. It may be more buggy, and it is known to
be pretty slow at this time. Since this library relies heavily on
Protocol Buffers and GRPC, it might be prone to occasional hiccups and
unexpected behaviour.

Installation
============

1) Make sure you have Python 2.6 or newer. If in doubt, run:

   $ python -V

2) If you do not have setuptools, numpy, scipy, grpcio, and protobuf
   installed, note that they will be downloaded and installed
   automatically as soon as you run setup.py. If you would rather
   install them manually, you may do so by following the instructions on
   this page:

   https://packaging.python.org/en/latest/installing.html#setup-for-installing-packages

3) Build the C++ code, or install a binary distribution of protoc. If
   you install a binary distribution, make sure that it is the same
   version as this package. If in doubt, run:

   $ protoc --version

4) Build and run the tests:

    $ python setup.py build
    $ python setup.py test

If some tests fail, this library may not work correctly on your system.
Continue at your own risk.

Please note that there is a known problem with some versions of Python
on Cygwin which causes the tests to fail after printing the error:
"sem\_init: Resource temporarily unavailable". This appears to be a bug
either in Cygwin or in Python:
http://www.cygwin.com/ml/cygwin/2005-07/msg01378.html We do not know if
or when it might me fixed. We also do not know how likely it is that
this bug will affect users in practice.

5) Install:

   $ python setup.py install

This step may require superuser privileges.

Usage
=====

The complete documentation for RasPy is still under development.

Import Raspy
------------

::

    $ import raspy

Connect to default port 7001 if not specified
---------------------------------------------

::

    $ ras = raspy.Connection(hostname="0.0.0.0", username="myuser", password="mypass", port=7000)

Open the database given a db name
---------------------------------

::

    $ db = ras.database("dbname")

List of all the collections available
-------------------------------------

::

    $ collection_list = db.collections ()

Begin transaction
-----------------

::

    $ txn = db.transaction ()

Get array data from rasdaman server using RasQL query
-----------------------------------------------------

::

    $ query = txn.query("select m[0:10 ,0:10] from mr as m")
    $ data = query.execute()

End transaction
---------------

::

    $ del txn

Close the database connection
-----------------------------

::

    $ del db

Convert to Numpy Array
----------------------

::

    $ data = data.toArray()

Numpy Operations
----------------

::

    $ data += 1

Contributors
============
* Siddharth Shukla

Thanks also to
==============
* Alex Mircea Dumitru
* Vlad Merticariu
* Peter Baumann