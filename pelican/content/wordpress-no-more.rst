Wordpress no more
#################
:date: 2013-12-28 15:13
:author: nasser
:category: News
:slug: wordpress-no-more
:tags: wordpress, pelican

This blog was running on wordpress until an update to my server broke it.
I was running the ubuntu server version of wordpress and something went wrong
and caused the WSOD_ (White Screen of Death). I finally managed to solve the problem
after hours of searching. Then I thought about it. Why am I using wordpress?
It's an overkill to what I want. I just want a simple blog engine that I can
customize and support basic functionality.

The first thing I wanted is a static blog. I don't want to deal with MySQL or
PHP anymore. Which led me to the concept of static blog engines. There are lots
of them out there, for example:

* Nikola_ 

* Hyde_

* Pelican_

These are all Python based. You can find more at https://wiki.python.org/moin/PythonBlogSoftware.

I've decided to go with Pelican_ and picked a theme called Lannisport_ and
modified it to my liking.
 
.. _WSOD: http://en.wikipedia.org/wiki/Screen_of_death#Other_screens_of_death
.. _Nikola: http://getnikola.com
.. _Hyde: http://ringce.com/hyde
.. _Pelican: http://blog.getpelican.com
.. _Lannisport: https://github.com/siovene/lannisport
