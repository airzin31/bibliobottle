#Bouteille
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
#import sqlite3
from pandas.core.nanops import bottleneck_switch


class Bottle:
    def __init__(self,Code,Country,Region,Quantity,disponible="available"):
        self.Code = Code
        self.Country=Country
        self.Region=Region
        self.Quantity=Quantity
        self.disponible = disponible

    def CaracteristiqueBottle(self):
        print("The bottle:{} Country:{} Region:{} Qty:{}".format(self.Code,self.Country,self.Region,self.Quantity))

bordeau=Bottle(33001,"France","Bordeau",21)
bordeau.CaracteristiqueBottle()

class Beer(Bottle):
    def __init__(self,Code,Country,Region,Quantity,Aroma,Savor,ColorB,disponible):
        super().__init__(Code,Country,Region,Quantity,disponible)
        self.Savor = Savor
        self.Aroma = Aroma
        self.ColorB = ColorB

    def CaracteristiqueBeer(self):
        # Appel de la méthode de la classe Mère
        print("Beer:{} Country:{} Region:{} Color:{} Aroma:{} Savor:{} Qty:{}".format(self.Code,self.Country,self.Region,self.ColorB,self.Aroma,self.Savor,self.Quantity))

Belge=Beer(12,"Belge","Bruxelle",999,"Café","Caramel","Blonde","available")
Belge.CaracteristiqueBeer()

class Wine(Bottle):
    def __init__(self,Code,Country,Region,Quantity,Domain,Year,Tanin,ColorW,disponible):
        super().__init__(Code,Country,Region,Quantity,disponible)
        self.Domain = Domain
        self.Year = Year
        self.ColorW = ColorW
        self.Tanin = Tanin

    def CaracteristiqueWine(self):
        print("Wine:{} Country:{} Region:{} Domain:{} Color:{} Year:{} Tanin Strength:{} Qty:{} ".format(self.Code,self.Country,self.Region,self.Domain,self.ColorW,self.Year,self.Tanin,self.Quantity))

GrandCru=Wine(12,"France","Aveyron",69,"Rodez",1986,4,"Red","available")
GrandCru.CaracteristiqueWine()

class Personne:
    def __init__(self,nom,prenom,country,year):
        self.nom = nom
        self.prenom = prenom
        self.country = country
        self.year = year

    def sePresenter(self):
        print("Je m'appelle {} {}, je viens de {}, né en {}.".format(self.prenom,self.nom,self.country,self.year))

Ludo=Personne("SINmammmmmammamaSE","Ludovic","France","1986")
Ludo.sePresenter()



