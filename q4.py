import tkinter as tk
from collections import deque
from abc import ABC, abstractmethod

class History:
    def __init__(self):
        self.__list = deque()

    def __str__(self):
        return '\n'.join(f'{i+1}: {item}' for (i,item) in enumerate(self.__list))

    def add(self,item):
        self.__list.appendleft(item)

# Invoker
class ClientBackend:
    def __init__(self):
        self.__history = History()

    @property
    def history(self):
        return str(self.__history)

    def execute(self, command):
        self.__history.add(command)
        return command.execute()

def foo():
    from random import randint
    print(randint(1,100))

# Command Interface
class Command(ABC):
    def __init__(self,obj):
        self._obj = obj

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return self.__str__()

    @abstractmethod
    def execute(self):
        pass

class Saldo(Command):
    def execute(self):
        return self._obj.saldo()

class Extrato(Command):
    def execute(self):
        return self._obj.extrato()

class Transferencia(Command):
    def execute(self):
        return self._obj.transf()

class BankBackend:
    def saldo(self):
        return 5000.00

    def extrato(self):
        return [1000,-100,4100]

    def transf(self):
        return 'Transferencia Realizada'

# Client
class ClientUI:
    def __init__(self):
        self.__client = ClientBackend()
        self.__server = BankBackend()

        self.__main = tk.Tk()
        self.__main.title('Banco CES-22')
        self.__frame = tk.Frame(self.__main, height=500, width=100)

        labels = ['Consultar Saldo', 'Consultar Extrato', 'Realizar Transferência','Histórico']
        funcs = [self.saldo, self.extrato, self.transferencia, self.history]

        self.__buttons = []
        for i in range(len(labels)):
            self.__buttons.append(tk.Button(self.__frame, text=labels[i], command=funcs[i]))
            self.__buttons[i].pack()

        self.__frame.pack()
        self.__main.mainloop()

    def saldo(self):
        for button in self.__buttons:
            button.pack_forget()

        self.__aux = []
        text = tk.Text(self.__frame, height=1)
        text.insert(tk.INSERT, 'R$ ' + str(self.__client.execute(Saldo(self.__server))))
        text.configure(state='disabled')

        button = tk.Button(self.__frame, text='Voltar', command=self.back)
        self.__aux.append(button)
        self.__aux.append(text)

        text.pack()
        button.pack()

    def extrato(self):
        for button in self.__buttons:
            button.pack_forget()

        self.__aux = []
        text = tk.Text(self.__frame, height=7)
        for value in self.__client.execute(Extrato(self.__server)):
            text.insert(tk.INSERT, ('+' if value > 0 else '-') + str(abs(value)) + '\n' )

        text.configure(state='disabled')

        button = tk.Button(self.__frame, text='Voltar', command=self.back)
        self.__aux.append(button)
        self.__aux.append(text)

        text.pack()
        button.pack()

    def transferencia(self):
        for button in self.__buttons:
            button.pack_forget()

        self.__aux = []
        text = tk.Text(self.__frame, height=1)
        text.insert(tk.INSERT, self.__client.execute(Transferencia(self.__server)))
        text.configure(state='disabled')

        button = tk.Button(self.__frame, text='Voltar', command=self.back)
        self.__aux.append(button)
        self.__aux.append(text)

        text.pack()
        button.pack()

    def history(self):
        for button in self.__buttons:
            button.pack_forget()

        self.__aux = []
        text = tk.Text(self.__frame, height=7)
        text.insert(tk.INSERT, self.__client.history)
        text.configure(state='disabled')

        button = tk.Button(self.__frame, text='Voltar', command=self.back)
        self.__aux.append(button)
        self.__aux.append(text)

        text.pack()
        button.pack()

    def back(self):
        for item in self.__aux:
            item.destroy()

        self.__aux.clear()

        for button in self.__buttons:
            button.pack()


ClientUI()
