FROM robcherry/docker-chromedriver:latest
RUN mkdir -p /home/automation/app && chown -R automation:automation /home/automation/app &&  apt-get update
#RUN  apt-get install -y make build-essential libssl-dev zlib1g-dev &&  apt-get install -y libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm &&  apt-get install -y libncurses5-dev  libncursesw5-dev xz-utils tk-dev && wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz && tar xvf Python-3.6.4.tgz && cd Python-3.6.4 && ./configure --enable-optimizations && make -j8 &&  make altinstall
