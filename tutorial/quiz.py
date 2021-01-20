class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
    def check(self, answer):
        return self.answer == answer

questions = [
    Question("What color are apples?\n(a) Red\n(b) Black\n(c) Purple\n", "a"),
    Question("What color are bananas?\n(a) Red\n(b) Yellow\n(c) Purple\n", "b"),
    Question("What color are strawberries?\n(a) Red\n(b) Green\n(c) Purple\n", "a")
]

def run_test(questions):
    score = 0
    for q in questions:
        answer = input(q.prompt)
        if q.check(answer):
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " right")

run_test(questions)