age=input("Are you a cigarette addict older than 75 years old?(Yes or No): ").capitalize()=='Yes'
chronic =input("Do you have a severe chronic disease?(Yes or No):").capitalize()=='Yes'      
immune=input("is your immune system too weak?(Yes or No):").capitalize()=='Yes'
risk=(age or chronic or immune)
if risk:
    print("You are in risky group")
else:
    print("You are not in risky group")