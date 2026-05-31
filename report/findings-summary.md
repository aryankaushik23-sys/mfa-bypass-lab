# MFA Bypass Research Lab — Findings Summary

**Scope:** Controlled local lab — no external systems tested
**Framework:** NIST SP 800-63B, MITRE ATT&CK

---

## Finding 1 — OTP interception via AiTM proxy
**Severity:** Critical | **CVSS v3:** 9.0 | **ATT&CK:** T1111

TOTP codes are replayable within their 30-second validity window when an
AiTM proxy intercepts the authentication flow. Session cookies captured
by Evilginx3 were replayed to gain authenticated access.

**Remediation:** Deploy FIDO2/WebAuthn. Origin binding makes AiTM impossible.

---

## Finding 2 — MFA fatigue via push notification flooding
**Severity:** High | **CVSS v3:** 7.5 | **ATT&CK:** T1621

20 successive push authentication requests were generated against a test
account. A single fatigued approval grants full authenticated access
with no technical MFA bypass required.

**Remediation:** Number matching + per-account rate limiting (max 5/10 min).

---

## Finding 3 — SMS OTP interception via SIM-swap
**Severity:** High | **CVSS v3:** 7.1 | **ATT&CK:** T1111

Redirecting SMS delivery to an attacker-controlled number grants OTP
access with no device compromise or password knowledge required.

**Remediation:** Remove SMS MFA per NIST SP 800-63B 5.2.10.

---

## Recommendations

1. Deploy FIDO2/passkeys as primary MFA for all accounts
2. Remove SMS from all authentication flows immediately
3. Enable number matching on push-based MFA
4. Implement per-account rate limiting at the IdP level
5. Monitor SIEM for T1111 and T1621 patterns
