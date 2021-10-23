FROM centos:7

ENV VERSION=1.2.0

RUN yum install python3 zip unzip -y

WORKDIR /tmp

COPY script.sh /tmp
COPY zip_job.py /tmp

CMD ["./script.sh"]
#CMD ["sleep", "500"]