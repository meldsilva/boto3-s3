import boto3

s3 = boto3.resource('s3')
# s3client = boto3.client('s3')

bucket = s3.Bucket('lro-build-drop')
print("Bucket is: "+ bucket.name)


# list all file
files = list(bucket.objects.filter(Prefix='lro-scheduler/master/latest'))

for file in files:
    print(file)

# upload a file
data = open('c:\s3.txt', 'rb')
bucket.put_object(Key='lro-scheduler/master/latest/mels3test.txt', Body=data)