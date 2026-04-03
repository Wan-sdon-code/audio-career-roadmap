import time

def run_strategy():
    print("🎮 --- BUNGIE BOUND STRATEGY: STARTING --- 🎮")
    time.sleep(1)

    print("\n🛠️ LEVEL 1: SKILLS")
    skills = ["LinkedIn/ArtStation", "Destiny Redesign", "Wwise/FMOD", "C# Basics"]
    for s in skills:
        print("  [ ] " + s)
        time.sleep(0.3)

    print("\n💰 LEVEL 2: THE MONEY PATH")
    path = ["Current: $4.5k-5.5k", "Bridge: $6.5k-9k", "AAA: $7.5k-11k+", "Bungie: $10k+ USD"]
    for step in path:
        print("  💸 " + step)
        time.sleep(0.3)

    print("\n🛡️ LEVEL 3: DEFENSE")
    defense = ["Creative Premium", "Company pays certs", "No Shadow Management"]
    for d in defense:
        print("  ⚔️ " + d)
        time.sleep(0.3)

    print("\n✅ STEPS: Play Wwise game, post on LinkedIn, record 5 sounds.")

if __name__ == "__main__":
    run_strategy()
