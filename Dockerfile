FROM selenium/standalone-chrome:latest
RUN sudo mkdir -p /home/automation/app && sudo mkdir -p /home/automation/app/books &&  sudo apt-get update
COPY bookhack_ikoblyk/jpg_to_djvu.sh /home/automation/app
WORKDIR /home/automation/app
RUN sudo chmod +x jpg_to_djvu.sh
USER root
RUN sudo apt-get install -y python3-distutils
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py && sudo apt-get install -y python3-tk libxext-dev libxrender-dev libxtst-dev
RUN pip3 install bookhack-ikoblyk==0.0.5