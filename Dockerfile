FROM debian:trixie

# install required packages from repositories
#RUN sed -i -e "s/ main[[:space:]]*\$/ main contrib non-free/" /etc/apt/sources.list
RUN DEBIAN_FRONTEND=noninteractive apt-get update -y && apt-get upgrade -y \
  && apt-get install -y --no-install-recommends python3 python3-biopython \
  python3-numpy python3-scipy gawk sed python3-dev python3-numpy-dev \
  python3-pip gcc

# environment variables
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV TERM=xterm

WORKDIR /
RUN mkdir /build
ADD . /build
WORKDIR /build/
RUN pip install . --break-system-packages

# cleanup
WORKDIR /
RUN rm -rf /build

# default interactive shell
CMD ["/bin/bash"]
