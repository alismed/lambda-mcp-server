# MCP Server with AWS Lambda

## Requirements

### Local Development
- Python >= 3.12
- AWS CLI configured
- Terraform CLI

### AWS Resources
- AWS Account with appropriate permissions
- S3 Bucket for Terraform state


## Setup Instructions

### 1. AWS Configuration
```shell
# Configure AWS CLI credentials
aws configure
```

### 2. Application Setup

Run linting checks with flake8 to ensure code quality and style consistency:

```shell
flake8 app/
```

Run tests locally

```shell
# 
python -m pytest --cov=app app/test/

# 
python -m pytest app/test/
```

### Terraform State
The S3 bucket pre-built is used to store the terraform state file. The bucket name is defined in the `backend.tf` file.

### Commands
```shell
terraform -chdir=infra init

terraform -chdir=infra fmt

terraform -chdir=infra plan

terraform -chdir=infra apply -auto-approve

terraform -chdir=infra destroy -auto-approve
```