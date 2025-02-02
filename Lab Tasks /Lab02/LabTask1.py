'''Layyana Junaid 23k-0056 BSAI-4A'''
'''Making a securtiy agent'''
 
import random

class SystemEnvironment:
    def __init__(self):
        self.components = []
        self.vulnerabilities = []
        for components in range(0, 9):
            self.components.append(random.choice([0, 1])) #component can either be safe(0) or vulnerable(1)
    
    def print_state(self):
        self.vulnerabilities = []  #reset vulnerabilities list each time
        for index, component in enumerate(self.components):
            if component == 1:  # 1 means vulnerable
                self.vulnerabilities.append(f"component {index}")

        if self.vulnerabilities:
            print(f"These components are vulnerable:")
            print(f"{self.vulnerabilities}\n")
        else:
            print("No Vulnerability! Every Component is functional!")


'''s1 = SystemEnvironment()
s1.print_state()'''

class SecurityAgent:
    def __init__(self, system):
        self.system = system
        self.loggs = []

    def patching(self):
        self.system.components = [0 for component in self.system.components]
        print(f"These components are vulnerable and have been patched!:")
        print(f"{self.system.vulnerabilities}\n")

    def search(self) :
        for component in self.system.components :
            if component == 1:
                self.loggs.append("Warning. Component is vulnerable")
            else :
                self.loggs.append("Success!")
        self.patching()

sys = SystemEnvironment()
agent = SecurityAgent(sys)

sys.print_state()
agent.search()
sys.print_state()

        
    
