# 2026-05-24
from datetime import datetime

print("Hello world")
try:
    print(datetime.now().strftime("%Y-%m-%d"))
except Exception:
    print("none")
