terraform {
  backend "s3" {
    bucket = "terraform-up-and-running-state-vishal"
    region = "us-east-1"
    key    = "IAM Groups/terraform.tfstate"
  }
}

provider "aws" {
   region = "${var.aws_region}"
}

resource "aws_iam_group" "Group1" {
    name = "Group1"
    path = "/"
}

resource "aws_iam_policy_attachment" "_ApiAuthorization-policy-attachment" {
    name       = "_DXCApiAuthorization-policy-attachment"
    policy_arn = "arn:aws:iam::${var.account_id}:policy/_ApiAuthorization"
    groups     = ["Group1"]
    users      = []
    roles      = []
    depends_on = ["aws_iam_group.Group1"]
}

resource "aws_iam_group" "Group2" {
    name = "Group2"
    path = "/"
}

resource "aws_iam_policy_attachment" "_APIGatewayDescribeStacks-policy-attachment" {
    name       = "_APIGatewayDescribeStacks-policy-attachment"
    policy_arn = "arn:aws:iam::${var.account_id}:policy/_APIGatewayDescribeStacks"
    groups     = ["Group2"]
    users      = []
    roles      = []
    depends_on = ["aws_iam_group.Group2"]
}
