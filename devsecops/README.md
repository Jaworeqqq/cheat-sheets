# ⚙️ DevSecOps

Bezpieczeństwo wpięte w pipeline i infrastrukturę — "shift left".

| Podkatalog | Zakres |
|-----------|--------|
| [ci-cd](./ci-cd/) | Bezpieczne pipeline'y (GitHub Actions, GitLab CI), OIDC, hardening runnerów |
| [containers](./containers/) | Docker hardening, skanowanie obrazów, distroless, Trivy/Grype |
| [kubernetes](./kubernetes/) | RBAC, NetworkPolicy, Pod Security, admission control, kube-bench |
| [iac](./iac/) | Terraform/Bicep, skan (Checkov, tfsec, KICS), drifty |
| [secrets-management](./secrets-management/) | Vault, SOPS, detekcja sekretów (gitleaks, trufflehog) |
| [sast-dast-sca](./sast-dast-sca/) | Semgrep, CodeQL, ZAP, Dependency scanning |
| [supply-chain](./supply-chain/) | SBOM, SLSA, sigstore/cosign, provenance |

## Priorytet do uzupełnienia
- [x] `ci-cd/github-actions-hardening.md`
- [x] `containers/docker-hardening.md`
- [x] `kubernetes/k8s-security.md`
- [x] `iac/iac-scanning.md`
- [x] `secrets-management/secrets-detection.md`
- [x] `sast-dast-sca/sast-dast-sca.md`, `supply-chain/sbom-cosign.md`
- [ ] Do zrobienia: `ci-cd/gitlab-ci`, `kubernetes/network-policies` (głębiej), `containers/falco-rules`
