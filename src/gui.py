import customtkinter as ctk
from tkinter import filedialog, messagebox
from cp import verifyFiles, getFileList, copyImages
from manual import ManualPlacementWindow

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("cpExcel")
        self.geometry("800x800")
        self.resizable(False, False)

        self.file_list = []
        self.destination_file = ""
        self.folder_path = ""

        self.titleFrame = ctk.CTkFrame(self)
        self.titleFrame.pack(pady=20)
        self.titleLabel = ctk.CTkLabel(self.titleFrame, text="cpExcel", font=ctk.CTkFont(size=30, weight="bold"))
        self.titleLabel.pack()
        self.mode = ctk.StringVar(value="Fichiers")
        self.ModeMenu = ctk.CTkOptionMenu(self, values=["Fichiers", "Dossier"], command=self.selectMode, variable=self.mode)
        self.ModeMenu.pack(pady=10)

        self.placementMode = ctk.StringVar(value="Auto")
        self.PlacementModeMenu = ctk.CTkOptionMenu(self, values=["Auto", "Manuel"], command=self.selectPlacementMode, variable=self.placementMode)
        self.PlacementModeMenu.pack(pady=10)

        self.fileFrame = ctk.CTkScrollableFrame(self)
        self.fileFrame.pack(pady=20)

        self.buttonFrame = ctk.CTkFrame(self)
        self.buttonFrame.pack(pady=20)
        self.selectFilesButton = ctk.CTkButton(self.buttonFrame, text="Sélectionner les fichiers", command=self.selectFiles)
        self.selectFilesButton.pack(pady=20)
        self.startButton = ctk.CTkButton(self.buttonFrame, text="Lancer la copie", command=self.startCopy)
        self.startButton.pack()

    def selectPlacementMode(self, value):
        print(f"Mode de placement sélectionné : {value}")
        if value == "Auto":
            pass
        elif value == "Manuel":
            pass
        else:
            return 1

    def selectMode(self, value):
        print(f"Mode sélectionné : {value}")
        if value == "Fichiers":
            self.selectFilesButton.configure(text="Sélectionner les fichiers")
            pass
        elif value == "Dossier":
            self.selectFilesButton.configure(text="Sélectionner un dossier")
            pass
        else:
            return 1

    def selectFiles(self):
        for w in self.fileFrame.winfo_children():
            w.destroy()

        if self.mode.get() == "Fichiers":
            self.file_list = filedialog.askopenfilenames(title="Sélectionner les fichiers", filetypes=[("Image files", "*.png *.jpg *.jpeg")])
            if self.file_list:
                print(f"Fichiers sélectionnés : {self.file_list}")
                self.fileLabel = ctk.CTkLabel(self.fileFrame, text="\n".join(self.file_list))
                self.fileLabel.pack()
            else:
                print("Aucun fichier sélectionné.")
        elif self.mode.get() == "Dossier":
            self.folder_path = filedialog.askdirectory(title="Sélectionner un dossier")
            if self.folder_path:
                print(f"Dossier sélectionné : {self.folder_path}")
                self.fileLabel = ctk.CTkLabel(self.fileFrame, text=self.folder_path)
                self.fileLabel.pack()
            else:
                print("Aucun dossier sélectionné.")
        else:
            print("Mode de sélection invalide.")
            return 1

    def startCopy(self):
        self.destination_file = filedialog.askopenfilename(title="Sélectionner l'excel de destination", filetypes=[("Excel files", "*.xlsx *.xls *.xlsm *.xlsb")])
        if self.mode.get() == "Fichiers":
            verifyFiles(self.file_list)
        elif self.mode.get() == "Dossier":
            self.file_list = getFileList(self.folder_path)
            verifyFiles(self.file_list)

        if self.placementMode.get() == "Auto":
            copyImages(self.file_list, self.destination_file, mode="Auto")
        elif self.placementMode.get() == "Manuel":
            copyImages(self.file_list, self.destination_file, mode="Manuel",parent = self)

        return 0


cp = App()
cp.mainloop()