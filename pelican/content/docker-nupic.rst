Docker NuPIC
============

:date: 2014-10-10 9:38
:author: nasser
:category: Linux 
:slug: docker-nupic
:tags: linux, arch, docker, nupic, ipython, python, notebook, nupic studio, X11,
       SSH, VNC, numenta, Dockerfile, image

|docker_nupic|

*UPDATE* Right now nupic is available at PyPi and can be simply installed by:

.. code:: bash

    pip install nupic


I just set up a docker image that will provide an easy development environment
for the NuPIC_ project. The image comes with the following:

- NuPIC
- NuPIC Studio
- iPython notebook
- Matplotlib
- MySQL server

The docker image is available at the docker hub here_. And the Dockerfile_ is at
github with all the instructions to use.

.. |docker_nupic| image:: {filename}images/docker_nupic.png
   :alt: Docker and NuPIC

.. _NuPIC: https://github.com/numenta/nupic

.. _here: https://registry.hub.docker.com/u/nashamri/nupic/

.. _Dockerfile: https://github.com/nashamri/nupic
