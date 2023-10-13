# Tools

This repo contains some a launcher that can turn scripts into GUIs, making
them easier to use by non-technical people.

## Features

- Easily generate GUIs from command line scripts.
- Allows using the scripts from the command line as well.
- Automatically generates command line arguments for the various inputs.
- Automatically parses environment variables for the various inputs, including variables sourced from .env files automatically.

## Setup/Install

1. Clone this repo -- `git clone ssh://git@bitbucket.critical.pt:7999/wrhvp/tools.git`
2. Install python3 and pip -- [python.org](https://www.python.org/downloads/)
3. Open a terminal on the projects directory -- `cd polar`
4. Install the lib and its dependencies -- `pip install -e .`
5. Open the launcher -- `python -m polar`

## Example

This is a simple example of a script that can be turned into a GUI.

```python
from polar import action, TextField, TextBox

box = TextBox("First name")
field = TextField("Last name")


@action
def act():
    global box, field
    print(f"{box.name}: {box.value}")
    print(f"{field.name}: {field.value}")
```

## TODO

- ~~Trap for ctrl+c~~
  - Make it stop current task (if any) or exit otherwise
- Threading so GUI doesn't freeze while processing
- Ctrl+c na GUI para interromper task?
  - Maybe not ctrl-c
  - Only ctrl-c when processing (is fine)
- Botao switch current script
- Option para começarem todos selected:
  - Maybe botao de selectAll instead: self.\_listbox.select_set(0, tk.END)
- ~~Environment file~~
  - ~~works the same as cmdline args~~
- ~~Definir algo no contexto do loader para scripts puderem correr sem a GUI~~
  - ~~auto cmdline options~~
