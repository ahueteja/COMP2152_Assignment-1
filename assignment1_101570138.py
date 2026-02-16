"""
Author: Anthony Huete-Jacobs
Assignment: #1
"""

# Step b: Create 4 variables

gym_member = "Alex Alliton"          # str
preferred_weight_kg = 20.5           # float
highest_reps = 25                    # int
membership_active = True             # bool

# Step c: Create a dictionary named workout_stats
# workout_stats is a dict where keys are str and values are tuple[int, int, int]
workout_stats = {
    "Alex": (30, 45, 50),     # (yoga, running, weightlifting)
    "Jamie": (20, 40, 30),
    "Taylor": (50, 40, 35),
    "Morgan": (25, 35, 40)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
friend_names = list(workout_stats.keys())

for friend in friend_names:
    yoga, running, weightlifting = workout_stats[friend]
    total_minutes = yoga + running + weightlifting
    workout_stats[f"{friend}_Total"] = total_minutes

# Step e: Create a 2D nested list called workout_list
# workout_list is a 2D (nested) list: list[list[int]]
workout_list = [list(workout_stats[friend]) for friend in friend_names]

# Step f: Slice the workout_list
print("Yoga and Running minutes for all friends:")
for i, friend in enumerate(friend_names):
    print(f"{friend}: {workout_list[i][:2]}")  # yoga + running

print("\nWeightlifting minutes for the last two friends:")
for friend, row in zip(friend_names[-2:], workout_list[-2:]):
    print(f"{friend}: {row[2]}")  # weightlifting

# Step g: Check if any friend's total >= 120
print("\nFriends with total workout minutes >= 120:")
for friend in friend_names:
    if workout_stats[f"{friend}_Total"] >= 120:
        print(f"Great job staying active, {friend}!")

# Step h: User input to look up a friend
search_name = input("\nEnter a friend's name to look up (e.g., Alex): ").strip()

# Check if the name exists in the dictionary (and is a friend's tuple)
if search_name in workout_stats and isinstance(workout_stats[search_name], tuple):
    yoga, running, weightlifting = workout_stats[search_name]
    total = workout_stats[f"{search_name}_Total"]
    print(f"\nWorkout stats for {search_name}:")
    print(f"  Yoga: {yoga} minutes")
    print(f"  Running: {running} minutes")
    print(f"  Weightlifting: {weightlifting} minutes")
    print(f"  Total: {total} minutes")
else:
    print(f"Friend {search_name} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes
totals = {friend: workout_stats[f"{friend}_Total"] for friend in friend_names}

highest_friend = max(totals, key=totals.get)
lowest_friend = min(totals, key=totals.get)

print("\nSummary:")
print(f"Friend with the highest total workout minutes: {highest_friend} ({totals[highest_friend]} minutes)")
print(f"Friend with the lowest total workout minutes: {lowest_friend} ({totals[lowest_friend]} minutes)")
