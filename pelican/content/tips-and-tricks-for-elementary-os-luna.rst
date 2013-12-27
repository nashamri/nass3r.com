Tips and Tricks for elementary OS Luna
######################################
:date: 2012-12-11 19:19
:author: nasser
:category: Linux
:slug: tips-and-tricks-for-elementary-os-luna
:tags: elementary OS, linux, tips and tricks


After using Elementary OS as my main distro on my Desktop and my laptop
for sometime, Here are some tips and tricks and small modifications that
I have right now:

Make sure you have dconf-editor installed you can do so by running this
command:


.. code:: sh

    sudo apt-get install dconf-tools


1. Remove ubuntu overlay scroll bars:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
open dconf-editor then go to this path:

.. code:: sh

    org.gnome.desktop.interface

And uncheck the ubuntu-overlay-scrollbars entry.

2. Silencing the bell:
~~~~~~~~~~~~~~~~~~~~~~

This for muting that annoying sound when you try to auto-complete
something in the terminal and nothing matches. Go to this path with
dconf-editor:

.. code:: sh

    org.gnome.desktop.wm.preferences

And uncheck the audible-bell entry.

3. Modify the dock:
~~~~~~~~~~~~~~~~~~~

I like to have the indicators on so I can know whether a program is
running or not.
To do so, open up this file with your favorite text editor:

.. code:: sh

    ~/.config/plank/theme/dock.theme

And change this line:

.. code:: sh

    IndicatorSize=5

Its default value was zero on my installation, it might be different on
yours. You can change a lot of stuff in here, like the color of the
dock, the padding of the items, etc. Each entry is commented with a
small description.

On my laptop I have a limited vertical space, so having the dock on the
bottom wasn't the best idea in my opinion. So to change the position of
the dock, open up this file

.. code:: sh

    ~/.config/plank/dock1/settings

And change the value of the "Position" variable to either 0,1,2,3.

0 to move it to the left.

1 to move it to the right.

2 to move it to the top (doesn't work since we have the top bar).

3 to move it to the bottom (the default value).

That's it for now, hope you like it and to the elementary devs and
designers, you guys rock! \\m/,
