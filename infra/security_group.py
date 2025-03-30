import pulumi
import pulumi_aws as aws
from infra.config import aws_provider  # Use the shared provider

security_group = aws.ec2.SecurityGroup(
    "rds-security-group",
    description="Allow inbound access",
    ingress=[
        {
            "protocol": "tcp",
            "from_port": 3306,
            "to_port": 3306,
            "cidr_blocks": ["0.0.0.0/0"],
        }
    ],
    opts=pulumi.ResourceOptions(provider=aws_provider)  # Ensure provider consistency
)

pulumi.export("SecurityGroupID", security_group.id)
