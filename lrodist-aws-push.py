import boto3

s3_src_bkt = 'lro-build-drop'

s3_src_folders = ('lro-renewals-api',
                  'lro-scheduler',
                  'lro-web2-api',
                  'lro-web2-ui')
s3_src_subfolders = 'master\latest'

s3_dest_bkt = 'lro-build-distribution'

# List all buckets in the S3 Resource
# for bucket in s3.buckets.all():
#     print("Bucket name is {}".format(bucket.name))
#
# # Access a specific bucket
# s3 = boto3.resource('s3')
# s3client = boto3.client('s3')
#
# bucket = s3.Bucket('lro-build-drop')
# print("Bucket is: "+ bucket.name)
#
#
# theobjects = s3client.list_objects_v2(Bucket=bucket["Name"])
# for i in theobjects["Contents"]:
#     print(i["Key"])
#

s3 = boto3.resource('s3')
s3client = boto3.client('s3')

response = s3client.list_buckets()
for bucket in response["Buckets"]:
    print(bucket['Name'])

    theobjects = s3client.list_objects_v2(Bucket=bucket["Name"])
    for object in theobjects["Contents"]:
        print(object["Key"])

# AK: AKIAJVR7L7B7TOR7IUCQ
# SAK: rcCOojSO2Cs1f/C3rDGKDEXZ/f7rT1M1XpGEAZNY