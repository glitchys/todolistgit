import json

with open("questions.json", "r") as f:
    content = f.read()

data = json.loads(content)

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1,"-",alternative)
    user_answer = int(input("Your answer: "))
    question["user_answer"] = user_answer

score = 0
for index, question in enumerate(data):
    if question["user_answer"] == question["correct_answer"]:
        score += 1
        result = "Correct :)"
    else:
        result = "Wrong :("
    messege = (f"{index + 1}-{result} Question: {question['question_text']} Your answer: "
               f"{question['user_answer']} Correct answer: "
               f"{question['correct_answer']}")
    print(messege)

print(f"Your score is {score}")

