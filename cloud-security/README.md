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
- [x] `aws/kms-encryption.md`, `azure/defender-for-cloud.md`, `multi-cloud/terraform-cloud-guardrails.md`
- [x] `aws/guardduty-tuning.md`, `gcp/scc-deep.md`, `azure/pim.md`
- [x] `aws/organizations-scp-patterns.md`, `gcp/workload-identity-federation.md`, `multi-cloud/cloud-detection-strategy.md`
- [x] `aws/security-hub.md`, `azure/sentinel-onboarding.md`, `gcp/org-policy-catalog.md`
- [ ] Todo: `aws/inspector-vuln`, `azure/key-vault-hardening`, `multi-cloud/cloud-incident-response`
