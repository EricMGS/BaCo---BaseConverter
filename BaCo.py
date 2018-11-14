#Programa que converte base numericas, da base 2 ate 62. Tem como valor de saida máximo 100 caracteres

#tabela de digitos para conversao de acordo com a posicao da string
digitos = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

#converte um valor para a base desejada
def Converte (entrada, base_entrada, base_saida):
    
    #transforma letras em numeros para efeito de calculo
    def DigitoDec (digito):
        for x in range(base_entrada):
            if digito == digitos[x]:
                return x
        return 'Erro'
    
    #converte a entrada em decimal
    decimal = 0
    expoente = 0
    for digito in range(len(entrada),0, -1):
        if DigitoDec (entrada [digito - 1]) == 'Erro':
            return 'Erro'
        else:
            decimal += base_entrada ** expoente * DigitoDec(entrada[digito - 1])
            expoente += 1
    
    #converte decimal para a saida
    count = 0
    saida = ''
    while decimal:
        x = int(decimal % base_saida)
        saida += digitos[x]
        decimal //= base_saida
        count += 1
    return saida[::-1]




#interface grafica
from tkinter import Tk, Label, Spinbox, Entry, messagebox, ttk, CENTER

#colors
bg_color = 'lightblue'
bg_box = 'gray95'

#window
window = Tk()
window.wm_iconbitmap('BaCo.ico') 
window.title("BaCo - BaseConverter")
window.geometry ('700x400')
window.resizable (0, 0)
window.configure (bg = bg_color)

#style
style=ttk.Style()
style.theme_use('vista')
style.configure ('TButton')

#labels
lblbase = Label (window, text = 'Base:', bg = bg_color, font = ('Arial', 12))
lblbase.place (relx = 0.5, rely = 0.1, anchor = CENTER)

lblfor = Label (window, text = 'para', bg = bg_color)
lblfor.place (relx = 0.5, rely = 0.2, anchor = CENTER)

lblvalue = Label (window, bg = bg_color, text = 'Valor: (0 - 1)', font = ('Arial', 12))
lblvalue.place (relx = 0.5, rely = 0.4, anchor = CENTER)

result = Label (window, bg = bg_color, text = 'Resultado:', font = ('Arial', 12))
result.place (relx = 0.5, rely = 0.6, anchor = CENTER)

final_result = Label (window, bg = bg_color)
final_result.place (relx = 0.5, rely = 0.7, anchor = CENTER)

signature = Label (window, bg = bg_color, text = './.-./../-.-./--/--./...')
signature.place (relx = 0.9, rely = 0.9, anchor = CENTER)
#spinbox
def clicked ():
    lblvalue.configure (text = 'Valor: (0 - ' +  digitos[int(base1.get())] + ')')

base1 = Spinbox(window, from_ = 2, to = 62, width = 5, bg = bg_box, state = 'readonly', command = clicked)
base1.place (relx = 0.4, rely= 0.2, anchor = CENTER)

base2 = Spinbox (window, from_ = 2, to = 62, width = 5, bg = bg_box, state = 'readonly')
base2.place (relx = 0.6, rely = 0.2, anchor = CENTER)

#entry
value = Entry (window, width = 110, bg = bg_box, justify = 'center')
value.place (relx = 0.5, rely = 0.5, anchor = CENTER)

#buttons
def convert():
    if Converte (value.get(), int(base1.get()), int(base2.get())) == 'Erro':
        return messagebox.showerror ('Erro 1', 'Valor invalido')
        
    res = Converte (value.get(), int(base1.get()), int(base2.get()))
    final_result.configure (text = res + '\n')
    
    if len(res) > 100:
        final_result.configure (text = '')
        return messagebox.showerror ('Erro 2', 'O resultado é muito grande\nMáximo: 100 digitos')

convert_btn = ttk.Button (window, text = 'Converter', command = convert, style = 'TButton')
convert_btn.place (relx = 0.3, rely = 0.9, anchor = CENTER)


def out ():
    if messagebox.askyesno ('Sair', 'Deseja mesmo sair?') == 1:
        import sys
        sys.exit()

out_btn = ttk.Button (window, text = 'Sair', command = out, style = 'TButton')
out_btn.place(relx = 0.7, rely = 0.9, anchor = CENTER)

window.mainloop ()


#EricMGS
#. .-. .. -.-.
#marco de 2018