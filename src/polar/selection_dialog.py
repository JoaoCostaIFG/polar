import tkinter as tk
import tkinter.ttk as ttk


class SelectionDialog(tk.Toplevel):
    def __init__(
        self,
        options: list,
        singleSelection: bool = True,
        atLeastOneSelect: bool = True,
        title: str = "Make a selection",
    ):
        super().__init__()
        self.title(title)
        self._isSingle: bool = singleSelection
        self._atLeastOne: bool = atLeastOneSelect
        self._selection: list = None

        self._listbox = tk.Listbox(
            self,
            selectmode=tk.BROWSE if self._isSingle else tk.MULTIPLE,
            height=10,
            width=120,
        )
        self._listbox.pack(side=tk.LEFT, pady=15)

        scrollbar = ttk.Scrollbar(self, command=self._listbox.yview)
        scrollbar.pack(side=tk.LEFT, fill=tk.BOTH)
        self._listbox.config(yscrollcommand=scrollbar.set)

        tk.Button(self, text="Confirm", command=self._select).pack(
            pady=10, side=tk.BOTTOM
        )

        for opt in options:
            self._listbox.insert(tk.END, opt)

    @property
    def selection(self) -> str:
        return self._selection

    def _select(self) -> None:
        selection = self._listbox.curselection()
        if selection:
            if self._isSingle:
                self._selection = self._listbox.get(selection[0])
            else:
                self._selection = list(map(lambda s: self._listbox.get(s), selection))
            self.destroy()
        elif not self._atLeastOne:
            if self._isSingle:
                self._selection = None
            else:
                self._selection = []
            self.destroy()

    def show(self) -> list:
        self.grab_set()
        self.deiconify()
        self.wm_protocol("WM_DELETE_WINDOW", self.destroy)
        self.wait_window(self)

        self.grab_release()
        return self._selection


def selectFromDict(
    itemDict: dict,
    singleSelection: bool = True,
    atLeastOneSelect: bool = True,
    title: str = "Make a selection",
) -> list:
    selectedItems = SelectionDialog(
        list(itemDict.keys()),
        title=title,
        singleSelection=singleSelection,
        atLeastOneSelect=atLeastOneSelect,
    ).show()
    if selectedItems is None:
        print("No items selected.")
        return []
    if singleSelection:
        return [itemDict[selectedItems]]
    return [itemDict[key] for key in selectedItems]
