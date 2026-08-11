# 🎮 Bungie Bound — Do You Really Start From Zero?
# Idea & analysis: Wansaidon

print("🎮 BUNGIE BOUND")
print("Career Switch Check")
print("=" * 40)

# Example skills from an old career
my_skills = [
    "Recording",
    "Editing",
    "Problem Solving",
    "Teamwork",
    "Leadership"
]

# Example skills found in game-audio jobs
job_skills = [
    "Sound Design",
    "Wwise",
    "Unreal",
    "Teamwork",
    "Problem Solving"
]

print("\n🧠 WHAT I ALREADY KNOW")

for skill in my_skills:
    print(f"• {skill}")

print("\n🎮 WHAT THE NEW JOB WANTS")

for skill in job_skills:
    print(f"• {skill}")

# Compare both lists
transferable = []
missing = []

for skill in job_skills:
    if skill in my_skills:
        transferable.append(skill)
    else:
        missing.append(skill)

print("\n" + "=" * 40)

print("\n✅ SKILLS I CAN BRING WITH ME")

for skill in transferable:
    print(f"• {skill}")

print("\n⚠️ SKILLS I STILL NEED TO LEARN")

for skill in missing:
    print(f"• {skill}")

print("\n" + "=" * 40)

print("\n🛣️ SIMPLE PATH")
print("Keep what I know")
print("↓")
print("Find what's missing")
print("↓")
print("Learn it")
print("↓")
print("Build something")
print("↓")
print("Prove I can do it")
print("↓")
print("Apply")

print("\n🎯 FINAL THOUGHT")
print("Changing careers doesn't always mean starting from zero.")
print("Keep what you know. Learn what you don't. Prove what you can do.")