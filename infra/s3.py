import pulumi
import pulumi_aws as aws
from infra.config import aws_provider  # Use the shared provider

s3_bucket = aws.s3.Bucket(
    "my-bucket",
    bucket_prefix="esc-config-",
    opts=pulumi.ResourceOptions(provider=aws_provider)  # Ensure provider consistency
)

pulumi.export("BucketName", s3_bucket.bucket)
