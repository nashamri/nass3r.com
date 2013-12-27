Android Storage space running out!
##################################
:date: 2013-03-28 14:37
:author: nasser
:category: Android
:slug: android-storage-space-running-out
:tags: android, storage space

I have my galaxy SII with Cyanogenmod 10.1 and I got this message
"Storage space running out some system functions may not work". I tried
to uninstall some applications but that didn't do the trick. I only had
like 100MB of free space. Then I found that there are like 1.8Gigs of
log files stored in the /data/log directory which I don't really care
about.

.. image:: {filename}images/androidStorage.png
    :alt: Android storage warning

So in order to free some space, I ran the following commands from the
terminal:

.. code:: bash

    $ su -
    $ cd /data/log
    $ rm *.log

It'll ask for root permissions when u run the first line.
Hope this helps!
