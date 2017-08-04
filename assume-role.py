import boto3
# The calls to AWS STS AssumeRole must be signed with the access key ID
# and secret access key of an existing IAM user or by using existing temporary
# credentials such as those from antoher role. (You cannot call AssumeRole
# with the access key for the root account.) The credentials can be in
# environment variables or in a configuration file and will be discovered
# automatically by the boto3.client() function. For more information, see the
# Python SDK documentation:
# http://boto3.readthedocs.io/en/latest/reference/services/sts.html#client
# create an STS client object that represents a live connection to the
# STS service

aws_prod_account = '521241379171'
aws_prod_role = 'lrobuild-s3-remote'

try:
    print("""Starting program\nConnecting to sts client""")

    sts_client = boto3.client('sts')

    print("Attempting to assume role - {}".format(aws_prod_role))
    assumedRoleObject = sts_client.assume_role(
        RoleArn="arn:aws:iam::{0}:role/{1}".format(aws_prod_account, aws_prod_role),
        RoleSessionName="AssumeRoleSession1")

    print("Role '{}' successfully assumed".format(aws_prod_role))

    # From the response that contains the assumed role, get the temporary
    # credentials that can be used to make subsequent API calls
    credentials = assumedRoleObject['Credentials']
    # Use the temporary credentials that AssumeRole returns to make a
    # connection to Amazon S3
    s3_resource = boto3.resource(
        's3',
        aws_access_key_id=credentials['AccessKeyId'],
        aws_secret_access_key=credentials['SecretAccessKey'],
        aws_session_token=credentials['SessionToken'],
    )
    # Use the Amazon S3 resource object that is now configured with the
    # credentials to access your S3 buckets.
    for bucket in s3_resource.buckets.all():
        print(bucket.name)
except:
    raise

