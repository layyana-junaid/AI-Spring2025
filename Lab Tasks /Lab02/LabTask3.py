'''Layyana Junaid 23k-0056 BSAI-4A'''
'''Backup Management System'''

import random

class BackupManagementSystem:
    def __init__(self):
        self.backups = []
        self.failed_backups = []

        for backups in range(0,10):
            self.backups.append(random.choice([0, 1])) # 0 = Backup, 1 = Failed Backups
        
    def check_backups(self):
        self.failed_backups = []
        for index, backup in enumerate(self.backups):
            if backup == 1:
                print("Backup Failed!")
                self.failed_backups.append(index)

        if self.failed_backups:
            print(f"{self.failed_backups}\n These are failed backups")
        else:
            print("No Failed Backups!")

    def reuploading_failed_backups(self):
        if not self.failed_backups:
            print("No failed backups to correct.")
            return
        
        for index in self.failed_backups:
            self.backups[index] = 0  

        print("The Failed Backups were corrected!")
        print(f"Updated Backups: {self.backups}\n")

backup_system = BackupManagementSystem()

backup_system.check_backups()
backup_system.reuploading_failed_backups()
backup_system.check_backups()


