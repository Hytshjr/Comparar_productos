from columnas_filas import readxslx
from scrap import Links_download, Get_bloque, Get_title
import pandas as pd

def filter(title,price,list_links,producto,list_names,list_price,list_url):
    try:
        for i in range(len(title)):

            words = producto.split()
            verify = 0 
            for ver in words:

                if ver.lower() in title[i].lower():
                    verify +=1

                if verify == len(words):
                    list_names.append(title[i])
                    list_price.append(price[i])
                    list_url.append(list_links[i])

        return list_names,list_price,list_url
    
    except:
        print("ERROR")

def run():

    list_names = []
    list_price = []
    list_url = []

    url = '/home/hytsh/Documents/practice/scrap_product/link_brands_test.xlsx'
    producto = input("Ingrese el producto que desea buscar: ")

    links = readxslx(url,0)

    list_bloque = readxslx(url,1)
    list_bloque_class = readxslx(url,2)
    list_bloque_class_id = readxslx(url,3)

    list_title_etiqueta = readxslx(url,4)
    list_title_etiqueta_class =readxslx(url,5)
    list_title_etiqueta_class_id = readxslx(url,6)

    list_price_etiqueta = readxslx(url,7)
    list_price_etiqueta_class = readxslx(url,8)
    list_price_etiqueta_class_id = readxslx(url,9)

    list_links_home_page = readxslx(url,10)



    for indice in range(len(links)):

        try:
            soup = Links_download(links[indice],producto)
            soup = soup.parse()
            
            bloque = Get_bloque(soup,list_bloque[indice],list_bloque_class[indice],list_bloque_class_id[indice])
            bloque = bloque.get_body()
            
            title = Get_title(bloque,list_title_etiqueta[indice],list_title_etiqueta_class[indice],list_title_etiqueta_class_id[indice])
            title = title.has_data_bloque()

            price = Get_title(bloque,list_price_etiqueta[indice],list_price_etiqueta_class[indice],list_price_etiqueta_class_id[indice])
            price = price.has_data_bloque()


            list_links = Get_title(bloque_div=bloque,title_etiqueta=list_links_home_page[indice],title_etiqueta_class=0,title_etiqueta_class_id=0)
            list_links = list_links.has_link()


            list_names,list_price,list_url = filter(title,price,list_links,producto,list_names,list_price,list_url)
        
        except Exception as e:
            
            print('Erro en el llamado de alguna clase', e)

    valores = {'Precio':[], 'Links':[]}
    valores ['Precio'] = list_price
    valores ['Links'] = list_url

    cuadro = pd.DataFrame(data=valores , index=list_names)

    print(cuadro)

if __name__ == '__main__':
    run()