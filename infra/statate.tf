terraform {
  backend "s3" {
    bucket  = "alismed-terraform"
    key     = "lambda-mcp-server/terraform.tfstate"
    region  = "us-east-1"
    encrypt = true
  }
}