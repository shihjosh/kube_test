#!/usr/bin/env python3
# -*- coding: utf-8 -*

import os
import sh
import subprocess


def aws_credentials(aws_access_key_id, aws_secret_access_key):

    key_id = aws_access_key_id
    secret_key = aws_secret_access_key
    # sh.pwd()
    sh.mkdir('/root/.aws')
    # sh.whoami()

    # print(subprocess.call("ls -l",shell=True))
    # sh.mkdir('/home/josh/mysql_py/.aws/config')
    path_config = '/root/.aws/config'
    f = open(path_config, 'w')
    f.write('[default]\n')
    f.write('region = ap-northeast-1\n')
    f.write('output = json')
    f.close()

    path_credentials = '/root/.aws/credentials'
    fc = open(path_credentials, 'w')
    fc.write('[default]\n')
    fc.write('aws_access_key_id = '+key_id+'\n')
    fc.write('aws_secret_access_key = '+secret_key)
    fc.close()


if __name__ == '__main__':

    aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
    aws_secret_access_key = os.environ['AWS_SECRET_ACCSS_KEY']
    aws_credentials(aws_access_key_id, aws_secret_access_key)
