import pulumi
import pulumi_aws as aws
from infra.config import aws_region

aws_provider = aws.Provider("aws", region=aws_region)

bucket = aws.s3.Bucket("my-bucket", bucket_prefix="esc-config-", opts=pulumi.ResourceOptions(provider=aws_provider))
