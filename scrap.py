import requests
from bs4 import BeautifulSoup
import lxml
import pyshorteners as ps



def acortador(link):
    shorti = ps.Shortener()
    url= shorti.dagd.short(link)
    return url



class Links_download:

    def __init__(self,link, producto):
        self.link = link
        self.producto = producto

    def parse(self):
        try:
            page = requests.get(self.link + self.producto) 
            return BeautifulSoup(page.text,'lxml')
        except:
            print("Error al pedir requests " + page)


class Get_bloque:
    
    def __init__(self,soup,bloque,bloque_class,bloque_class_id):
        self.soup = soup
        self.bloque = bloque
        self.bloque_class = bloque_class
        self.bloque_class_id = bloque_class_id

    def get_body(self):
        return self.soup.find_all(self.bloque, attrs={self.bloque_class : self.bloque_class_id})



class Get_title():
    
    def __init__(self,bloque_div,title_etiqueta,title_etiqueta_class ,title_etiqueta_class_id):
        self.bloque_div = bloque_div
        self.title_etiqueta = title_etiqueta
        self.title_etiqueta_class = title_etiqueta_class
        self.title_etiqueta_class_id = title_etiqueta_class_id

    def has_data_bloque(self):
        list_data = []
        for i in self.bloque_div:
            name = i.find(self.title_etiqueta, attrs = {self.title_etiqueta_class : self.title_etiqueta_class_id}).get_text()
            name = name.replace('  ','')
            name = name.replace('S/','')
            name = name.replace('. ','')
            name = name.replace(', ','')
            name = name.replace('.00','')
            name = name.replace('\n','')
            list_data.append(name)
        return list_data
    
    def has_link(self):
        list_links = []

        for i in self.bloque_div:

            links = i.a.get('href')

            if self.title_etiqueta in links:
                links=acortador(links)
                list_links.append(links)
            else:
                links= self.title_etiqueta + links
                links=acortador(links)
                list_links.append(links)
            

        return list_links



