--- INSTRUCCIONS D'ÚS DEL PROGRAMA ---
Aquest programa és un programa d'encriptament i desencriptament de missatges creat per Biel Constenla, Sergi Pons i Hector
Martínez, estudiants de segon de Batxillerat tecnològic, per a un Treball de Recerca sobre criptografia.

Requisits per a executar:
- Python 2.7 o superior.
- Llibreria MIMEMultipart (per a instal·lar, introduir a la consola de comandaments "pip install MIMEMultipart")
- Llibreria PySimpleGUI (per a instal·lar, introduir a la consola de comandaments "pip install PySimpleGUI")

Instruccions:
- Botó d'encriptament: Introduir al primer quadre de text la frase i en el segon la clau. Després prémer el botó.
- Botó de desencriptament: Introduir al primer quadre de text la frase i prémer el botó.
- Botó d'enviament: Seguir instruccions del primer botó, però s'ha de prémer el botó d'encriptar i enviar. En la següent
		    pantalla, introduir una adreça de correu vàlida per a l'enviament* i una altra a la que enviar el 
		    missatge.


Instruccions de credencials:
1. S'ha de moure la carpeta del programa (TDR) a l'escriptori.
2. Entrar a la carpeta "credencials", dins de la carpeta "TDR".
3. Obrir el programa "creds.py". Et redirigirà a una pàgina de Google.
4. Iniciar sessió amb un compte de correu. Et demanarà que acceptis uns permisos determinats.**

Alguns errors a tenir en compte:
1. El programa no conté missatges d'error excepte a l'apartat d'enviament, per tant, si quan es vol encriptar
   no s'introdueix la clau, el programa es tancarà, mostrant l'error a la consola de comandaments.
2. El programa encripta nombres i símbols, però no els desencripta. Es desencripten com si fossin lletres corrents.


*Adreça de correu vàlida: Credencials validades per a aquella adreça. Revisar instruccions de credencials
**NOTA: Degut a problemes de Google Cloud Console, el programa no es troba en fase pública i, per tant, només usuaris
seleccionats pel desenvolupador poden accedir a les credencials. Per a poder accedir, s'haurà de demanar ser inclós dins
de la llista als desenvolupadors.