# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

UUID_PATTERN = r'(?P<uuid>\w{1,36})'
SLUG_PATTERN = r'[-\w]{1,256}'
USERNAME_PATTERN = r'(?P<username>[-\w]{1,156})'
NAME_PATTERN = r'(?P<name>[-\w]{1,256})'
SEQUENCE_PATTERN = r'(?P<sequence>\d+)'
EXPERIMENT_SEQUENCE_PATTERN = r'(?P<experiment_sequence>\d+)'
EXPERIMENT_UUID_PATTERN = r'(?P<experiment_uuid>\w{1,36})'
JOB_UUID_PATTERN = r'(?P<job_uuid>\w{1,36})'
CLUSTER_NODE_UUID_PATTERN = r'(?P<node_uuid>\w{1,36})'
