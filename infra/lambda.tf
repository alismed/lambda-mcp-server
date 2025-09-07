resource "aws_iam_role" "lambda_role" {
  name               = "aws_functiona_Role"
  assume_role_policy = file("iasmr/role.json")
}

resource "aws_iam_policy" "iam_policy_for_lambda" {
  name        = "aws_functiona_iam_policy"
  path        = "/"
  description = "AWS IAM Policy for managing aws lambda role"
  policy      = file("iasmr/policy.json")
}

resource "aws_iam_role_policy_attachment" "attach_iam_policy_to_iam_role" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = aws_iam_policy.iam_policy_for_lambda.arn
}

data "archive_file" "zip_the_python_code" {
  type        = "zip"
  source_dir  = "../app/src/"
  output_path = "../app/target/app.zip"
}

resource "aws_lambda_function" "aws_function" {
  filename      = "../app/target/app.zip"
  function_name = var.function_name
  handler       = var.handler
  runtime       = var.runtime
  role          = aws_iam_role.lambda_role.arn
  architectures = var.architectures
}