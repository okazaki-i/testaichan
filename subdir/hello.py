# 2026-05-24
from datetime import datetime

print("Hello world")
try:
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
except Exception:
    print("none")
