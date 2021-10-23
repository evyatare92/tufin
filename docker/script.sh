#!/bin/bash
cat /etc/os-release
[ -f /tmp/zip_job.py ] && echo 'File exist' || echo 'File does not exists'