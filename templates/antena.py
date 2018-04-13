class  Antena():
	color = "Verde"


class insecto():

	nombre = ""
	antenas =Antena("2")
	def __init__(seft,nombre):
		self.nombre = nombre
i=insecto("mosca")
print (i.nombre, i.antenas, i.color)
