class QuizBrain:

    def __init__(self,list):
        self.question_numnber = 0
        self.question_list = list 
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_numnber]
        self.question_numnber += 1
        user_ans = str(input(f'Q.{self.question_numnber}: {current_question.text} (True/False) ? :')).lower()
        self.check_answer(user_ans,current_question.answer)
        
    def still_questions_left(self):
        return self.question_numnber < len(self.question_list)
    
    def check_answer(self,user_answer,correct_ans):
        if user_answer == correct_ans.lower():
            print('You got it Right!')
            self.score += 1
        else:
            print('Wrong Answer')
        print(f'The correct answer was : {correct_ans}')
        print(f'Your current score is {self.score}/{self.question_numnber}')
        print('\n')

    def final_score(self):
        return self.score
