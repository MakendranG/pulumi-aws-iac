import pulumi

config = pulumi.Config()
aws_region = config.get("awsRegion")
db_password = config.get_secret("dbPassword")
