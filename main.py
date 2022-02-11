from typing import Text
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

from getPrecioLuz import *
from kivymd.uix.list import TwoLineAvatarListItem,ImageLeftWidget
from kivymd.uix.dialog import MDDialog

Builder.load_file("main.kv")


class Prueba(MDScreen):
    pass

class MainApp(MDApp):
    def build(self):
        # Establecemos el tema
        self.theme_cls.primary_palette = "DeepPurple"
        return Prueba()

    #Mostrar un icono rojo,verde o amarillo segun sea el valor en lugar de la fuente del texto
    def on_start(self):
        horas = getHoras()
        precio = getPrecio()
        for i in range(24):
            if float(precio[i]) < precioHorario()[0]:#Horario valle
                imagen="icon_green.png"
            elif float(precio[i]) > precioHorario()[0] and float(precio[i]) < precioHorario()[1]:#Horario Llano
                imagen="icon_yellow.png"
            else:
                imagen="icon_red.png"#Horario punta
            wid = TwoLineAvatarListItem(text= precio[i] + ' €', secondary_text= horas[i],theme_text_color="Custom",text_color=(0,0,0,1))
            wid.add_widget(ImageLeftWidget(source=imagen))
            self.root.ids.contenedor.add_widget(wid
                
                )
    def muestra_info(self):
        dialogo = MDDialog(title= "Informacion", text="""Esta App extrae los datos del precio de la electricidad de la WEB https://tarifaluzhora.es/""")
        dialogo.open()

if __name__ == '__main__':
    
    MainApp().run()
