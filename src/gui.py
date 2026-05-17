import customtkinter as ctk
from tkinter import filedialog, messagebox
from cp import verifyFile, getFileList

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    file_list = list
    destination_file = str
    folder_path = str

    def __init__(self):
        super().__init__()
        self.title("cpExcel")
        self.geometry("800x800")
        self.resizable(False, False)

        self.titleFrame = ctk.CTkFrame(self)
        self.titleFrame.pack(pady=20)
        self.titleLabel = ctk.CTkLabel(self.titleFrame, text="cpExcel", font=ctk.CTkFont(size=30, weight="bold"))
        self.titleLabel.pack()
        self.mode = ctk.StringVar(value="Fichiers")
        self.selectMode = ctk.CTkOptionMenu(self, values=["Fichiers", "Dossier"], command=self.selectMode, variable=self.mode)
        self.selectMode.pack(pady=10)

        self.placementMode = ctk.StringVar(value="Auto")
        self.selectPlacementMode = ctk.CTkOptionMenu(self, values=["Auto", "Manuel"], command=self.selectPlacementMode, variable=self.placementMode)
        self.selectPlacementMode.pack(pady=10)

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
            pass
        elif value == "Dossier":
            pass
        else:
            return 1

    def selectFiles(self):
        if self.mode.get() == "Fichiers":
            file_paths = filedialog.askopenfilenames(title="Sélectionner les fichiers", filetypes=[("Image files", "*.png *.jpg *.jpeg")])
            if file_paths:
                print(f"Fichiers sélectionnés : {file_paths}")
                self.fileLabel = ctk.CTkLabel(self.fileFrame, text="\n".join(file_paths))
                self.fileLabel.pack()
            else:
                print("Aucun fichier sélectionné.")
        elif self.mode.get() == "Dossier":
            folder_path = filedialog.askdirectory(title="Sélectionner un dossier")
            if folder_path:
                print(f"Dossier sélectionné : {folder_path}")
            else:
                print("Aucun dossier sélectionné.")
        else:
            print("Mode de sélection invalide.")
            return 1

    def startCopy(self):
        if self.mode.get() == "Fichiers":
            verifyFile(self.file_list)
        elif self.mode.get() == "Dossier":
            self.file_list = getFileList(self.folder_path)
            verifyFile(self.file_list)

cp = App()
cp.mainloop()