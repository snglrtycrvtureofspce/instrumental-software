
class person:	
	counter=0
	def __init__(self,name,age,tipe):
		
		self.name=name
		self.age=age
		self.tipe=tipe
	

	def display_input(self):
		print(f'{self.name} \n{self.tipe}\n{self.age}\n___________')

def skolko_chelovek():
	print(person.counter)

class Kosmonaft(person):
	__priv_god=2020
	def __init__(self,name,age,tipe):
		person.__init__(self,name,age,tipe)
		person.counter=person.counter+1
		

	def display_input1(self):
		print(f'{self.name} \n{self.tipe}\n{self.age}\n___________')
	def otv1(self):
		print(Kosmonaft.__priv_god)

	def die(self) :
		self.name="die"
		self.age=0
		self.tipe="die"

class proverka(Kosmonaft):
	def dorova():
		print('dorova')
	def otv2(self):
		print(proverka.__priv_god)

class MKS(person):
	
	def dobPer(self,nazvanie,znachenie):
		MKS.nazvanie=znachenie
	def vivPer(self,nazvanie):
		print(nazvanie)


d=Kosmonaft("Ученик",20,"D")
d.display_input1()
d.die()
d.display_input1()
d.otv1()
v=proverka("Leron",23,"v")
v.die()
v.display_input1()
v.otv1()#тут нужно поствить otv2() для проверки я написал otv1() что бы работало
L=MKS('chelovek',20,'C')
L.dobPer('dok',23)
L.vivPer('dok')
skolko_chelovek()
















