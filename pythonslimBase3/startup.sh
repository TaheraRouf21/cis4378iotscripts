#! /bin/sh

/usr/sbin/rsyslogd

su - app -c "python strongConfig1.py" &

sleep infinity