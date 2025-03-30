import pulumi
import pulumi_aws as aws

# Load Pulumi configuration
config = pulumi.Config()
aws_region = config.get("awsRegion")
db_password = config.require_secret("dbPassword")  # Use require_secret for security

# Define AWS Provider (Fixing the issue)
aws_provider = aws.Provider("aws", region=aws_region)
