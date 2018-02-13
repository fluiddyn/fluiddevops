FROM ${image}
MAINTAINER Ashwin Vishnu Mohanan <avmo@kth.se>

RUN apt-get update

RUN apt-get install -y --no-install-recommends libfftw3-mpi-dev
RUN apt-get install -y --no-install-recommends libhdf5-openmpi-dev
RUN apt-get install -y --no-install-recommends openmpi-bin
RUN apt-get install -y --no-install-recommends libopenblas-dev
RUN apt-get install -y --no-install-recommends gfortran
RUN apt-get install -y --no-install-recommends emacs vim
RUN apt-get install -y --no-install-recommends libfftw3-dev
RUN apt-get install -y --no-install-recommends udisks2

RUN rm -rf /var/lib/apt/lists/*

RUN groupadd -g 999 appuser && useradd -m -r -u 999 -g appuser -s /bin/bash appuser
USER appuser

RUN mkdir -p $HOME/opt
WORKDIR $HOME/opt

RUN mkdir -p $HOME/.local/include
RUN mkdir -p $HOME/.local/lib
RUN ln -s /usr/include/fftw* $HOME/.local/include
RUN ln -s /usr/lib/x86_64-linux-gnu/libfftw3* $HOME/.local/lib
RUN wget https://bitbucket.org/fluiddyn/fluidfft/raw/default/doc/install/install_p3dfft.sh -O ./install_p3dfft.sh
RUN bash install_p3dfft.sh
RUN wget https://bitbucket.org/fluiddyn/fluidfft/raw/default/doc/install/install_pfft.sh -O ./install_pfft.sh
RUN bash install_pfft.sh
RUN wget https://bitbucket.org/fluiddyn/fluidfft/raw/default/doc/install/install_pfft.sh -O ./install_pfft.sh
RUN wget https://bitbucket.org/fluiddyn/fluidfft/raw/default/site.cfg.files/site.cfg.docker -O ~/.fluidfft-site.cfg

COPY requirements.txt $PWD
RUN ${pip} install --no-cache-dir --user -U -r requirements.txt
COPY requirements_extra.txt $PWD
RUN ${pip} install --no-cache-dir --user -U -r requirements_extra.txt

RUN mkdir -p $HOME/.config/matplotlib
RUN echo 'backend      : agg' > $HOME/.config/matplotlib/matplotlibrc
