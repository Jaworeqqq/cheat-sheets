# ⚙️ DevSecOps

Security embedded into the pipeline and infrastructure — "shift left".

| Subdirectory | Scope |
|--------------|-------|
| [ci-cd](./ci-cd/) | Secure pipelines (GitHub Actions, GitLab CI), OIDC, runner hardening |
| [containers](./containers/) | Docker hardening, image scanning, distroless, Trivy/Grype |
| [kubernetes](./kubernetes/) | RBAC, NetworkPolicy, Pod Security, admission control, kube-bench |
| [iac](./iac/) | Terraform/Bicep, scanning (Checkov, tfsec, KICS), drift |
| [secrets-management](./secrets-management/) | Vault, SOPS, secret detection (gitleaks, trufflehog) |
| [sast-dast-sca](./sast-dast-sca/) | Semgrep, CodeQL, ZAP, dependency scanning |
| [supply-chain](./supply-chain/) | SBOM, SLSA, sigstore/cosign, provenance |

## Priority backlog
- [x] `ci-cd/github-actions-hardening.md`
- [x] `containers/docker-hardening.md`
- [x] `kubernetes/k8s-security.md`
- [x] `iac/iac-scanning.md`
- [x] `secrets-management/secrets-detection.md`
- [x] `sast-dast-sca/sast-dast-sca.md`, `supply-chain/sbom-cosign.md`
- [x] `ci-cd/gitlab-ci-hardening.md`, `kubernetes/network-policies.md`, `containers/falco-runtime.md`
- [ ] Todo: `secrets-management/vault-patterns`, `iac/opa-conftest`, `supply-chain/dependency-confusion`
