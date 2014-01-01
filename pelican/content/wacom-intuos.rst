Wacom Intuos Pro and Linux
##########################
:date: 2014-01-01 14:58
:author: nasser
:category: Paintings
:slug: wacom-intuos
:tags: krita, mypaint, paintings, linux, arch, wacom, intuos pro, review,
       installation, configuration

Intuos Pro
==========

|wacom1|

So a new year and I got my self a little gift, a Wacom Intuos pro. I'm upgrading
from an Intuos 3 so my opinions could be a little out of date.

Here is a couple of pictures of the pen and the pen holder.

|wacom2|
|wacom3|

The cool thing about the pen is the different nibs that you can use. As you can
see in the picture below, the nibs are stored in the pen holder and you can
choose the one that best suits your style.

|wacom4|

The Intuos pro comes in three different sized. I got the small one because it's
cheaper :P and I wanted a compact tablet that I can easily carry with me if
I want to. The tablet surface feels like paper and It's definitely an improvement
over the Intuos 3.

|wacom5|

Another thing that I really like about the Intuos pro is the ability to have it
work wirelessly. Underneath the tablet there is a removable battery and
a compartment for the wireless dongle. You can remove the battery and the
wireless dongle if you want to work in wired mode. The battery is charged via
the USB cable in wired mode.

|wacom6|

Here are closer pictures of the wireless and USB dongle.


|wacom7|
|wacom8|

Installation and Configuration
==============================
The main purpose of this blog post is to show how I got the tablet to work under
Linux. I'm using Arch at the moment and when I plugged the tablet in, it did't
work. I had to mess with it a bit to get it working.

Driver installation
-------------------
First off, you need to install the wacom drivers. So run the following command
which will install the drivers form the main repos.

.. code:: sh

    sudo pacman -S xf86-input-wacom

Kernel module installation
--------------------------
Then you have to install this kernel module_. Thanks to apicici_ for maintaining
this. It's not in the official repos but you can get it from AUR. I'm using
yaourt here, but you can use whatever AUR manager you have. Also, you have to
have the kernel headers installed before this step, if you don't have them already.

.. code:: sh

    sudo pacman -S linux-headers
    sudo yaourt -S input-wacom-dkms


Desktop environment configuration
---------------------------------
I use KDE now and there's a cool :abbr:`KCM (KConfig Modules)` for the wacom
tablet in the AUR. To get it run the following:

.. code:: sh

    sudo yaourt -S kcm-wacomtablet

Here is a screen shot of it:

|kcm1|

The tablet could be used as a big touchpad. While it's good to have the option,
it's not really practical because the palm rejection isn't working. So I think
disabling the touchpad is better, for now at least. You can do so as shown in
the screen shot below:

|kcm2|

One awesome feature of this KCS, is the ability to have profiles. Here I have
some shortcuts for MyPaint_.

|kcm3|

So this is it, have fun!

|wacom9|

.. |wacom1| image:: {filename}images/wacom/wacom1.jpg
   :alt: wacom intuos pro

.. |wacom2| image:: {filename}images/wacom/wacom2.jpg
   :alt: wacom intuos pro pen and pen holder

.. |wacom3| image:: {filename}images/wacom/wacom3.jpg
   :alt: wacom intuos pro pen

.. |wacom4| image:: {filename}images/wacom/wacom4.jpg
   :alt: wacom intuos pro holde and nibs 

.. |wacom5| image:: {filename}images/wacom/wacom5.jpg
   :alt: wacom intuos pro table 

.. |wacom6| image:: {filename}images/wacom/wacom6.jpg
   :alt: wacom intuos pro table 

.. |wacom7| image:: {filename}images/wacom/wacom7.jpg
   :alt: wacom intuos pro table 

.. |wacom8| image:: {filename}images/wacom/wacom8.jpg
   :alt: wacom intuos pro table 

.. |wacom9| image:: {filename}images/wacom/wacom9.jpg
   :alt: wacom intuos pro table 

.. |kcm1| image:: {filename}images/wacom/kcm1.png
   :alt: Wacom KCM
   :target: {filename}images/wacom/kcm1.png

.. |kcm2| image:: {filename}images/wacom/kcm2.png
   :alt: Wacom KCM
   :target: {filename}images/wacom/kcm2.png

.. |kcm3| image:: {filename}images/wacom/kcm3.png
   :alt: Wacom KCM
   :target: {filename}images/wacom/kcm3.png

.. _module: https://aur.archlinux.org/packages/input-wacom-dkms/ 

.. _apicici: https://aur.archlinux.org/packages/?K=apicici&SeB=m

.. _more: https://bbs.archlinux.org/viewtopic.php?pid=133772

.. _MyPaint: http://mypaint.intilinux.com/
