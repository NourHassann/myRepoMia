
class Gru():
    health = 100
    energy = 500
    gruWeapon = ["Freeze Gun", "Electric Prod", "Mega Magnet", "Kalman Missile"]
    gruWeaponEnergy =[50,88,92,120]
    gruWeaponDamage = [11,18,10,20]
    gruWeaponRes =["inf",5,3,1] # 0 for inf
    gruShield = ["Energy-Projected BarrierGun","Selective Permeability"]
    gruShieldEnergy =[20,50]
    gruShieldSave = [40,90] #percent
    grushieldRes =["inf",2]
    def __init__(self): #constructor to initalize the attributes
        self.indexNumberWeapon = int(input("please enter number to select Weapon:\n 1 for Freeze Gun 2 for Electric prod 3 for Mega magnet 4 for kalman missle")) #talking the index of the list
        self.weapon = self.gruWeapon[self.indexNumberWeapon-1]
        self.damage= self.gruWeaponDamage[self.indexNumberWeapon-1]
        self.Genergy = self.gruWeaponEnergy[self.indexNumberWeapon-1]
        self.res = self.gruWeaponRes[self.indexNumberWeapon-1] 
        self.indexNumberShield= int(input("please enter number for the shield: 1 for Energy-Projected BarrierGun 2 for Selective Permeability"))
        self.shield = self.gruShield[self.indexNumberShield-1]
        self.shieldenergy =self.gruShieldEnergy[self.indexNumberShield-1]
        self.Shieldsave= self.gruShieldSave[self.indexNumberShield-1]
        self.shieldres = self.grushieldRes[self.indexNumberShield-1]
        
    def decreaseEnergyToGru (self):
         Gru.energy-= (self.Genergy+self.shieldenergy)
         if self.res and self.shieldres == "inf": #dec the res values also i tried to make the code send msg to the user when he use res who become 0 but it turned to infinite loop
             pass
         else:
               self.res-=1
               self.shieldres-=1
    
        


class vector(Gru):
    vectorWeapon = ["Laser Blasters", "Plasma Grenades", "Sonic Resonance Cannon"]
    vectorWeaponEnergy =[40,56,100]
    vectorWeaponDamage = [8,13,22]
    vectorWeaponRes =["inf",8,3] # 0 for inf
    vectorShield = ["Energy Net Trap","Quantum Deflector"]
    vectorShieldEnergy =[15,40]
    vectorShieldSave = [32,80] #percent
    vectorshieldRes =["inf",3]
    def __init__(self):
        self.indexNumberWeapon= int(input("please enter number to select weapon:\n 1 for Laser Blasters 2 for Plasma Grenades 3 forSonic Resonance Cannon"))
        self.indexNumberShield= int(input("please enter number to select shield:\n 1 for Energy Net Trap 2 for Quantum Deflector 3 for Mega magnet 4 for kalman missle"))
        self.weapon = self.vectorWeapon[self.indexNumberWeapon-1]
        self.damage= self.vectorWeaponDamage[self.indexNumberWeapon-1]
        self.Genergy = self.vectorWeaponEnergy[self.indexNumberWeapon-1]
        self.res = self.vectorWeaponRes[self.indexNumberWeapon-1]
        self.shield = self.vectorShield[self.indexNumberShield-1]
        self.shieldenergy =self.vectorShieldEnergy[self.indexNumberShield-1]
        self.Shieldsave= self.vectorShieldSave[self.indexNumberShield-1]
        self.shieldres = self.vectorshieldRes[self.indexNumberShield-1]
    def decreaseEnergyToVector (self):
        vector.energy-= (self.Genergy + self.shieldenergy)
        if self.res and self.shieldres == "inf":
           pass
        else:
             self.res-=1
             self.shieldres-=1
    


def damage(): #this fun apply the effect of other vilian use
    gru.health-= Vector.damage
    Vector.health -= gru.damage
    #print(gru.health)
    #print(Vector.health)
    #print(gru.energy)
    #print(Vector.energy)
    #print(gru.res)
    #print(gru.shieldres)
    #print(Vector.res)
    #print(Vector.shieldres)
def save(): #this fun apply the shield effect that the user choose
    gru.health+= (Vector.damage/100)* gru.Shieldsave
    Vector.health+= (gru.damage/100)*Vector.Shieldsave
gru = Gru() 
Vector = vector()
gru.decreaseEnergyToGru()
Vector.decreaseEnergyToVector()
save()
damage()
def round(): #this fun get the attribiute new value to finish the game
     while gru.health and Vector.health and gru.energy and Vector.energy>0:
         newWeaponGru = int(input("please enter new weapon for gru:\n 1 for Freeze Gun 2 for Electric prod 3 for Mega magnet 4 for kalman missle"))
         newShieldGru = int(input("please enter new shield for gru:\n 1 for Energy-Projected BarrierGun 2 for Selective Permeability"))
         newWeaponVector = int(input("please enter new weapon for vector:\n 1 for Laser Blasters 2 for Plasma Grenades 3 forSonic Resonance Cannon"))
         newShieldVector = int(input("please enter new shield for vector:\n 1 for Energy Net Trap 2 for Quantum Deflector"))
         gru.weapon = Gru.gruWeapon[newWeaponGru-1]
         gru.damage= Gru.gruWeaponDamage[newWeaponGru-1]
         gru.Genergy = Gru.gruWeaponEnergy[newWeaponGru-1]
         gru.res = Gru.gruWeaponRes[newWeaponGru-1]
         gru.shield = Gru.gruShield[newWeaponVector-1]
         gru.shieldenergy =Gru.gruShieldEnergy[newWeaponVector-1]
         gru.Shieldsave= Gru.gruShieldSave[newWeaponVector-1]
         gru.shieldres = Gru.grushieldRes[newWeaponVector-1]
         Vector.weapon = vector.vectorWeapon[newWeaponVector-1]
         Vector.damage= vector.vectorWeaponDamage[newWeaponVector-1]
         Vector.Genergy = vector.vectorWeaponEnergy[newWeaponVector-1]
         Vector.res = vector.vectorWeaponRes[newWeaponVector-1]
         Vector.shield = vector.vectorShield[newWeaponVector-1]
         Vector.shieldenergy =vector.vectorShieldEnergy[newWeaponVector-1]
         Vector.Shieldsave= vector.vectorShieldSave[newWeaponVector-1]
         Vector.shieldres = vector.vectorshieldRes[newWeaponVector-1]
         gru.decreaseEnergyToGru()
         Vector.decreaseEnergyToVector()
         save()
         damage()
def theWinner():
    if gru.health> Vector.health:
        print("Gru is the winner")
    else:
        print("vector is the winner")
round()
theWinner() 





    
  

