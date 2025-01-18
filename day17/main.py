from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:    
    question_text = question['text']
    question_ans = question['answer']
    new_question = Question(question_text,question_ans)
    question_bank.append(new_question) 

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_questions_left():
    quiz_brain.next_question()

print('You have completed the quiz')
print(f'You final score is : {quiz_brain.final_score()}')
