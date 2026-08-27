""" VISITOR PATTERN
Consider a Hospital Management System where different types of
patients are admitted:
• General Patients
• Children Patients
• Senior Citizens

Hospital management needs to perform different operations on patients, such
as:
• Doctor consultation
• Health checkup
• Insurance claim processing
• Medicine prescription
• Billing calculation
Instead of adding all these operations inside patient classes, the application
should use a specific design pattern to separate operations from objects
"""

from abc import ABC, abstractmethod


class Patient(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass
    

class GeneralPatient(Patient):
    def accept(self, visitor):
        visitor.visit_general_patient(self)
        

class ChildrenPatient(Patient):
    def accept(self, visitor):
        visitor.visit_children_patient(self)
        
        
class SeniorCitizen(Patient):
    def accept(self, visitor):
        visitor.visit_senior_citizen(self)
        
        
class PatientVisitor(ABC):
    @abstractmethod
    def visit_general_patient(self, patient):
        pass

    @abstractmethod
    def visit_children_patient(self, patient):
        pass

    @abstractmethod
    def visit_senior_citizen(self, patient):
        pass
    
    
class DoctorConsultation(PatientVisitor):
    def visit_general_patient(self, patient):
        print("Doctor consultation for General Patient.")

    def visit_children_patient(self, patient):
        print("Doctor consultation for Children Patient.")

    def visit_senior_citizen(self, patient):
        print("Doctor consultation for Senior Citizen.")
        
        
class HealthCheckup(PatientVisitor):
    def visit_general_patient(self, patient):
        print("Health checkup for General Patient.")

    def visit_children_patient(self, patient):
        print("Health checkup for Children Patient.")

    def visit_senior_citizen(self, patient):
        print("Health checkup for Senior Citizen.")
        
        
class InsuranceClaimProcessing(PatientVisitor):
    def visit_general_patient(self, patient):
        print("Insurance claim processing for General Patient.")

    def visit_children_patient(self, patient):
        print("Insurance claim processing for Children Patient.")

    def visit_senior_citizen(self, patient):
        print("Insurance claim processing for Senior Citizen.")
        
        
class MedicinePrescription(PatientVisitor):
    def visit_general_patient(self, patient):
        print("Medicine prescription for General Patient.")

    def visit_children_patient(self, patient):
        print("Medicine prescription for Children Patient.")

    def visit_senior_citizen(self, patient):
        print("Medicine prescription for Senior Citizen.")
        
        
class BillingCalculation(PatientVisitor):
    def visit_general_patient(self, patient):
        print("Billing calculation for General Patient.")

    def visit_children_patient(self, patient):
        print("Billing calculation for Children Patient.")

    def visit_senior_citizen(self, patient):
        print("Billing calculation for Senior Citizen.")
        
        
class HospitalManagementSystem:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def perform_operations(self, visitor):
        for patient in self.patients:
            patient.accept(visitor)
            

def main():
    hospital = HospitalManagementSystem()
    visitors = {
        "1": DoctorConsultation(),
        "2": HealthCheckup(),
        "3": InsuranceClaimProcessing(),
        "4": MedicinePrescription(),
        "5": BillingCalculation(),
    }

    while True:
        print("\nHospital Management System")
        print("1. Add general patient")
        print("2. Add children patient")
        print("3. Add senior citizen")
        print("4. Perform doctor consultation")
        print("5. Perform health checkup")
        print("6. Process insurance claims")
        print("7. Prescribe medicine")
        print("8. Calculate billing")
        print("9. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            hospital.add_patient(GeneralPatient())
            print("General patient added.")
        elif choice == "2":
            hospital.add_patient(ChildrenPatient())
            print("Children patient added.")
        elif choice == "3":
            hospital.add_patient(SeniorCitizen())
            print("Senior citizen added.")
        elif choice in {"4", "5", "6", "7", "8"}:
            if not hospital.patients:
                print("No patients have been added yet.")
            else:
                hospital.perform_operations(visitors[str(int(choice) - 3)])
        elif choice == "9":
            print("Exiting Hospital Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
    