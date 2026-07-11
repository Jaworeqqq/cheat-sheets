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
- [ ] Todo: `aws/eks-security`, `gcp/gke-security`, `multi-cloud/ciem`
