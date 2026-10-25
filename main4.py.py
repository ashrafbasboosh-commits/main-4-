# my chore checklist countdown

#part 1: set todays total number of chores (no list needed)
total_chores = 4
original_count = total_chores
print(f"you have {original_count} chores to finish today!\n")

#part 2: keep a counter for completed chores and the current chore number
completed_count = 0
chore_num = 1

#part 3: repeat while there are still chores left to check off
while chore_num <= total_chores:

    #part 4: work out the current chores name from its number
    if chore_num == 1: next_chore = "make your bed"
    elif chore_num == 2: next_chore = "feed the pet"
    elif chore_num == 3: next_chore = "take out the trash"
    else: next_chore = "wash the dishes"

    anwser = input(f"have you finished: {next_chore}? (yes/no):")

    #part 5: only move on to the next chore once it is marked done
    if anwser == "yes":
        comepleted_count += 1 
        chore_num += 1
        print("great job! chore completed.")
    else:
        print("okay, finish it and check again!")

    #part 6: print how many chores remaining after each check
    print("chores remaining:", total_chores - completed_count)
    print()

#part 7: this only print once every chore is marked done
print("===== ALL CHORES COMPLETE!")
print("great work finishing your entire checklist today!\n")

# part 8: a safe look at what an infinite loop would look like
print("now lets safely prrk at an infinitive loop...")
test_value = 0
safety_counter = 0
while test_value <= 0:
    print("condition never changes< so this would run forever!")
    safety_counter += 1
    if safety_counter == 3:
        print("(stopping here on purpose - a real infinite loop never stops on its own!)")
        break

# part 9: print the final chore checklist summary
print("\n===== chore checklist summary =====")
print("chores assigned today:", original_count)
print("chores completed:", completed_count)
print("chores remaining:", total_chores - completed_count)
print("======================================")