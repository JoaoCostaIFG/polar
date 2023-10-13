import tkinter as tk
import tkinter.ttk as ttk

from polar.inputfield import InputField


class TextField(InputField):
    def __init__(
        self, name: str, defaultValue: str = None, hidden: bool = False
    ) -> None:
        super().__init__(name, defaultValue)
        self._field = ttk.Entry(master=self._frame, width=50)
        if hidden:
            self._field.config(show="*")
        self._field.grid(row=0, column=1)

        if defaultValue is not None:
            self.value = defaultValue

    @property
    def value(self) -> str:
        return self._field.get()

    @value.setter
    def value(self, value: str) -> None:
        self._field.delete(0, tk.END)
        self._field.insert(0, value)

    def __str__(self) -> str:
        return self.value