class IhmFunction(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('StockBarV14.ui',self)
        self.Belge =[]
        self.bordeau=[]
        self.loginUser=[]
        ouvrir(self,Belge,bordeau)
        affichage(self,Belge,bordeau)

        self.listWidgetRef.clicked.connect(self.Select)
        self.pbSaveSub.clicked.connect(self.SaveSub)
        self.pbDisconnect.clicked.connect(self.Disconnect)
        self.pbModify.clicked.connect(self.Modify)
        self.bottonConnectionSub.clicked.connect(self.Connection)

        #self.bpbPickUpDis.clicked.connect(self.BPickUp)
        #rent wine button
        self.pushButtonpicking_2.clicked.connect(self.rentWine)
        #rent beer button
        self.pushButtonpicking.clicked.connect(self.rentBeer)
        self.pbBeerSort.clicked.connect(self.SortBeer)
        self.pbWineSort.clicked.connect(self.SortWine)
        self.pbWineSearch.clicked.connect(self.WSearch)
        self.pbBeerSearch.clicked.connect(self.BSearch)
        self.pbSearchRef.clicked.connect(self.Search)
        #self.pbCustomerRef.clicked.connect(self.Return)
        self.pbNewRef.clicked.connect(self.New)
        self.deleteButton.clicked.connect(self.Delete)
        self.pushConsult.clicked.connect(self.consultRentBottle)
        self.pushReturn.clicked.connect(self.returnBottle)

    #def returnBottle(self):

     #   if (len(self.loginUser) != 0):


    def consultRentBottle(self):

        self.listWidgetRenter.clear()
        if (len(self.loginUser) != 0):
            #affichage dans Customer Wine
            if len(self.bordeau)!=0:
                for p in self.bordeau:
                    print(str(p))
                    if p.disponible == str(self.loginUser):
                        self.listWidgetRenter.addItem("Wine\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(p.Code,p.Country,p.Region,p.Quantity,p.Domain,p.Year,p.Tanin,p.ColorW,p.disponible))

            #affichage dans Customer Beer
            if len(self.Belge)!=0:
                for i in self.Belge:
                    print(str(i))
                    if i.disponible == str(self.loginUser):
                        self.listWidgetRenter.addItem("Beer\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(i.Code,i.Country,i.Region,i.Quantity,i.Aroma,i.Savor,i.ColorB,i.disponible))


    def rentBeer(self):
        print("rent beer")
        if (len(self.loginUser) != 0):

            selection=self.BeerList.currentItem()
            #vérifie le format de la selection pour éviter le bug si c'est vide
            if isinstance(selection,QListWidgetItem)==True:
                #passage d'une variable QListWidgetItem à une chaine de caractère puis à une liste
                selection=selection.text()
                selection = selection.rstrip('\n')
                selectionList = selection.split("\t| ")
                bottleName = selectionList[1]

                for i in self.Belge:
                    if bottleName == i.Code:
                        #modifie les valeurs enregistrer pour cette reférence par les nouvelles
                        i.disponible = str(self.loginUser)
                        affichage(self,Belge,bordeau)
                        enregistrer(self)


                print("test rentBeer")
                print(selectionList)


    def rentWine(self):

        if (len(self.loginUser) != 0):

            selection=self.WineList.currentItem()
            #vérifie le format de la selection pour éviter le bug si c'est vide
            if isinstance(selection,QListWidgetItem)==True:
                #passage d'une variable QListWidgetItem à une chaine de caractère puis à une liste
                selection=selection.text()
                selection = selection.rstrip('\n')
                selectionList = selection.split("\t| ")
                bottleName = selectionList[1]

                for i in self.bordeau:
                    if bottleName == i.Code:
                        #modifie les valeurs enregistrer pour cette reférence par les nouvelles
                        i.disponible = str(self.loginUser)
                        affichage(self,Belge,bordeau)
                        enregistrer(self)

                print("test rentWine")
                print(selectionList)




    def SaveSub(self):
        file1 = open('fichTxtPers.txt','a')
        self.persAlready.setText("")
        print(self.FirstNameSub.text())
        pers = Personne(self.FirstNameSub.text(),self.LastNameSub.text(),self.CountrySub.text(),self.YearSub.text())
        print ( pers.sePresenter())
        file1 = open('fichTxtPers.txt','r+')

        dejaExistant=False
        for i in file1:
            i = i.rstrip('\n')
            temp = i.split("\t| ")
            if temp[0]==self.LastNameSub.text():
                dejaExistant=True
                self.persAlready.setText("Already Exist")

                print("déja existant")
        if not dejaExistant:

            file1.write("{}\t| {}\t| {}\t| {}\n".format(pers.prenom,pers.nom,pers.country,pers.year))
            self.persAlready.setText("well recorded")
        file1.close



        #█conn = sqlite3.connect("maBD.bd")
        #fichiertPers = open('fichTxtPers.txt','w')
        #person1 = pers.sePresenter()
        #print ( person1)


        #☺file1.write('helloooooo \n, fgfdgfdgfdgfdgf\n')
        #file1.write(str(person1))
        #file1.close()
        #fichiertPers = close('fichTxtPers.txt','a')

    def Connection(self):
        login = self.LastNameSubConnection.text()

        file1 = open('fichTxtPers.txt','r+')
        print("login" + login)
        dejaExistant = False
        for i in file1:
            i = i.rstrip('\n')
            temp = i.split("\t| ")
            if temp[0]==login :
                dejaExistant=True
                self.persAlready.setText("Bienvenu " + login)
                self.loginName.setText(login)
                self.loginUser = login
        file1.close()

    def SortWine(self):
        TempWine=self.bordeau
        if self.comboBoxWine.currentText()=="Bottle Name":
            TempWine=sorted(self.bordeau, key=lambda Wine: Wine.Code)
        elif self.comboBoxWine.currentText()=="Country":
            TempWine=sorted(self.bordeau, key=lambda Wine: Wine.Country)
        elif self.comboBoxWine.currentText()=="Region":
            TempWine=sorted(self.bordeau, key=lambda Wine: Wine.Region)
        elif self.comboBoxWine.currentText()=="Quantity":
            TempWine=sorted(self.bordeau, key=lambda Wine: Wine.Quantity)
        elif self.comboBoxWine.currentText()=="Domain":
            TempWine=sorted(self.bordeau, key=lambda Wine: Wine.Domain)
        elif self.comboBoxWine.currentText()=="Year":
            TempWine=sorted(self.bordeau, key=lambda Wine: Wine.Year)
        elif self.comboBoxWine.currentText()=="Tanin":
            TempWine=sorted(self.bordeau, key=lambda Wine: Wine.Tanin)
        elif self.comboBoxWine.currentText()=="Color":
            TempWine=sorted(self.bordeau, key=lambda Wine: Wine.ColorW)
        self.bordeau=TempWine
        affichage(self,Belge,bordeau)


    def SortBeer(self):
        TempBeer=self.Belge
        if self.comboBoxBeer.currentText()=="Bottle Name":
            TempBeer=sorted(self.Belge, key=lambda Beer: Beer.Code)
        elif self.comboBoxBeer.currentText()=="Country":
            TempBeer=sorted(self.Belge, key=lambda Beer: Beer.Country)
        elif self.comboBoxBeer.currentText()=="Region":
            TempBeer=sorted(self.Belge, key=lambda Beer: Beer.Region)
        elif self.comboBoxBeer.currentText()=="Quantity":
            TempBeer=sorted(self.Belge, key=lambda Beer: Beer.Quantity)
        elif self.comboBoxBeer.currentText()=="Aroma":
            TempBeer=sorted(self.Belge, key=lambda Beer: Beer.Aroma)
        elif self.comboBoxBeer.currentText()=="Savor":
            TempBeer=sorted(self.Belge, key=lambda Beer: Beer.Savor)
        elif self.comboBoxBeer.currentText()=="Color":
            TempBeer=sorted(self.Belge, key=lambda Beer: Beer.ColorB)
        self.Belge=TempBeer
        affichage(self,Belge,bordeau)



    def SearchSub(self):
        print("SearchSub")

    def Register(self):
        print("Register")

    def Disconnect(self):
        self.loginUser = []
        self.loginName.setText("Vous n'êtes pas connecté.")
        self.persAlready.setText("")
        print("disconnect")

    def BSearch(self):
        self.BeerList.clear()
        #recherche par bottle name
        if self.comboBoxBeer.currentText()=="Bottle Name":
            for i in self.Belge:
                if self.bCodeDis.text().lower()==i.Code[0:len(self.bCodeDis.text())].lower():
                    self.BeerList.addItem("Beer\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(i.Code,i.Country,i.Region,i.Quantity,i.Aroma,i.Savor,i.ColorB))
        #recherche par région
        elif self.comboBoxBeer.currentText()=="Region":
            for i in self.Belge:
                if self.bRegionDis.text().lower()==i.Region[0:len(self.bRegionDis.text())].lower():
                    self.BeerList.addItem("Beer\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(i.Code,i.Country,i.Region,i.Quantity,i.Aroma,i.Savor,i.ColorB))

        #recherche par pays
        elif self.comboBoxBeer.currentText()=="Country":
            for i in self.Belge:
                if self.bCountryDis.text().lower()==i.Country[0:len(self.bCountryDis.text())].lower():
                    self.BeerList.addItem("Beer\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(i.Code,i.Country,i.Region,i.Quantity,i.Aroma,i.Savor,i.ColorB))

        #recherche exacte par couleur de bière
        elif self.comboBoxBeer.currentText()=="Color":
            for i in self.Belge:
                if self.bColorDis.currentText()==i.ColorB:
                    self.BeerList.addItem("Beer\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(i.Code,i.Country,i.Region,i.Quantity,i.Aroma,i.Savor,i.ColorB))
        #recherche par Arome
        elif self.comboBoxBeer.currentText()=="Aroma":
            for i in self.Belge:
                if self.bAromaDis.text().lower()==i.Aroma[0:len(self.bAromaDis.text())].lower():
                    self.BeerList.addItem("Beer\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(i.Code,i.Country,i.Region,i.Quantity,i.Aroma,i.Savor,i.ColorB))
        #recherche par savor
        elif self.comboBoxBeer.currentText()=="Savor":
            for i in self.Belge:
                if self.bSavorDis.text().lower()==i.Savor[0:len(self.bSavorDis.text())].lower():
                    self.BeerList.addItem("Beer\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(i.Code,i.Country,i.Region,i.Quantity,i.Aroma,i.Savor,i.ColorB))
        #recherche par quantité
        elif self.comboBoxBeer.currentText()=="Quantity":
            for i in self.Belge:
                if self.bQuantityDis.text().lower()==i.Quantity[0:len(self.bQuantityDis.text())].lower():
                    self.BeerList.addItem("Beer\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(i.Code,i.Country,i.Region,i.Quantity,i.Aroma,i.Savor,i.ColorB))

        #retourne à l'affichage sans recherche
        elif self.comboBoxBeer.currentText()=="None":
            affichage(self,Belge,bordeau)

    def WSearch(self):
        self.WineList.clear()
        #recherche par bottle name
        if self.comboBoxWine.currentText()=="Bottle Name":
            for p in self.bordeau:
                if self.wCodeDis.text().lower()==p.Code[0:len(self.wCodeDis.text())].lower():
                    self.WineList.addItem("Wine\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(p.Code,p.Country,p.Region,p.Quantity,p.Domain,p.Year,p.Tanin,p.ColorW))
        #recherche par région
        elif self.comboBoxWine.currentText()=="Region":
            for p in self.bordeau:
                if self.wRegionDis.text().lower()==p.Region[0:len(self.wRegionDis.text())].lower():
                    self.WineList.addItem("Wine\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(p.Code,p.Country,p.Region,p.Quantity,p.Domain,p.Year,p.Tanin,p.ColorW))

        #recherche par pays
        elif self.comboBoxWine.currentText()=="Country":
            for p in self.bordeau:
                if self.wCountryDis.text().lower()==p.Country[0:len(self.wCountryDis.text())].lower():
                    self.WineList.addItem("Wine\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(p.Code,p.Country,p.Region,p.Quantity,p.Domain,p.Year,p.Tanin,p.ColorW))

        #recherche exacte par couleur du vin
        elif self.comboBoxWine.currentText()=="Color":
            for p in self.bordeau:
                if self.wColorDis.currentText()==p.ColorW:
                    self.WineList.addItem("Wine\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(p.Code,p.Country,p.Region,p.Quantity,p.Domain,p.Year,p.Tanin,p.ColorW))

        #recherche par Domain
        elif self.comboBoxWine.currentText()=="Domain":
            for p in self.bordeau:
                if self.wDomainDis.text().lower()==p.Domain[0:len(self.wDomainDis.text())].lower():
                    self.WineList.addItem("Wine\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(p.Code,p.Country,p.Region,p.Quantity,p.Domain,p.Year,p.Tanin,p.ColorW))
        #recherche par Year
        elif self.comboBoxWine.currentText()=="Year":
            for p in self.bordeau:
                if self.wYearDis.text().lower()==p.Year[0:len(self.wYearDis.text())].lower():
                    self.WineList.addItem("Wine\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(p.Code,p.Country,p.Region,p.Quantity,p.Domain,p.Year,p.Tanin,p.ColorW))
        #recherche par quantité
        elif self.comboBoxWine.currentText()=="Quantity":
            for p in self.bordeau:
                if self.wQuantityDis.text().lower()==p.Quantity[0:len(self.wQuantityDis.text())].lower():
                    self.WineList.addItem("Wine\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(p.Code,p.Country,p.Region,p.Quantity,p.Domain,p.Year,p.Tanin,p.ColorW))

        #recherche par Tanin
        elif self.comboBoxWine.currentText()=="Tanin":
            for p in self.bordeau:
                if self.wTaninDis.currentText()==p.Tanin:
                    self.WineList.addItem("Wine\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(p.Code,p.Country,p.Region,p.Quantity,p.Domain,p.Year,p.Tanin,p.ColorW))
        #retourne à l'affichage sans recherche
        elif self.comboBoxWine.currentText()=="None":
            affichage(self,Belge,bordeau)


    def Select(self):
        #selection de la valeur de la liste à supprimer par un clic dans la liste affichée
        selection=self.listWidgetRef.currentItem()
        #passage d'une variable QListWidgetItem à une chaine de caractère puis à une liste
        selection=selection.text()
        #la fonction suivante élimine le retour à la ligne
        selection = selection.rstrip('\n')
        #la fonction suivante sépare la chaine de caractere en une liste avec le découpe selon la tabulation suivi d'un espace
        selectionList = selection.split("\t| ")
        # regarde si une bière ou du vin a été choisi
        if selectionList[0]=="Wine":
            for p in self.bordeau:
                #recherche la valeur selectionner dans la liste des vins et renseigne ses caratéristiques associées
                if selectionList[1]==p.Code:
                    self.CodeRef.setText(p.Code)
                    self.CountryRef.setText(p.Country)
                    self.RegionRef.setText(p.Region)
                    self.QuantityRef.setText(p.Quantity)
                    self.DomainRef.setText(p.Domain)
                    self.YearRef.setText(p.Year)
                    self.TaninRef.setCurrentText(p.Tanin)
                    self.wColorRef.setCurrentText(p.ColorW)

        elif selectionList[0]=="Beer":
            #recherche la valeur selectionner dans la liste des bières et renseigne ses caratéristiques associées
            for i in self.Belge:
                if selectionList[1]==i.Code:
                    self.CodeRef.setText(i.Code)
                    self.CountryRef.setText(i.Country)
                    self.RegionRef.setText(i.Region)
                    self.QuantityRef.setText(i.Quantity)
                    self.AromaRef.setText(i.Aroma)
                    self.SavorRef.setText(i.Savor)
                    self.bColorRef.setCurrentText(i.ColorB)

    def Modify(self):
        #recherche si la référence est presente dans les bières
        for i in self.Belge:
            if self.CodeRef.text()==i.Code:
                #modifie les valeurs enregistrer pour cette reférence par les nouvelles
                i.Country=self.CountryRef.text()
                i.Region=self.RegionRef.text()
                i.Quantity=self.QuantityRef.text()
                i.Aroma=self.AromaRef.text()
                i.Savor=self.SavorRef.text()
                i.ColorB=self.bColorRef.currentText()
                affichage(self,Belge,bordeau)
                enregistrer(self)

        #idem dans les vins
        for p in self.bordeau:
            if self.CodeRef.text()==p.Code:
                p.Country=self.CountryRef.text()
                p.Region=self.RegionRef.text()
                p.Quantity=self.QuantityRef.text()
                p.Domain=self.DomainRef.text()
                p.Year=self.YearRef.text()
                p.Tanin=self.TaninRef.currentText()
                p.ColorW=self.wColorRef.currentText()
                affichage(self,Belge,bordeau)
                enregistrer(self)




    def Search(self):
        self.listWidgetRef.clear()
        #recherche par Bottle Name
        #la fonction .lower() permet de mettre tout en minuscule pour la comparaison et ainsi éliminer les problème de casse
        if self.comboBoxSearchRef.currentText()=="Code":
            for i in self.Belge:
                if self.CodeRef.text().lower()==i.Code[0:len(self.CodeRef.text())].lower():
                    self.listWidgetRef.addItem("Beer\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(i.Code,i.Country,i.Region,i.Quantity,i.Aroma,i.Savor,i.ColorB))
            for p in self.bordeau:
                if self.CodeRef.text().lower()==p.Code[0:len(self.CodeRef.text())].lower():
                    self.listWidgetRef.addItem("Wine\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(p.Code,p.Country,p.Region,p.Quantity,p.Domain,p.Year,p.Tanin,p.ColorW))
        #recherche par région
        if self.comboBoxSearchRef.currentText()=="Region":
            for i in self.Belge:
                if self.RegionRef.text().lower()==i.Region[0:len(self.RegionRef.text())].lower():
                    self.listWidgetRef.addItem("Beer\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(i.Code,i.Country,i.Region,i.Quantity,i.Aroma,i.Savor,i.ColorB))
            for p in self.bordeau:
                if self.RegionRef.text().lower()==p.Region[0:len(self.RegionRef.text())].lower():
                    self.listWidgetRef.addItem("Wine\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(p.Code,p.Country,p.Region,p.Quantity,p.Domain,p.Year,p.Tanin,p.ColorW))
        #recherche par pays
        if self.comboBoxSearchRef.currentText()=="Country":
            for i in self.Belge:
                if self.CountryRef.text().lower()==i.Country[0:len(self.CountryRef.text())].lower():
                    self.listWidgetRef.addItem("Beer\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(i.Code,i.Country,i.Region,i.Quantity,i.Aroma,i.Savor,i.ColorB))
            for p in self.bordeau:
                if self.CountryRef.text().lower()==p.Country[0:len(self.CountryRef.text())].lower():
                    self.listWidgetRef.addItem("Wine\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(p.Code,p.Country,p.Region,p.Quantity,p.Domain,p.Year,p.Tanin,p.ColorW))
        #recherche exacte par couleur de bière
        if self.comboBoxSearchRef.currentText()=="Color Beer":
            for i in self.Belge:
                if self.bColorRef.currentText()==i.ColorB:
                    self.listWidgetRef.addItem("Beer\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(i.Code,i.Country,i.Region,i.Quantity,i.Aroma,i.Savor,i.ColorB))
        #recherche exacte par couleur de vin
        if self.comboBoxSearchRef.currentText()=="Color Wine":
            for p in self.bordeau:
                if self.wColorRef.currentText()==p.ColorW:
                    self.listWidgetRef.addItem("Wine\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(p.Code,p.Country,p.Region,p.Quantity,p.Domain,p.Year,p.Tanin,p.ColorW))
        #retourne à l'affichage sans recherche
        if self.comboBoxSearchRef.currentText()=="None":
            affichage(self,Belge,bordeau)


    def Return(self):
        print("return")
        if self.WineBeerRef.currentText() =="Wine":
            print("wine")
        elif self.WineBeerRef.currentText() =="Beer":
            print("beer")

    def New(self):
        self.existing.setText("")
        fichiertBeer = open('fichTxtBeer.txt','r+')
        fichiertWine = open('fichTXTWine.txt','r+')

        bottleName= self.CodeRef.text()
        print(bottleName)

        dejaExistant=False

        if self.WineBeerRef.currentText() =="Wine":

            for i in fichiertWine:
                i = i.rstrip('\n')
                temp = i.split("\t| ")
                if temp[0]==bottleName :
                    print("déja existant")
                    dejaExistant=True
                    self.existing.setText("Already Exist")


            if not dejaExistant:
                Wine_c(self,Belge,bordeau)

        elif self.WineBeerRef.currentText() =="Beer":

            for i in fichiertBeer:
                i = i.rstrip('\n')
                temp = i.split("\t| ")
                if temp[0]==bottleName :
                    dejaExistant=True
                    self.existing.setText("Already Exist")


                    print("déja existant")




            if not dejaExistant:

                Beer_c(self,Belge)


        affichage(self,Belge,bordeau)
        enregistrer(self)
        fichiertBeer.close
        fichiertWine.close



    def Delete(self):

        #selection de la valeur de la liste à supprimer par un clic dans la liste affichée
        selection=self.listWidgetRef.currentItem()
        #vérifie le format de la selection pour éviter le bug si c'est vide
        if isinstance(selection,QListWidgetItem)==True:
            #passage d'une variable QListWidgetItem à une chaine de caractère puis à une liste
            selection=selection.text()
            selection = selection.rstrip('\n')
            selectionList = selection.split("\t| ")

            #recherche si c'est du vin ou de la bière et efface dans la bonne variable
            if selectionList[0]=="Wine":
                for p in self.bordeau:
                    if selectionList[1]==p.Code:
                        self.bordeau.remove(p)

            elif selectionList[0]=="Beer":
                for i in self.Belge:
                    if selectionList[1]==i.Code:
                        self.Belge.remove(i)
        #affiche la liste apres modification puis sauvegarde cette modification
        affichage(self,Belge,bordeau)
        enregistrer(self)



def Wine_c(self,Belge,bordeau):
    newWine = Wine(self.CodeRef.text(),self.CountryRef.text(),self.RegionRef.text(),self.QuantityRef.text(),self.DomainRef.text(),self.YearRef.text(),self.TaninRef.currentText(),self.wColorRef.currentText())
    newWine.CaracteristiqueWine()
    self.bordeau.append(newWine)


def Beer_c(self,Belge):
    newBeer=Beer(self.CodeRef.text(),self.CountryRef.text(),self.RegionRef.text(),self.QuantityRef.text(),self.AromaRef.text(),self.SavorRef.text(),self.bColorRef.currentText())
    newBeer.CaracteristiqueBeer()
    self.Belge.append(newBeer)


def enregistrer(self):
    fichiertBeer = open('fichTxtBeer.txt','w')
    fichiertWine = open('fichTXTWine.txt','w')
    for i in self.Belge:
        fichiertBeer.write("{}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(i.Code,i.Country,i.Region,i.Quantity,i.Aroma,i.Savor,i.ColorB,i.disponible))
    for p in self.bordeau:
        fichiertWine.write("{}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(p.Code,p.Country,p.Region,p.Quantity,p.Domain,p.Year,p.Tanin,p.ColorW,p.disponible))
    fichiertBeer.close
    fichiertWine.close



def ouvrir(self,Belge,bordeau):

    fichiertBeer = open('fichTxtBeer.txt','a')
    fichiertBeer.close
    fichiertBeer = open('fichTxtBeer.txt','r')
    for ligneb in fichiertBeer:
        ligneb = ligneb.rstrip('\n')
        Beerf = ligneb.split('\t| ')
        if len(Beerf) > 5:
            self.Belge.append(Beer(Beerf[0],Beerf[1],Beerf[2],Beerf[3],Beerf[4],Beerf[5],Beerf[6],Beerf[7]))
    fichiertBeer.close

    fichiertWine = open('fichTXTWine.txt','a')
    fichiertWine.close
    fichiertWine = open('fichTXTWine.txt','r')
    for lignew in fichiertWine:
        lignew = lignew.rstrip('\n')
        Winef = lignew.split('\t| ')
        if len(Winef) >6:
            self.bordeau.append(Wine(Winef[0],Winef[1],Winef[2],Winef[3],Winef[4],Winef[5],Winef[6],Winef[7],Winef[8]))
    fichiertWine.close


def affichage(self,Belge,bordeau, loginUser="available"):
    #afficahge dans Refund
    self.listWidgetRef.clear()
    if len(self.Belge)!=0:
        for i in self.Belge:
            self.listWidgetRef.addItem("Beer\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(i.Code,i.Country,i.Region,i.Quantity,i.Aroma,i.Savor,i.ColorB,i.disponible))
    for p in self.bordeau:
        self.listWidgetRef.addItem("Wine\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(p.Code,p.Country,p.Region,p.Quantity,p.Domain,p.Year,p.Tanin,p.ColorW,p.disponible))

    #affichage dans Customer Wine
    self.WineList.clear()
    if len(self.bordeau)!=0:
        for p in self.bordeau:
            if p.disponible == loginUser:
                self.WineList.addItem("Wine\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(p.Code,p.Country,p.Region,p.Quantity,p.Domain,p.Year,p.Tanin,p.ColorW,p.disponible))

    #affichage dans Customer Beer
    self.BeerList.clear()
    if len(self.Belge)!=0:
        for i in self.Belge:
            if i.disponible == loginUser:
                self.BeerList.addItem("Beer\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\t| {}\n".format(i.Code,i.Country,i.Region,i.Quantity,i.Aroma,i.Savor,i.ColorB,i.disponible))





app = QApplication([])
ihm=IhmFunction()
ihm.show()
app.exec_()