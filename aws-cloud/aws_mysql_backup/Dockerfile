FROM joshshih/mysql-backup:v01

RUN apt-get update
RUN apt-get -y install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev
RUN curl -O https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tar.xz
RUN tar -xf Python-3.8.2.tar.xz
RUN cd Python-3.8.2
RUN ./configure --enable-optimizations
RUN make -j$(nproc)
RUN make altinstall
RUN python3.8 --version
RUN apt-get -y install python3-venv python3-pip
# RUN pip3 -y install --user awscli
