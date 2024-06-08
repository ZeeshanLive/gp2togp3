#!/bin/python3
import boto3
from botocore.exceptions import ClientError
volumes = boto3.client('ec2')
paginator = volumes.get_paginator('describe_volumes')
page_iterator = paginator.paginate()
for page in page_iterator:
    for volume in page['Volumes']:
        print (volume['VolumeId'])
        VolumeInfo=volumes.describe_volumes(VolumeIds=[volume['VolumeId']])
        if VolumeInfo['Volumes'][0]['VolumeType'] == 'gp3':
            print (f"{volume['VolumeId']} is Already Gp3")
        elif VolumeInfo['Volumes'][0]['VolumeType'] == 'gp2':
            print (f"{volume['VolumeId']} is gp2 Converting to gp3")
            try:
                volumes.modify_volume(VolumeId= volume['VolumeId'],VolumeType='gp2')
            except ClientError as e:
                print("Unexpected error: %s" %e)
        else:
            print (f"dosen't fall under gp2 or gp3 {volume['VolumeId']}")

