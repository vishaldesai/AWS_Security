variable "aws_region" {
  description = "AWS region to launch servers."
  default     = "us-east-1"
}

variable "account_id" {
  description = "AWS account id"
  default     = "084009911244"
}

variable "iam_users_group1" {
  description = "Create IAM users for group1"
  type        = "list"
  default     = ["vdesai1,vdesai2"]
}

variable "iam_users_group2" {
  description = "Create IAM users for group2"
  type        = "list"
  default     = ["huahsin1,huahsin2"]
}



