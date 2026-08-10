from abc import ABC, abstractmethod

class ResumeBuilder(ABC):
    @abstractmethod
    def add_experience(self):
        pass

    @abstractmethod
    def add_education(self):
        pass

    @abstractmethod
    def add_personal_info(self):
        pass

    @abstractmethod
    def add_skills(self):
        pass

    @abstractmethod
    def add_hobbies(self):
        pass


class Resume:
    def __init__(self):
        self.experience = {}
        self.education = {}
        self.personal_info = {}
        self.skills = []
        self.hobbies = []
        
    def show_resume(self):
        print("Resume:")
        print("Experience:", self.experience)
        print("Education:", self.education)
        print("Personal Info:", self.personal_info)
        print("Skills:", self.skills)
        print("Hobbies:", self.hobbies)
        

class StandardResumeBuilder(ResumeBuilder):
    def __init__(self):
        self.resume = Resume()
        
    def add_experience(self, experience):
        self.resume.experience = experience
        
    def add_education(self, education):
        self.resume.education = education
        
    def add_personal_info(self, personal_info):
        self.resume.personal_info = personal_info
        
    def add_skills(self, skills):
        self.resume.skills = skills
        
    def add_hobbies(self, hobbies):
        self.resume.hobbies = hobbies
        
    def get_resume(self):
        return self.resume
    
def main():
    builder = StandardResumeBuilder()
    
    experience = {"Company": "ABC Corp", "Role": "Software Engineer", "Duration": "2 years"}
    education = {"Degree": "B.Tech", "University": "XYZ University", "Year": "2020"}
    personal_info = {"Name": "John Doe", "Email": "john.doe@example.com"}
    skills = ["Python", "Java", "C++"]
    hobbies = ["Reading", "Gaming", "Traveling"]

    builder.add_experience(experience)
    builder.add_education(education)
    builder.add_personal_info(personal_info)
    builder.add_skills(skills)
    builder.add_hobbies(hobbies)

    resume = builder.get_resume()
    resume.show_resume()
    
    
main()