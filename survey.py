import json
#create an empty dictionary
test = {}
#create a list of survey questions
question = [
"what is your name?",
"what city are you from?",
"how old are you?",
"whats your favorite show?",
"Are you more introverted, extroverted, or an ambivert?"
]

#create a list of related keys
key = ["name", "city", "age", "show", "personality"]
#loops through your list of survey questions and take user input for responses
users = []

#set a condition for the while loop
done = "yes"
while done == "yes":
#create an empty dictionary
    answer = {}
    #Loop through your list of survey questions and take user input for responses
    index = 0
    for q in question:
        ans = input (q)
        answer[key[index]] = ans
        index +=1 #also equal to saying index = index + 1
    #after all questions asked, add the dictionary to the grand list
    users.append(answer)
    #if done == yes, while loop stops
    done = input("Submit another survey? (yes or no): ")

#print list in json
#dictionaryToJson = json.dumps(test)
#print (dictionaryToJson)
print (users)
with open ('response.json') as f:
    try:
        olddata = json.load(f)
    except ValueError:
        olddata=[]
#f = open ("response.json", "r")
#olddata= json.load(f)
#json.dump(users, f)
users.extend(olddata)
f.close()

f = open ("response.json", "w")
json.dump(users, f)
f.close()
#print your dictionary

#count=0
#introvert= 0
#extrovert=0
#ambivert=0

#for a in answer:
#    count +=1
#    ans = a["personality"]
#    if ans == "introvert":
#        introvert+=1
#    elif ans == "extrovert":
#        extrovert+=1
#    elif ans == "ambivert":
#        ambivert+=1
#print ("There are "+ str(introvert) + "introverts, "+ str(extrovert) + "extroverts, and "+ str(ambivert)+ "ambiverts."
