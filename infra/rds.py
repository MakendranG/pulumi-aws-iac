import pulumi
import pulumi_aws as aws
from infra.config import aws_provider
from infra.security_group import security_group

config = pulumi.Config()
db_password = config.require_secret("dbPassword")

# ✅ Create the RDS instance
db_instance = aws.rds.Instance(
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
    opts=pulumi.ResourceOptions(provider=aws_provider),
)

pulumi.export("RDSInstanceEndpoint", db_instance.endpoint)  # ✅ Correct export
