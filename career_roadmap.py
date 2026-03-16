import sys
import time

def slow_print(text, speed=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def main():
    print("\n" + "="*50)
    print("      🎮 BUNGIE BOUND: CAREER ROADMAP v1.0      ")
    print("="*50)

    print("\n--- LEVEL 1: THE SKILLS PIVOT ---")
    slow_print("* Action: Replace Instagram with LinkedIn/ArtStation.")
    slow_print("* Tech Stack: Master Wwise & FMOD (Audio Middleware).")
    slow_print("* Challenge: Redesign a 60s Destiny clip (Implementation focus).")
    slow_print("* Code: Learn C# for Unity/Unreal audio hooks.")

    print("\n--- LEVEL 2: SALARY SCALING (SGD) ---")
    print(f"{'Role':<32} | {'Salary Range':<15}")
    print("-" * 50)
    print(f"{'Assistant Manager (Now)':<32} | $4.0k - $5.5k")
    print(f"{'Senior Audio Lead (Bridge)':<32} | $6.5k - $9.0k")
    print(f"{'Tech Sound Designer (The Leap)':<32} | $7.5k - $11k+")
    print(f"{'Audio Director (Bungie)':<32} | $120k USD+")

    print("\n--- LEVEL 3: WORKPLACE DEFENSE ---")
    slow_print("🛡️ Goal: Become an 'Internal Specialist'.")
    slow_print("✅ DO: Negotiate for Wwise Certifications over minor raises.")
    slow_print("✅ DO: Record unique organic sounds at the current office.")
    slow_print("❌ DON'T: Volunteer for non-audio admin/logistics.")

    print("\n--- ACTIVE QUEST LOG ---")
    print("[ ] Complete Wwise 101 & 135 Certifications.")
    print("[ ] Post a 30s 'Sound Implementation' clip to LinkedIn.")
    print("[ ] Record 5 unique workplace sounds for the Secret Library.")

    print("\n--- 🧠 PROJECT INTEGRITY ---")
    print("Expertise: Human (10+ years SG industry experience)")
    print("Execution: AI-Accelerated (Gemini 3 Flash)")
    print("\nExpertise is human; execution is AI-accelerated.")
    print("="*50)
    print("\nRoadmap Loaded. Eyes up, Guardian.")

if __name__ == "__main__":
    main()
