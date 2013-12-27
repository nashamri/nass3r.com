Boosting your ati graphics performance
######################################
:date: 2012-10-06 20:31
:author: nasser
:category: Linux
:tags: ati, Elementary OS, Linux, radeon, Ubuntu
:slug: boosting-your-ati-graphics-performance

If you have an ATI graphics card (ATI Radeon HD 3000 series or newer)
and using the open source driver you can get better performance by
enabling PCI-E Gen2 option.

To enable this on Ubuntu 12.04, you must pass this boot parameter
"radeon.pcie\_gen2=1".

Here are the detailed steps:

#. Run the following command in a terminal (use your favorite text
   editor ofc):
    ``sudo vim /etc/default/grub``
#. Change the line that says:
    ``GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"``
    To
    ``GRUB_CMDLINE_LINUX_DEFAULT="quiet splash radeon.pcie_gen2=1"``
#. Save the file and run the following command:
    ``sudo update-grub``
#. Reboot and enjoy the butter smooth performance.

I'm getting really great result while testing Elementary OS luna.
Everything is so smooth and nice, Good job elementary team :)
