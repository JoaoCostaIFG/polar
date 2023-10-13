import tkinter as tk

from polar.inputfield import InputField


class TextBox(InputField):
    def __init__(self, name: str, defaultValue: str = None) -> None:
        super().__init__(name, defaultValue)
        self._field = tk.Text(master=self._frame)
        self._field.grid(row=0, column=1)

        if defaultValue is not None:
            self.value = defaultValue

    @property
    def value(self) -> str:
        return self._field.get("1.0", tk.END).strip("\n")

    @value.setter
    def value(self, value: str) -> None:
        self._field.delete("1.0", tk.END)
        self._field.insert("1.0", value)

    @property
    def lines(self) -> list:
        return self.value.split("\n")

    @lines.setter
    def lines(self, lines: list) -> None:
        self.value = "\n".join(lines)

    def __str__(self) -> str:
        return self.value