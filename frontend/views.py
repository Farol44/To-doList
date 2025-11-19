import customtkinter as ctk
from frontend.styles import *
from backend.controllers import *
class TodoList(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List")
        self.geometry("400x600")
        self.configure(bg=BACKGROUND_COLOR)
        self.task_frame = ctk.CTkFrame(self)
        self.task_frame.pack(fill="both", expand=True, padx=10, pady=10)
        self.entry_title = ctk.CTkEntry(self, placeholder_text="Titre de la tâche")
        self.entry_title.pack(pady=5)
        self.add_button = ctk.CTkButton(self, text="Ajouter Tâche", command=self.add_task_gui)
        self.add_button.pack(pady=5)
        self.refresh_tasks()
    def add_task_gui(self):
        title = self.entry_title.get()
        desc = self.entry_desc.get()
        if title:
            add_task(title, desc)
            self.entry_title.delete(0, 'end')
            self.entry_desc.delete(0, 'end')
            self.refresh_tasks()
    def delete_task_gui(self, task_id):
        delete_task(task_id)
        self.refresh_tasks()
    def refresh_tasks(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()
        tasks = get_tasks()
        for task in tasks:
            text = f"{task.title}- {"<>" if task.description else "x"}"
            btn = ctk.CTkButton(self.task_frame, text=text, command=lambda id=task.id: self.delete_task_gui(id))
            btn.pack(fill="x", pady=2)
            del_btn = ctk.CTkButton(self.task_frame, text="Supprimer", command=lambda id=task.id: self.delete_task_gui(id))
            del_btn.pack(fill="x", pady=2)
    def toggle_task_gui(self, task_id):
        toggle_task(task_id)
        self.refresh_tasks()