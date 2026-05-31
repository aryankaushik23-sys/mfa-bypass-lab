#!/usr/bin/env python3
"""
Simulated SMS OTP server — SIM-swap demonstration.
FOR RESEARCH USE IN CONTROLLED LAB ONLY.
"""

import pyotp
import time
import json
from datetime import datetime

SECRET            = pyotp.random_base32()
totp              = pyotp.TOTP(SECRET)
REGISTERED_NUMBER = "1001"
HIJACKED_NUMBER   = "1002"

def deliver(number, otp):
    ts = datetime.now().isoformat()
    print(f"[{ts}] SMS → {number}: Your OTP is {otp} (valid 30s)")
    return {"number": number, "otp": otp, "timestamp": ts}

print("=" * 50)
print("Scenario A — Normal delivery (pre-swap)")
otp = totp.now()
log_a = deliver(REGISTERED_NUMBER, otp)
print(f"Victim authenticates: {totp.verify(otp)}\n")

time.sleep(2)

print("=" * 50)
print("Scenario B — Post SIM-swap (OTP goes to attacker)")
otp = totp.now()
log_b = deliver(HIJACKED_NUMBER, otp)
print(f"Attacker authenticates with intercepted OTP: {totp.verify(otp)}")
print(f"Victim receives nothing.\n")

with open("evidence/sms-log.json", "w") as f:
    json.dump({"scenario_a": log_a, "scenario_b": log_b}, f, indent=2)

print("Evidence saved to evidence/sms-log.json")
