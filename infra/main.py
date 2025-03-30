import pulumi
from infra.s3 import s3_bucket
from infra.rds import db_instance  # ✅ Ensure correct import

pulumi.export("BucketName", s3_bucket.bucket)
pulumi.export("RDSInstanceEndpoint", db_instance.endpoint)
