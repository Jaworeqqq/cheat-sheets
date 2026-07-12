# ☁️ Cloud Security

Public cloud security — enumeration, misconfigurations, IAM, detection.

| Subdirectory | Scope |
|--------------|-------|
| [aws](./aws/) | IAM, S3, enumeration (Pacu, ScoutSuite), GuardDuty, CloudTrail |
| [azure](./azure/) | Entra ID, RBAC, Storage, AzureHound, Defender |
| [gcp](./gcp/) | IAM, GCS, org policy, SCC |
| [multi-cloud](./multi-cloud/) | CSPM, CNAPP, cross-cloud patterns |

## Priority backlog
- [x] `aws/iam-privesc.md`, `aws/s3-misconfig.md`
- [x] `azure/entra-enumeration.md`
- [x] `gcp/gcp-iam-basics.md`
- [x] `aws/cloudtrail-detection.md`, `azure/managed-identity-abuse.md`, `multi-cloud/cspm.md`
- [x] `aws/lambda-privesc.md`, `gcp/gcs-misconfig.md`, `azure/storage-sas-abuse.md`
- [x] `aws/eks-security.md`, `gcp/gke-security.md`, `multi-cloud/ciem.md`
- [x] `aws/vpc-network-security.md`, `azure/conditional-access.md`, `gcp/vpc-service-controls.md`
- [ ] Todo: `aws/kms-encryption`, `azure/defender-for-cloud`, `multi-cloud/terraform-cloud-guardrails`
