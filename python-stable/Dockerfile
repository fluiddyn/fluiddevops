FROM python:2.7
MAINTAINER Ashwin Vishnu Mohanan <avmo@kth.se>

RUN apt-get update

RUN apt-get install -y --no-install-recommends libfftw3-dev
RUN apt-get install -y --no-install-recommends libhdf5-openmpi-dev
RUN apt-get install -y --no-install-recommends openmpi-bin
RUN apt-get install -y --no-install-recommends libopenblas-dev
RUN apt-get install -y --no-install-recommends gfortran

# RUN apt-get install -y --no-install-recommends python python-pip python-dev

RUN rm -rf /var/lib/apt/lists/*

ADD . /tmp/docker
WORKDIR /tmp/docker
RUN ./install_python.sh 3.6.0 9.0.1
RUN pip2 install -U -r requirements.txt
RUN pip3 install -U -r requirements.txt
