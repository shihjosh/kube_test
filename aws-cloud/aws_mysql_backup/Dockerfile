FROM joshshih/mysql-backup:v01
 
RUN apt-get update
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN pip3 install --user awscli
RUN export PATH=$PATH:$HOME/.local/bin
RUN pip3 install boto3
RUN pip3 install sh