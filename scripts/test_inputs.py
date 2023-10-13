from polar import action, TextField, TextBox

box = TextBox("First name")
field = TextField("Last name")


@action
def act():
    global box, field
    print(f"{box.name}: {box.value}")
    print(f"{field.name}: {field.value}")
