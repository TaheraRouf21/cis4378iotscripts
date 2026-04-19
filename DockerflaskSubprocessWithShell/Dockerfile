FROM python:3.10-slim
#RUN apt install nano

#update repository lists
RUN apt-get update
#logging
RUN printf 'Y' | apt install rsyslog
#remove kernel module from rsyslog configuration
RUN sed -i '12d' /etc/rsyslog.conf
# add lsof for viewing open socket files
RUN printf 'Y' | apt install lsof

#Docker commands to add script to configuration file
COPY promptCommand.txt /var
# Append prompt_command env var, to configure shell logging
RUN cat /var/promptCommand.txt | tr -d '\r' >> /etc/bash.bashrc
# Not needed. Delete
RUN rm /var/promptCommand.txt

#RUN printf 'Y' | apt install mosquitto_clients

RUN pip install flask

RUN pip install bcrypt

RUN pip install python-dateutil

# add app user to isolate and limit privileges
RUN adduser --gecos "username" --disabled-password app

# set app password
RUN echo 'app:app' | chpasswd

# set root password
RUN echo 'root:D3hmZ89sf2q5Ptu' | chpasswd

# change group

# most recently added
# change default shell of app
RUN usermod -s /bin/rbash app

# change group of su executable to root and none for user
RUN dpkg-statoverride --update --add root root 4750 /bin/su
RUN dpkg-statoverride --update --add root root 4750 /usr/bin/chsh

WORKDIR /home/app

#Copy python files
COPY updateFlaskTemp .

COPY startup.sh /etc

#RUN chown app session.txt
#RUN chown app sessionTime.txt

ENTRYPOINT ["bash", "/etc/startup.sh"]