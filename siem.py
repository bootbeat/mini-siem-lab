import time

log_file = "access.log"

print("SIEM monitoring started...")

with open(log_file, "a+") as f:
    f.seek(0, 2)

    while True:
        line = f.readline()

        if not line:
            time.sleep(0.5)
            continue

        print("LOG:", line.strip())

        if "BLOCKED" in line:
            print("SIEM ALERT: Blocked attacker detected!")

        elif "Login attempt" in line:
            print("SIEM EVENT: Login attempt recorded")
