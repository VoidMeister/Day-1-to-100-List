#Create a class called QuizBrain
#Write an init() method
# Initialise the question_number to 0
# Initialise the question_list to an input

class QuizBrain:
    """
    This class is main code for the project. You print out the questions and see if they had the right answer.
     If they do, go to the next question
    """
    def __init__(self, q_list):
        """
        
        :param q_list: # this attribute stores the question bank which has objects of class Question
        # that have "text" attribute and "answer" attribute
        """
        self.question_number = 0  # this attribute keeps track of how many questions we have gone over
        self.question_list = q_list
        self.score = 0 # keeps track of the user score
        self.balls = 1

    def next_question(self):
        """
        This method gets the current question on the question_list and then increments the question_number. We
        also ask the user for input
        :return: Doesn't return anything
        """
    #Retrieve the item at the current question_number from the question_list
    #Use the input function to show the user the question text and ask for the users answer
        current_question = self.question_list[self.question_number]
        #This returns the question at current question number--> {"text": "A slug's blood is green.", "answer": "True"}
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        """
        Checks if there are still questions that have not been gone through in the question_list.
        :return: Returns True if we haven't gone through all the dictionaries in the question bank i.e the questions
        """
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        """
        this function checks to see if the user answer is the same as the question answer attribute
        :param user_answer: this is the input from next_question
        :param correct_answer: this is the answer attribute from the current question
        :return: Nothing
        """
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The right answer is: {correct_answer}")
        print(f"Your current score is : {self.score}/{self.question_number}.")
        print("\n")


class NewQuizBrain(QuizBrain):
    def __init__(self, q_list):
        super().__init__(q_list)

