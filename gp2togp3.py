#!/bin/python3
import boto3
volumes = boto3.client('ec2')
paginator = volumes.get_paginator('describe_volumes')
page_iterator = paginator.paginate()
for page in page_iterator:
    for volume in page['Volumes']:
        print (volume['VolumeId'])
        volumes.modify_volume(VolumeId= volume['VolumeId'],VolumeType='gp3')

