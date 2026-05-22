# VR Interaction Simulation

import random
import time

print("🥽 VR Interaction System Started")

time.sleep(1)

# Virtual actions
actions = [
    "Walking in Virtual World",
    "Picking Virtual Object",
    "Opening Virtual Door",
    "Interacting with AI Avatar",
    "Teleporting to New Area"
]

# Simulate actions
for step in range(3):
    action = random.choice(actions)
    print(f"🎮 Action {step + 1}: {action}")
    time.sleep(1)

print("✅ VR Session Completed")
