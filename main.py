import tkinter
import customtkinter as ctk

from cryption import decrypt_files, encrypt_files, generate_fernet

def verschluesseln():
    if password1input.get() != password2input.get() or password1input.get() == "":
        password1input.delete(0, tkinter.END)
        password2input.delete(0, tkinter.END)
        errorWindow()
        # reset password fields


    elif password1input.get() == password2input.get():
        createTopLevelConfirmation()


def errorWindow():
    tl = ctk.CTk()
    tl.geometry("300x130")
    tl.title("File De- and Encrypter")

    label = ctk.CTkLabel(tl, text="Passwörter stimmen nicht\nüberein oder sind leer!",
                         font=("Arial", 15))
    label.place(rely=0.2)
    label.pack()
    exit_button = ctk.CTkButton(tl, text="Zurück", command=tl.destroy)
    exit_button.place(rely=0.7, relx=0.5, anchor=tkinter.CENTER)
    tl.mainloop()


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("500x300")
app.title("File De- and Encrypter")

label = ctk.CTkLabel(master=app, text="Ver- oder entschlüsselt alle Dateien\n in diesem Ordner und in allen Unterordnern",\
    font= ("Open Sans", 20),
    corner_radius=8,)

label.place(x=0, y=0, relwidth=1, relheight=0.2)

verschluesselnButton = ctk.CTkButton(master=app,
                                 width=100,
                                 height=30,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Verschlüsseln",
                                 command=verschluesseln)
verschluesselnButton.place(relx=0.395, rely=0.8, anchor=tkinter.CENTER)
entschluesselnButton = ctk.CTkButton(master=app,
                                 width=100,
                                 height=30,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Entschlüsseln")
entschluesselnButton.place(relx=0.605, rely=0.8, anchor=tkinter.CENTER)

input1label = ctk.CTkLabel(master=app, text="Passwort:",\
    font= ("Open Sans", 15),
    corner_radius=8,)

password1input = ctk.CTkEntry(master=app, width=200, font=("Open Sans", 15), corner_radius=8)
input1label.place(relx=0.3, rely=0.42, anchor=tkinter.CENTER)
password1input.place(relx=0.58, rely=0.42, anchor=tkinter.CENTER)

input2label = ctk.CTkLabel(master=app, text="Passwort wiederholen:",\
    font= ("Open Sans", 15),
    corner_radius=8,)
password2input = ctk.CTkEntry(master=app, width=200, font=("Open Sans", 15), corner_radius=8)

input2label.place(relx=0.219, rely=0.53, anchor=tkinter.CENTER)
password2input.place(relx=0.58, rely=0.53, anchor=tkinter.CENTER)


def createTopLevelConfirmation():
    tl = ctk.CTk()
    tl.geometry("300x230")
    tl.title("File De- and Encrypter")
    label0 = ctk.CTkLabel(tl, text="Verschlüsseln", font=("Arial", 20),
                          fg_color="#170101")
    label0.place(rely=0.05, relx = 0.5, anchor=tkinter.CENTER)
    label = ctk.CTkLabel(tl, text="Sind Sie sicher, dass Sie fortfahren wollen?",
                            font=("Arial", 15))
    label.place(rely=0.2)

    yes_button = ctk.CTkButton(tl, text="Verschlüsseln", command=encrypt_files(generate_fernet(password1input.get())))
    yes_button.place(rely=0.5, relx=0.5, anchor=tkinter.CENTER,
                     width=150, height=45,)

    no_button = ctk.CTkButton(tl, text="Abbrechen", command=tl.destroy,
                                    fg_color= "red")
    no_button.place(rely=0.7, relx=0.5, anchor=tkinter.CENTER,
                    width=100, height=30)
    tl.mainloop()


app.mainloop()



