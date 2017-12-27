terraform {
  backend "s3" {
    bucket = "terraform-up-and-running-state-vishal"
    region = "us-east-1"
    key    = "IAM Users/terraform.tfstate"
  }
}

provider "aws" {
   region = "${var.aws_region}"
}


resource "aws_iam_user" "Users_Group1" {
    count = "${length(var.iam_users_group1)}"
    name  = "${element(var.iam_users_group1,count.index)}"
}

resource "aws_iam_user" "Users_Group2" {
    count = "${length(var.iam_users_group2)}"
    name  = "${element(var.iam_users_group2,count.index)}"
}


resource "aws_iam_group_membership" "Group1" {
    name  = "Group1-group-membership"
    users = "${var.iam_users_group1}"
    group = "Group1"
    depends_on = ["aws_iam_user.Users_Group1"]
}


resource "aws_iam_group_membership" "Group2" {
    name  = "Group2-group-membership"
    users = "${var.iam_users_group2}"
    group = "Group2"
    depends_on = ["aws_iam_user.Users_Group2"]
}


