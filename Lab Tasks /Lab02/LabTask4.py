'''Layyana Junaid 23k-0056 BSAI-4A'''
'''Security System'''
import random

class SecuritySystem:
    def __init__(self):
        self.components = {}  
        self.status_mapping = {0: "Safe", 1: "Low Risk", 2: "High Risk"}
        self.initialize_system()

    def initialize_system(self):
        component_labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        for label in component_labels:
            self.components[label] = random.choice([0, 1, 2])

    def print_system_state(self, message):
        print(f"\n{message}")
        for component, status in self.components.items():
            print(f"Component {component}: {self.status_mapping[status]}")

    def scan_system(self):
        self.vulnerable_components = {"Low Risk": [], "High Risk": []}

        for component, status in self.components.items():
            if status == 1:
                self.vulnerable_components["Low Risk"].append(component)
            elif status == 2:
                self.vulnerable_components["High Risk"].append(component)

    def patch_vulnerabilities(self):
        for component in self.vulnerable_components["Low Risk"]:
            self.components[component] = 0  

        if self.vulnerable_components["High Risk"]:
            print("\n High Risk Vulnerabilities detected! Premium service required.")
            print(f"Affected components: {self.vulnerable_components['High Risk']}")
        else:
            print("\n No High Risk Vulnerabilities detected.")

system = SecuritySystem()
system.print_system_state("Initial System State")
system.scan_system()
system.patch_vulnerabilities()
system.print_system_state("Final System State (After Patching)")
