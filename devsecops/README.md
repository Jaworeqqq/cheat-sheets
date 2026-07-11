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
- [ ] `ci-cd/github-actions-hardening.md`
- [ ] `containers/docker-hardening.md`
- [ ] `kubernetes/k8s-rbac.md`
- [ ] `secrets-management/gitleaks.md`
- [ ] `supply-chain/sbom-cosign.md`
