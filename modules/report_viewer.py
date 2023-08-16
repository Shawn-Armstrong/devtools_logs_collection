import tkinter as tk
from tkinter import ttk
from .record import Record


class ReportViewer:
    def __init__(self, records):
        self.records = records
        self.root = tk.Tk()
        self.root.title("Report Viewer")
        
        self.notebook = ttk.Notebook(self.root)
        
        # Tab1: Display "Wells Fargo" at the center
        self.tab1 = ttk.Frame(self.notebook)
        label = ttk.Label(self.tab1, text="Wells Fargo")
        label.pack(pady=100, padx=100)
        self.notebook.add(self.tab1, text="Tab 1")

        # Tab2: Display Endpoints and Logs
        self.tab2 = ttk.Frame(self.notebook)
        
        # Endpoint list
        self.endpoints = tk.Listbox(self.tab2, width=40)
        self.endpoints.pack(side=tk.LEFT, fill=tk.Y)
        for record in self.records:
            self.endpoints.insert(tk.END, record.endpoint)
        self.endpoints.bind('<<ListboxSelect>>', self.on_endpoint_select)
        
        # Testing logs display
        self.testing_logs_display = tk.Text(self.tab2, wrap=tk.WORD, width=40)
        self.testing_logs_display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.testing_logs_display.insert(tk.END, "Testing Logs will appear here")

        # Production logs display
        self.production_logs_display = tk.Text(self.tab2, wrap=tk.WORD, width=40)
        self.production_logs_display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.production_logs_display.insert(tk.END, "Production Logs will appear here")

        self.notebook.add(self.tab2, text="Logs")
        
        self.notebook.pack(fill=tk.BOTH, expand=True)

    def on_endpoint_select(self, event):
        index = self.endpoints.curselection()[0]
        selected_endpoint = self.endpoints.get(index)
        self.update_display(selected_endpoint)

    def update_display(self, selected_endpoint):
        record = next(r for r in self.records if r.endpoint == selected_endpoint)

        # Update Testing Logs
        self.testing_logs_display.delete(1.0, tk.END)
        if record.testing_logs:
            for log in record.testing_logs:
                self.testing_logs_display.insert(tk.END, log + '\n')

        # Update Production Logs
        self.production_logs_display.delete(1.0, tk.END)
        if record.production_logs:
            for log in record.production_logs:
                self.production_logs_display.insert(tk.END, log + '\n')

    def run(self):
        self.root.mainloop()


# Usage:
# viewer = ReportViewer(records)
# viewer.run()
