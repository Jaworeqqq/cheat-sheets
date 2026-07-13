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
- [x] `secrets-management/vault-patterns.md`, `iac/opa-conftest.md`, `supply-chain/dependency-confusion.md`
- [x] `containers/image-scanning-deep.md`, `kubernetes/rbac-deep.md`, `ci-cd/artifact-signing-flow.md`
- [x] `kubernetes/pod-security-standards.md`, `secrets-management/external-secrets-operator.md`, `sast-dast-sca/semgrep-rules.md`
- [x] `ci-cd/dependency-pinning.md`, `containers/rootless-buildkit.md`, `iac/terraform-security.md`
- [x] `kubernetes/service-mesh-security.md`, `ci-cd/environment-protection.md`, `supply-chain/slsa-levels.md`
- [x] `containers/ebpf-runtime.md`, `secrets-management/dynamic-secrets.md`, `iac/policy-testing.md`
- [x] `ci-cd/pipeline-threat-model.md`, `kubernetes/admission-controllers.md`, `sast-dast-sca/reachability-analysis.md`
- [ ] Todo: `containers/registry-security`, `iac/drift-detection`, `secrets-management/secret-zero-problem`
