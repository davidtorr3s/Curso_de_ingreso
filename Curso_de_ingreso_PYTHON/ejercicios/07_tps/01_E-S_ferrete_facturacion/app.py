import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Perdón que lo entregue así pero tengo un problema con mi Github, para los próximos TP's ya lo voy a arreglar
Enunciado:
Para el departamento de facturación:
    A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
    B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	C.	ingresar tres precios de productos sumarlos y mostrar precio final (más IVA 21%).
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Producto 1")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_importe_1 = customtkinter.CTkEntry(master=self)
        self.txt_importe_1.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Producto 2")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_importe_2 = customtkinter.CTkEntry(master=self)
        self.txt_importe_2.grid(row=1, column=1)

        self.label_3 = customtkinter.CTkLabel(master=self, text="Producto 3")
        self.label_3.grid(row=2, column=0, padx=20, pady=10)
        
        self.txt_importe_3 = customtkinter.CTkEntry(master=self)
        self.txt_importe_3.grid(row=2, column=1)
       
        self.btn_total = customtkinter.CTkButton(master=self, text="TOTAL", command=self.btn_total_on_click)
        self.btn_total.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_promedio = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_promedio_on_click)
        self.btn_promedio.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_total_iva = customtkinter.CTkButton(master=self, text="TOTAL c/IVA", command=self.btn_total_iva_on_click)
        self.btn_total_iva.grid(row=5, pady=10, columnspan=2, sticky="nsew")

    def btn_total_on_click(self):
        number_one = self.txt_importe_1.get()
        number_one = float(number_one)
        
        number_two = self.txt_importe_2.get()
        number_two = float(number_two)
        
        number_three = self.txt_importe_3.get()
        number_three = float(number_three)
        
        resultado = number_one + number_two + number_three
        
        texto = f"La suma de los precios de los productos es de : {resultado}"
       
        alert (title= "Suma", message= texto) 

    def btn_promedio_on_click(self):
        number_one = self.txt_importe_1.get()
        number_one = float(number_one)
        
        number_two = self.txt_importe_2.get()
        number_two = float(number_two)
        
        number_three = self.txt_importe_3.get()
        number_three = float(number_three)
        
        resultado = number_one + number_two + number_three
        promedio = resultado / 3
        
        texto = f"El promedio de los precios es de : {promedio}"
       
        alert (title= "Promedio", message= texto) 

    def btn_total_iva_on_click(self):
        number_one = self.txt_importe_1.get()
        number_one = float(number_one)
        
        number_two = self.txt_importe_2.get()
        number_two = float(number_two)
        
        number_three = self.txt_importe_3.get()
        number_three = float(number_three)
        
        resultado = number_one + number_two + number_three
        porcentaje = (resultado * 21)/100 
        resultado_final = resultado + porcentaje
        
        texto = f"El precio final de los productos es de : {resultado_final}"
       
        alert (title= "Resultado (más IVA)", message= texto) 
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()