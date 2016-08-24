RasdaPy - Talk RasQL using Python
=================================

Copyright 2003 - 2016 Peter Baumann / rasdaman GmbH.

RasdaPy is a client side interface for Rasdaman that enables execution of
RasQL queries using the python programming languae without having to write the
actual RasQL queries.

This directory contains the RasdaPy library.

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

1) Make sure you have Python 2.7 or newer if using Python 2 and Python 3.4 or
newer if using Python 3. If in doubt, run:

::

   $ python --version

2) If you do not have setuptools, numpy, scipy, grpcio, and protobuf
   installed, note that they will be downloaded and installed
   automatically as soon as you run setup.py. If you would rather
   install them manually, you may do so by following the instructions on
   this page:

   https://packaging.python.org/en/latest/installing.html#setup-for-installing-packages

3) Install:

::

   $ pip install rasdapy

This step may require superuser privileges. In case the setup fails because of library issues, the dependencies
for the library are `grpcio>=1.0.0`, `numpy`, `protobuf>=3.0.0`, and `numpy`.

Usage: For low level API
========================

The complete documentation for RasdaPy can be found in Sphinx docs under the docs directory. Examples
can be found in the examples directory.

Import RasdaPy core API
-----------------------

::

    $ from rasdapy.core import Connection

Connect to default port 7001 if not specified
---------------------------------------------

::

    $ con = Connection(hostname="0.0.0.0", username="myuser", password="mypass", port=7000)

Open the database given a db name
---------------------------------

::

    $ db = con.database("dbname")

List of all the collections available
-------------------------------------

::

    $ collection_list = db.collections
    $ print(collection_list)

Begin transaction
-----------------

::

    $ txn = db.transaction()

Get array data from rasdaman server using RasQL query
-----------------------------------------------------

::

    $ query = txn.query("select m[0:10 ,0:10] from mr as m")
    $ data = query.execute()

End transaction (commit or abort as preferred)
----------------------------------------------

::

    $ txn.abort()
    $ txn.commit()

Close the database connection
-----------------------------

::

    $ db.close()

Convert to Numpy Array
----------------------

::

    $ data = data.to_array()

Numpy Operations
----------------

::

    $ data += 1


Usage: For Query Construction
=============================
Import RasdaPy lib API
----------------------

::

    $ from rasdapy.surface import RasCollection

Initialize RasCollection with collection name
---------------------------------------------
::

    $ col = RasCollection("rgb")

Perform operations as desired
-----------------------------
::

    $ col /= 3
    $ col += 10
    $ col = col.avg_cells()
    $ data = col.eval()

Add the associated database instance
------------------------------------
::

    $ col.use_db(db)

Get the data from db
--------------------
::

    $ arr = col.eval()
    $ data = col.to_array()

Convert array to image (only for 2D data)
-----------------------------------------
::

    $ arr.to_image("example.png")

Contributors
============
* Siddharth Shukla

Thanks also to
==============
* Alex Mircea Dumitru
* Vlad Merticariu
* George Merticariu
* Alex Toader
* Peter Baumann
