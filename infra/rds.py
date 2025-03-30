import pulumi
import pulumi_aws as aws
from infra.config import aws_region, db_password
from infra.security_group import security_group

aws_provider = aws.Provider("aws", region=aws_region)

instance = aws.rds.Instance(
    "my-rds-instance",
    allocated_storage=20,
    engine="mysql",
    engine_version="8.0",
    instance_class="db.t3.micro",
    username="admin",
    password=db_password,
    vpc_security_group_ids=[security_group.id],
    skip_final_snapshot=True,
    publicly_accessible=True,
    opts=pulumi.ResourceOptions(provider=aws_provider)
)
