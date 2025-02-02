'''Layyana Junaid 23k-0056 BSAI-4A'''
'''Hospital Robot'''

import random

class HospitalRobot:
    def __init__(self):
        self.current_location = "Storage"
        self.medicine_cart = {}  
        self.patients = {
            "Room 101": {"medicine": "Painkiller", "id": "P001"},
            "Room 102": {"medicine": "Antibiotic", "id": "P002"},
            "Room 103": {"medicine": "Insulin", "id": "P003"},
        }

    def move_to(self, location):
        print(f"Moving to {location}...")
        self.current_location = location

    def pick_up_medicine(self):
        print("Picking up medicines...")
        for room, details in self.patients.items():
            self.medicine_cart[room] = details["medicine"]
        print("Medicines loaded successfully.")

    def deliver_medicine(self, room):
        self.move_to(room)

        if room in self.patients:
            patient_id = self.patients[room]["id"]
            required_medicine = self.patients[room]["medicine"]
            
            print(f"Scanning patient ID in {room}... (ID: {patient_id})")
            if random.choice([True, False]): 
                print(f"ID Verified! Delivering {required_medicine} to {room}.\n")
            else:
                print(f"ID Mismatch! Alerting staff for {room}.\n")

    def start_delivery(self):
        self.move_to("Storage")
        self.pick_up_medicine()
        for room in self.patients:
            self.deliver_medicine(room)
        print("All deliveries are completed!")


robot = HospitalRobot()
robot.start_delivery()
