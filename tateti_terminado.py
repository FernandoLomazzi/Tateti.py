from tkinter import *
from tkinter import messagebox
from copy import copy, deepcopy
#+============Interfaz===============+#
main = Tk()
main.config(background='yellow')
miFrame = Frame(main,width=500,height=400)
miFrame.pack()
def inicio():
	titulo = Label(miFrame,width=20,height=15,text='Ta Te Ti',font=('Comic Sans MS',18),bg='yellow')
	titulo.grid(row=1,column=2,columnspan=1)
	jugar = Button(miFrame,width=5,text='Jugar',command=tateti_interfaz,padx=10,pady=5,cursor='pirate')
	jugar.grid(row=2,column=2)
	main.mainloop()

def tateti_interfaz():
	global b11,b12,b13,b21,b22,b23,b31,b32,b33
	miFrame.destroy()
	interfaz = Frame(main,width=500,height=400,bg='yellow')
	interfaz.pack()
	texto = Label(interfaz,text='Ta Te Ti',font=('Comic Sans MS',18),bg='yellow')
	texto.grid(row=1,columnspan=4)
	turno = True
	b11 = Button(interfaz,font=('Helvetica',15),width=5,height=5,cursor='hand2',command=lambda : tateti_x(b11,0,0))
	b12 = Button(interfaz,font=('Helvetica',15),width=5,height=5,cursor='hand2',command=lambda : tateti_x(b12,0,1))
	b13 = Button(interfaz,font=('Helvetica',15),width=5,height=5,cursor='hand2',command=lambda : tateti_x(b13,0,2))
	
	b21 = Button(interfaz,font=('Helvetica',15),width=5,height=5,cursor='hand2',command=lambda : tateti_x(b21,1,0))
	b22 = Button(interfaz,font=('Helvetica',15),width=5,height=5,cursor='hand2',command=lambda : tateti_x(b22,1,1))
	b23 = Button(interfaz,font=('Helvetica',15),width=5,height=5,cursor='hand2',command=lambda : tateti_x(b23,1,2))

	b31 = Button(interfaz,font=('Helvetica',15),width=5,height=5,cursor='hand2',command=lambda : tateti_x(b31,2,0))
	b32 = Button(interfaz,font=('Helvetica',15),width=5,height=5,cursor='hand2',command=lambda : tateti_x(b32,2,1))
	b33 = Button(interfaz,font=('Helvetica',15),width=5,height=5,cursor='hand2',command=lambda : tateti_x(b33,2,2))

	b11.grid(row=2,column=1)
	b12.grid(row=2,column=2)
	b13.grid(row=2,column=3)

	b21.grid(row=3,column=1)
	b22.grid(row=3,column=2)
	b23.grid(row=3,column=3)
	
	b31.grid(row=4,column=1)
	b32.grid(row=4,column=2)
	b33.grid(row=4,column=3)

def deshabilitar_botones():
	b11.config(state=DISABLED)
	b12.config(state=DISABLED)
	b13.config(state=DISABLED)
	b21.config(state=DISABLED)
	b22.config(state=DISABLED)
	b23.config(state=DISABLED)
	b31.config(state=DISABLED)
	b32.config(state=DISABLED)
	b33.config(state=DISABLED)

#+=====Implementacion=======+
hacer = ()
g = [
[' ',' ',' '],
[' ',' ',' '],
[' ',' ',' ']]
def actions(g):
	actions = []
	for i in range(3):
		for j in range(3):
			if g[i][j]==' ':
				actions.append((i,j))
	return actions
def ganador(g):
	for i in range(3):
		if g[0][i]==g[1][i]==g[2][i]!=' ' or g[i][0]==g[i][1]==g[i][2]!=' ':
			return True
	if g[0][0]==g[1][1]==g[2][2]!=' ' or g[0][2]==g[1][1]==g[2][0]!=' ':
		return True
	return False
def valor(g):
	if ganador(g):
		if turno_x(g):
			return -1
		else:
			return 1
	return 0
def completo(g):
	turnos = 0
	for i in g:
		turnos += i.count('x')+i.count('o')
	return turnos==9
def transicion(g,accion,cambio):
	global b11,b12,b13,b21,b22,b23,b31,b32,b33
	if turno_x(g):
		g[accion[0]][accion[1]] = 'x'
	else:
		if cambio:
			s = 'b'+str(accion[0]+1)+str(accion[1]+1)
			exec("%s['text'] = 'O'" %s)
		g[accion[0]][accion[1]] = 'o'
	return g
def turno_x(g):
	x = o = 0
	for i in range(3):
		x += g[i].count('x')
		o += g[i].count('o')
	if x>o:
		return False
	return True
def max_value(g,instancia):
	global hacer
	instancia += 1
	if ganador(g) or completo(g):
		return valor(g)
	aux = -4
	for acciones in actions(g):
		x = min_value(transicion(deepcopy(g),acciones,False),instancia)
		if aux<x:
			aux = x
	return aux
def min_value(g,instancia):
	global hacer
	instancia += 1
	if ganador(g) or completo(g):
		return valor(g)
	aux = 4
	for acciones in actions(g):
		x = max_value(transicion(deepcopy(g),acciones,False),instancia)
		if aux>x:
			aux = x
			if instancia==1:
				hacer = acciones
	return aux
def terminado(g):
	if ganador(g) or completo(g):
		if valor(g)==1:
			messagebox.showinfo("Fin del juego","Ganaste!!")
		elif valor(g)==0:
			messagebox.showinfo("Fin del juego","Empate :-(")
		else:
			messagebox.showinfo("Fin del juego","Perdiste uwu")

		deshabilitar_botones()
		return True
	return False
def tateti_x(boton,i,j):
	global g
	if boton['text']=='X' or boton['text']=='O':
		return
	g[i][j] = 'x'	
	boton['text'] = 'X'
	if terminado(g):
		return
	tateti_o()
def tateti_o():
	global g,hacer
	min_value(g,0)
	transicion(g,hacer,True)
	if terminado(g):
		return

inicio()