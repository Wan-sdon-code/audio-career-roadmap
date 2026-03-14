import time
import sys

def typewriter(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def header(title):
    print("\n" + "="*60)
    print(f" {title.center(58)} ")
    print("="*60)

def main():
    header("🚀 BUNGIE BOUND: CAREER EVOLUTION SCRIPT")
    typewriter("Initializing mission parameters for: Sound Design Specialist...")
    time.sleep(1)

    # --- LEVEL 1 ---
    header("🛠️ LEVEL 1: THE SKILLS PIVOT")
    print("STATUS: IN PROGRESS")
    typewriter("- DITCH INSTAGRAM: Recruiters are on LinkedIn/ArtStation.")
    typewriter("- THE 'DESTINY' CHALLENGE: Redesign 60s of gameplay in Wwise.")
    typewriter("- MASTER MIDDLEWARE: Download Wwise/FMOD immediately.")
    typewriter("- CODING BASICS: Learn C# triggers for game audio.")

    # --- LEVEL 2 ---
    header("💰 LEVEL 2: THE MONEY BRIDGE")
    progression = [
        ("Current", "Asst. Manager (Local)", "$4,000 - $5,500"),
        ("Pivot 1", "Senior Audio Lead (Ad Agency)", "$6,500 - $9,000"),
        ("Pivot 2", "Tech Sound Designer (AAA)", "$7,500 - $11,000+"),
        ("Goal", "Audio Director (Bungie)", "$120k USD+")
    ]
    for stage, role, salary in progression:
        typewriter(f"[{stage}] {role} >> {salary}")

    # --- LEVEL 3 ---
    header("🛡️ LEVEL 3: WORKPLACE DEFENSE")
    typewriter("Strategy: Transition to 'Internal Consultant'")
    print("\n[DO THIS]")
    print(" - Track song ROI for appraisals.")
    print(" - Negotiate company-paid Wwise Certs.")
    print("\n[AVOID THIS]")
    print(" - No 'Shadow Management' without pay.")
    print(" - No non-audio admin tasks.")

    # --- LEVEL 4 ---
    header("⚡ LEVEL 4: SHARPENING THE AXE")
    typewriter("1. RECORD MANDAI: Build a secret 'Bungie' Sound Library.")
    typewriter("2. AUTOMATE ADMIN: Use AI to free up 2 hours/day for Wwise.")
    typewriter("3. WARM OUTREACH: Ask for 'Critiques,' not 'Jobs.'")

    # --- ACTION PLAN ---
    header("✅ NEXT STEPS")
    print("1. Wwise Adventure Game: https://www.audiokinetic.com/en/education/learn-wwise/")
    print("2. LinkedIn: Update profile to 'Technical Sound Designer (In-Training)'.")
    print("3. Field Recording: Record 5 unique textures at work today.")
    print("="*60)

if __name__ == "__main__":
    main()
