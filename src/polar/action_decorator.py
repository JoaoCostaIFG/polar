from collections.abc import Callable
from sys import stderr
from timeit import default_timer as timer
from os import getenv
import traceback
import functools
import argparse

from tkinter.messagebox import showinfo, showerror
from polar.inputfield import InputField
import polar.gui_settings

from dotenv import dotenv_values


def _genAndParseArgs(func):
    env = dotenv_values()
    inputs: dict[str, InputField] = dict(
        filter(lambda g: isinstance(g[1], InputField), func.__globals__.items())
    )

    parser = argparse.ArgumentParser()
    for name, field in inputs.items():
        if name in env:
            # set env variables first because cmdline args have priority
            field.value = env[name]
        parser.add_argument(f"--{name}", help=field.name)

    args = parser.parse_args()
    for name, arg in args.__dict__.items():
        if arg is None:
            continue
        inputs[name].value = arg


def action(func):
    @functools.wraps(func)
    def actionFunc(*args, **kwargs):
        start = timer()
        try:
            func(*args, **kwargs)
            actionTimeTaken = timer() - start
            sucText = f"Finished running the task in {actionTimeTaken} seconds"
            print(sucText, file=stderr)
            if polar.gui_settings._hasGUI:
                showinfo("Task done", sucText)
        except Exception as e:
            excText = f"There was an error with the following exception:\n{traceback.format_exc()}"
            print(excText, file=stderr)
            if polar.gui_settings._hasGUI:
                showerror("There was an error", excText)

    # parse env vars and cmdline args
    _genAndParseArgs(func)

    actionFunc._isAction = True
    if not polar.gui_settings._hasGUI:
        actionFunc()

    return actionFunc


def _isAction(o) -> bool:
    return isinstance(o, Callable) and hasattr(o, "_isAction") and o._isAction == True
