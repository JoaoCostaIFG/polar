import tkinter as tk
import tkinter.ttk as ttk

from polar.inputfield import InputField


class ComboBox(InputField):
    def __init__(self, name: str, values: list, defaultValue: str = "") -> None:
        super().__init__(name, defaultValue)
        self._field = ttk.Combobox(master=self._frame, values=values, state="readonly")
        self._field.grid(row=0, column=1)

        if defaultValue is not None:
            self.value = defaultValue

    @property
    def value(self) -> str:
        return self._field.get()

    @value.setter
    def value(self, value: str) -> None:
        self._field.set(value)

    def __str__(self) -> str:
        return self.value
