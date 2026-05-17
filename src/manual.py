import customtkinter as ctk

class ManualPlacementWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Placement Manuel")
        self.geometry("400x400")
        self.resizable(True, True)

        self.tableFrame = ctk.CTkScrollableFrame(self)
        self.tableFrame.pack(pady=20, padx=20, fill="both", expand=True)

        self.buttonFrame = ctk.CTkFrame(self)
        self.buttonFrame.pack(pady=20)
        self.saveButton = ctk.CTkButton(self.buttonFrame, text="Enregistrer", command=self.savePlacement)
        self.saveButton.pack(pady=20)   
        
    def showPlacelements(self, fileList,sheetlist=None):

        for i, file in enumerate(fileList):

            sheet = ctk.CTkOptionMenu(self.tableFrame, values=sheetlist)
            sheet.grid(row=i+1, column=3, padx=10, pady=5)

            fileLabel = ctk.CTkLabel(self.tableFrame, text="Fichier")
            fileLabel.grid(row=0, column=0, padx=10, pady=5)

            colLabel = ctk.CTkLabel(self.tableFrame, text="Colonne")
            colLabel.grid(row=0, column=1, padx=10, pady=5)

            rowLabel = ctk.CTkLabel(self.tableFrame, text="Ligne")
            rowLabel.grid(row=0, column=2, padx=10, pady=5)

            label = ctk.CTkLabel(self.tableFrame, text=file)
            label.grid(row=i+1, column=0, padx=10, pady=5)

            rowEntry = ctk.CTkEntry(self.tableFrame)
            rowEntry.grid(row=i+1, column=1, padx=10, pady=5)

            colEntry = ctk.CTkEntry(self.tableFrame)
            colEntry.grid(row=i+1, column=2, padx=10, pady=5)
            
            self._widgets.append({
                "file": file,
                "col": colEntry,
                "row": rowEntry,
                "sheet": sheet,
            })

    def savePlacement(self):
        self.result = [{"file": w["file"],"col": w["col"].get(),"row": w["row"].get(),"sheet": w["sheet"].get(),} for w in self._widgets]
        self.destroy()
        print("Placement enregistré")
        self.destroy()