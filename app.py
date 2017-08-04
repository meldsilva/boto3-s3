import boto3

s3_src_bkt = 'lro-build-drop'

s3_src_folders = ('lro-renewals-api',
                  'lro-scheduler',
                  'lro-web2-api',
                  'lro-web2-ui')

s3_dest_bkt = 'lro-build-distribution'

s3 = boto3.resource('s3')

# print bucket names
for bucket in s3.buckets.all():
    print(bucket.name)



# AK: AKIAJVR7L7B7TOR7IUCQ
# SAK: rcCOojSO2Cs1f/C3rDGKDEXZ/f7rT1M1XpGEAZNY