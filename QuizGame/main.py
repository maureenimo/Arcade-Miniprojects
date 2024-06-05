from data import question_data
from question_model import Question
from quiz_brain import Quiz

question_bank= []

for question in question_data:
    text = question['question']
    answer = question['correct_answer']
    # level = question['difficulty']
    
    question = Question(text, answer)
    
    question_bank.append(question)
quiz = Quiz(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    
