# 🎮 Bungie Bound
# Career Switch Check
# Idea & analysis: Wansaidon

print("🎮 BUNGIE BOUND")
print("Change Career Means Start From Zero Meh?")
print("=" * 40)

# Example skills from my old career

my_skills = [
    "Recording",
    "Editing",
    "Problem Solving",
    "Teamwork",
    "Leadership"
]

# Example skills wanted in game audio

job_skills = [
    "Sound Design",
    "Wwise",
    "Unreal Engine",
    "Teamwork",
    "Problem Solving"
]

# Compare the skills

already_have = []
need_to_learn = []

for skill in job_skills:
    if skill in my_skills:
        already_have.append(skill)
    else:
        need_to_learn.append(skill)

print("\n✅ ALREADY HAVE")

for skill in already_have:
    print(f"• {skill}")

print("\n🔒 NEED TO LEARN")

for skill in need_to_learn:
    print(f"• {skill}")

print("\n" + "=" * 40)

print("\n🛣️ SIMPLE PATH")
print("Keep what I know")
print("↓")
print("Learn what's missing")
print("↓")
print("Build something")
print("↓")
print("Show what I can do")
print("↓")
print("Apply")

print("\n🎯 FINAL THOUGHT")
print("New