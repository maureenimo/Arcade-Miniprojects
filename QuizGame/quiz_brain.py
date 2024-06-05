class Quiz:
    
    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
            
    def next_question(self):
        if self.still_has_questions():
            current = self.question_list[self.question_number]
            self.question_number +=1
            user_answer = input(f"Q.{self.question_number}: {current.text} (True/False)? ")
            current_answer = current.answer
            self.check_answer(user_answer,current_answer)
            return user_answer
            
    def check_answer(self, user_answer, current_answer):
        if user_answer == current_answer:
            self.score +=1
            print(f'You got it right!\nThe correct answer was: {current_answer}.')
        else:
            print(f'That\'s wrong.\nThe correct answer was: {current_answer}.')
        print(f"Your final score is: {self.score}/{self.question_number}.")