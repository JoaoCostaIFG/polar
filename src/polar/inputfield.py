import tkinter as tk
import tkinter.ttk as ttk


class InputField:
    def __init__(self, name: str, defaultValue: str = None) -> None:
        self._defaultValue = defaultValue
        self._frame = ttk.Frame(padding=5)
        self._label = ttk.Label(master=self._frame, text=name)
        self._label.grid(row=0, column=0, sticky="e")

    @property
    def defaultValue(self) -> str:
        return self._defaultValue

    @property
    def name(self) -> str:
        return self._label["text"]

    @name.setter
    def name(self, name: str) -> None:
        self._label["text"] = name

    def _acquire(self, master) -> None:
        self._frame.master = master
        self._frame.pack(fill=tk.X)
