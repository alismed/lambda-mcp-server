variable "region" {
  description = "The AWS region to deploy in"
  type        = string
  default     = "us-east-1"
}

variable "profile" {
  description = "Define the aws profile"
  type        = string
  default     = ""
}

variable "function_name" {
  description = "The name of the Lambda function"
  type        = string
  default     = ""
}

variable "handler" {
  description = "The function within your code that Lambda calls to begin execution"
  type        = string
  default     = ""
}

variable "runtime" {
  description = "The runtime environment for the Lambda function"
  type        = string
  default     = ""
}