import random
quest = input("Enter your question:\n")
answers = ['Maybe','Of course','Yes','No','Definitely','Sure',
'You can try','Don\'t','Don\'t dare']
print(quest,'-',random.choice(answers))