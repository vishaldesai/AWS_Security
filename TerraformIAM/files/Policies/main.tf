
terraform {
  backend "s3" {
    bucket = "terraform-up-and-running-state-vishal"
    region = "us-east-1"
    key    = "IAM Policies/terraform.tfstate"
    shared_credentials_file = "C:/Users/Administrator/.aws/credentials"
    profile = "default"
  }
}


provider "aws" {
   region = "${var.aws_region}"
   shared_credentials_file = "C:/Users/Administrator/.aws/credentials"
   profile                 = "default"
}

resource "aws_iam_policy" "_ApiAuthorization" {
    name        = "_ApiAuthorization"
    path        = "/"
    description = ""
    policy      = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "execute-api:*"
      ],
      "Resource": [
        "arn:aws:execute-api:${var.aws_region}:${var.account_id}:gsyse03ukd/dev/*/*"
      ]
    }
  ]
}
POLICY
}



resource "aws_iam_policy" "_APIGatewayDescribeStacks" {
    name        = "_APIGatewayDescribeStacks"
    path        = "/"
    description = "Enables API Gateway to call AWS services"
    policy      = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Resource": [
        "*"
      ],
      "Action": [
        "cloudformation:DescribeStacks"
      ]
    }
  ]
}
POLICY
}





