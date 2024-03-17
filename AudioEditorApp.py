import os
import tkinter as tk
from tkinter import filedialog, messagebox
from AudioEditor import AudioEditor


class AudioEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Editor")

        # Configure the grid rows and columns
        self.root.grid_rowconfigure(0, weight=1)  # Makes the listbox row resizable
        self.root.grid_columnconfigure(0, weight=1)  # Makes the listbox column resizable

        # Listbox to display loaded files
        self.file_listbox = tk.Listbox(root, width=50)
        self.file_listbox.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        # Save Button
        self.save_button = tk.Button(root, text="Save Audio", command=self.save_audio)
        self.save_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Scrollbar for listbox
        self.scrollbar = tk.Scrollbar(root, orient='vertical', command=self.file_listbox.yview)
        self.scrollbar.grid(row=0, column=1, sticky='ns', padx=10, pady=10)

        # Configure the listbox's scrollbar
        self.file_listbox.config(yscrollcommand=self.scrollbar.set)

        # Button to load audio
        self.load_button = tk.Button(root, text="Load Audio", command=self.load_audio)
        self.load_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Store loaded audio data
        self.loaded_audios = {}

    def load_audio(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.aac *.flac *.wav *.aiff")])
        if file_path:
            try:
                audio_data = AudioEditor.load_audio(file_path)
                self.loaded_audios[os.path.basename(file_path)] = audio_data
                self.file_listbox.insert(tk.END, os.path.basename(file_path))
            except ValueError as e:
                tk.messagebox.showerror("Error", str(e))

    def save_audio(self):
        if self.loaded_audios:
            # Choose the first loaded audio file to save
            audio_data = list(self.loaded_audios.values())[0]

            # Ask the user for the output file path
            output_path = filedialog.asksaveasfilename(defaultextension=".mp3",
                                                       filetypes=[("MP3 files", "*.mp3"),
                                                                  ("WAV files", "*.wav"),
                                                                  ("All files", "*.*")])
            if output_path:
                try:
                    AudioEditor.save_audio(audio_data, output_path)
                    tk.messagebox.showinfo("Success", f"Audio saved successfully as {output_path}")
                except Exception as e:
                    tk.messagebox.showerror("Error", str(e))
        else:
            tk.messagebox.showinfo("Info", "No audio loaded to save")


root = tk.Tk()
app = AudioEditorApp(root)
root.mainloop()
