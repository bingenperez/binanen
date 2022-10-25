import requests 
import pandas as pd
import json
class binanen:
    def __init__(self,token):
        #self.apy_key=token

        url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/inventarioestaciones/todasestaciones/"

        querystring = {"api_key":token}

        headers = {
            'cache-control': "no-cache"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        ur_uso=json.loads(response.text)["datos"]



        url = "https://opendata.aemet.es/opendata/sh/4adf4e6f"

        querystring = {"api_key":"eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJiLnBlcmV6LmVyYXNvQG1hcmlzdGFzYmlsYmFvLmNvbSIsImp0aSI6IjUzY2IyNjJjLWIzNTktNGVkMi1hZDU4LTkyM2EzNzFiMDAwNSIsImlzcyI6IkFFTUVUIiwiaWF0IjoxNjY2MTAwMjIzLCJ1c2VySWQiOiI1M2NiMjYyYy1iMzU5LTRlZDItYWQ1OC05MjNhMzcxYjAwMDUiLCJyb2xlIjoiIn0.IoM_sSXns3A0yrv9C7YgfAMjtncQNucOohK-g1FNDZI"}

        headers = {
            'cache-control': "no-cache"
            }

        response = requests.request("GET", ur_uso, headers=headers, params=querystring)

        #print(response.text)
        datos=json.loads(response.text)
        df_datos=pd.DataFrame(datos,columns=['latitud', 'provincia',"altitud","indicativo","nombre","indsinop","longitud"])
        self.df_datos=df_datos

    def coordenadas(self):
        df_datos=self.df_datos
        print(df_datos["provincia"].unique())
        elige_prov=input("Elige la provincia: ")
        d=0
        while elige_prov not in df_datos.provincia.unique():
            d=d+1
            if d>1:
                elige_prov=input("¿Ya empezamos?, no me jodas eee, porfavor indique el nombre de nuevo:")
                print(df_datos.provincia.unique())
            else:
                elige_prov=input("Pon bien el nombre porfavor: ")
                print(df_datos.provincia.unique())
        
        df_prov=df_datos[df_datos["provincia"]==elige_prov]
        print(df_prov.nombre.unique())
        elige=input("Elige el nombre: ")
        a=0
        while elige not in df_prov.nombre.unique():
            a=a+1
            if a>1 :
                elige=input("¿Es usted tonto?, porfavor indique el nombre de nuevo:")
                print(df_prov.nombre.unique())
            else:
                elige=input("Pon bien el nombre porfavor: ")
                print(df_prov.nombre.unique())
        
        alt=df_prov[df_prov["nombre"]==elige]["altitud"].values[0]
        lat=df_prov[df_prov["nombre"]==elige]["latitud"].values[0]
        lon=df_prov[df_prov["nombre"]==elige]["longitud"].values[0]
        print("Su latitud es: ",lat)
        print("Su longitud es: ",lon )
        return lat,lon

if __name__ == "__main__":
    apykey="eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJiLnBlcmV6LmVyYXNvQG1hcmlzdGFzYmlsYmFvLmNvbSIsImp0aSI6IjUzY2IyNjJjLWIzNTktNGVkMi1hZDU4LTkyM2EzNzFiMDAwNSIsImlzcyI6IkFFTUVUIiwiaWF0IjoxNjY2MTAwMjIzLCJ1c2VySWQiOiI1M2NiMjYyYy1iMzU5LTRlZDItYWQ1OC05MjNhMzcxYjAwMDUiLCJyb2xlIjoiIn0.IoM_sSXns3A0yrv9C7YgfAMjtncQNucOohK-g1FNDZI"
    ale=binanen(apykey)
    ale.coordenadas()