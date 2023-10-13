from importlib import import_module
from os import listdir
from signal import signal, SIGINT, SIGILL, SIGTERM
from sys import stderr
import tkinter as tk
import tkinter.ttk as ttk

import polar.gui_settings
from polar.action_decorator import _isAction
from polar.inputfield import InputField
from polar.selection_dialog import SelectionDialog


class App(tk.Tk):
    def __init__(self, *args, **kwargs) -> None:
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Test GUI form")

        polar.gui_settings._hasGUI = True

        self._inputsFrame = ttk.Frame(relief=tk.GROOVE, borderwidth=3)
        self._inputsFrame.pack(padx=5, pady=5)

    def _importScript(self):
        scripts = list(filter(lambda o: o.endswith(".py"), listdir("scripts")))
        if len(scripts) == 0:
            print(f"No scripts found on the scripts directory.", file=stderr)
            exit(1)
        sel = SelectionDialog(scripts, title="Select a script").show()
        if sel is None:
            print(f"No selection made.", file=stderr)
            exit(1)
        script = import_module(f"scripts.{sel[0:-3]}")

        fields = filter(lambda g: isinstance(g, InputField), vars(script).values())
        actions = list(filter(_isAction, vars(script).values()))
        if len(actions) != 1:
            print(
                f"There can only be one action function per script. There are {len(actions)}: {actions}.",
                file=stderr,
            )
            exit(1)
        action = actions[0]

        for field in fields:
            field._acquire(self._inputsFrame)
        btn = ttk.Button(text="Submit", command=action)
        btn.pack()


def main():
    app = App()

    def handleSigint(sig, frame):
        print("Caught SIGINT. Exiting...", file=stderr)
        app.destroy()
        exit(1)

    def check():
        app.after(500, check)

    app.after(50, check)
    signal(SIGINT, handleSigint)

    app._importScript()
    app.mainloop()
