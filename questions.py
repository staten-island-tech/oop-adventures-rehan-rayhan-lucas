class Suspect:
    def __init__(self, name, role, responses):
        self.name = name
        self.role = role
        self.responses = responses  

    def ask_question(self, question_number):
        return self.responses.get(question_number, "I don't know.")



questions = [
    "Where were you when the crime happened?",
    "Do you have any idea who could be behind this?",
    "What were you doing before the crime?",
    "Can you remember anything strange from that night?"
]


suspect_a_responses = {
    1: "I was in my room all night. I didn’t hear anything unusual.",
    2: "Honestly, no. I don’t even know why anyone would want to do something like this.",
    3: "I was reading a book, nothing exciting. Just trying to pass the time.",
    4: "Nothing comes to mind. Everything seemed normal."
}

suspect_b_responses = {
    1: "I was in the kitchen, preparing food. I didn’t see anything.",
    2: "I’m not sure, but I did hear some strange noises coming from upstairs.",
    3: "I was just making some food, getting ready for the night. It was pretty quiet in the house.",
    4: "I thought I heard something from upstairs… it sounded like footsteps. But I was focused on the kitchen, so I didn’t investigate."
}

suspect_c_responses = {
    1: "I was outside the house. I needed some fresh air.",
    2: "It could have been Suspect B. I saw him acting nervous earlier.",
    3: "I was walking around the yard, getting some space. I didn’t hear anything from inside.",
    4: "It’s strange, but I noticed Suspect B seemed to be in a hurry. He was acting a bit off."
}


suspect_a = Suspect("Suspect A", "Innocent", suspect_a_responses)
suspect_b = Suspect("Suspect B", "Innocent", suspect_b_responses)
suspect_c = Suspect("Suspect C", "Guilty", suspect_c_responses)


def ask_suspect_question(suspect, question_number):
    print(f"Question: {questions[question_number - 1]}")
    print(f"{suspect.name}: {suspect.ask_question(question_number)}\n")


for suspect in [suspect_a, suspect_b, suspect_c]:
    for question_number in range(1, len(questions) + 1):
        ask_suspect_question(suspect, question_number)
