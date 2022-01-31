def full_name(first_name, last_name):
    """
    Returns a capitalized full name
    """
    full_name = first_name + " " + last_name
    return full_name.title()

def full_name_raw(first_name, last_name):
    """
    Returns full name with no capitalization
    """
    return first_name + " " + last_name

def full_name_reversed(first_name, last_name):
    """
    Returns a capitalized full name in the form "last, first"
    """
    full_name = last_name + " " + first_name
    return full_name.title()

class Question():
    """Represents a question for the questionnaire"""
    def __init__(self, question_text):
        """Initialization"""
        self.question_text = question_text
        self.answers = []
        
    def show_question(self):
        """Show question"""
        print(self.question_text)
        
    def store_answer(self, answer_text):
        """Store answer"""
        self.answers.append(answer_text)
        
    def show_answers(self):
        """Show answers"""
        print("Answers:")
        for answer in self.answers:
            print('- ' + answer)
