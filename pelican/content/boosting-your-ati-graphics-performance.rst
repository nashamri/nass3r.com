Boosting your ati graphics performance
######################################
:date: 2012-10-06 20:31
:author: nasser
:category: Linux
:slug: boosting-your-ati-graphics-performance
:tags: ati, elementary OS, Linux, radeon, ubuntu

If you have an ATI graphics card (ATI Radeon HD 3000 series or newer)
and using the open source driver you can get better performance by
enabling PCI-E Gen2 option.
To enable this on Ubuntu 12.04, you must pass this boot parameter:

.. code:: sh

    radeon.pcie_gen2=1

Here are the detailed steps:

1. Run the following command in a terminal (use your favorite text editor):

.. code:: sh

    sudo vim /etc/default/grub

2. Change the line that says:

.. code:: sh

    GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"

To

.. code:: sh

    GRUB_CMDLINE_LINUX_DEFAULT="quiet splash radeon.pcie_gen2=1"

3. Save the file and run the following command:

.. code:: sh

    sudo update-grub

4. Reboot and enjoy the butter smooth performance.

I'm getting really great result while testing Elementary OS luna.
Everything is so smooth and nice, Good job elementary team :)
