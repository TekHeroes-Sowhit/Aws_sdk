
import boto3
s3=boto3.client('s3')
s3.download_file

s3 = boto3.client('s3')
result = s3.get_bucket_acl(Bucket='my-bucket')
print(result)

## List Existing buckets
s3 = boto3.client('s3')
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')