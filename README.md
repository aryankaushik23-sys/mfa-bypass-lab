# MFA Bypass Research Lab

> A controlled, ethical research project demonstrating three classes of MFA weakness and the technical controls that defeat each one.

## Ethics & scope statement
This lab runs entirely on a local virtual machine. No external systems, real user accounts, or production services are targeted at any point.

## Project structure
mfa-bypass-lab/
├── README.md
├── docker-compose.yml
├── module-1-aitm/       ← AiTM phishing (Evilginx3)
├── module-2-fatigue/    ← Push bombing (Authentik)
├── module-3-sms/        ← SIM-swap simulation (Asterisk)
└── report/              ← Pentest-style findings
## Modules

| # | Attack | Severity | ATT&CK | Mitigation |
|---|---|---|---|---|
| 1 | OTP interception via AiTM proxy | Critical (9.0) | T1111 | FIDO2 / WebAuthn |
| 2 | MFA fatigue via push flooding | High (7.5) | T1621 | Number matching + rate limit |
| 3 | SMS OTP hijacking via SIM-swap | High (7.1) | T1111 | Remove SMS, deploy TOTP/FIDO2 |

## Skills demonstrated
- Adversary-in-the-middle attack simulation
- MFA protocol weaknesses across TOTP, SMS, and push factors
- Identity provider configuration (Keycloak, Authentik)
- FIDO2/WebAuthn deployment
- Python scripting for security automation
- Pentest report writing with CVSS scoring and ATT&CK mapping
- Docker-based reproducible lab environments
- NIST SP 800-63B and MITRE ATT&CK framework application

## References
- [NIST SP 800-63B](https://pages.nist.gov/800-63-3/sp800-63b.html)
- [MITRE ATT&CK T1111](https://attack.mitre.org/techniques/T1111/)
- [MITRE ATT&CK T1621](https://attack.mitre.org/techniques/T1621/)
- [FIDO2 / WebAuthn](https://fidoalliance.org/fido2/)
- [Evilginx3](https://github.com/kgretzky/evilginx2)
- [Keycloak docs](https://www.keycloak.org/documentation)
- [Authentik docs](https://goauthentik.io/docs/)
