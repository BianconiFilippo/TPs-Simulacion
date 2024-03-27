<h1>Repositorio para los TPS de simulacion</h1>

<p>
El TP1 es una primera version de la ruleta, si van a aportar modificaciones que sea sobre RuletaVC que es la version completa del TP1
</p>


<h2> Como correr el codigo</h2>
<p>Para correr el codigo, tenemos que hacer 2 cosas</p>
<ol>
    <li>Crear el entorno virtual</li>
    <li>Correr el tp que querramos </li>
</ol>
<h3>Crear entorno virtual</h3>
<p>Para esto, tenemos que tener el python preinstalado</p>
<ol>
    <li>
        <p>Abrir la terminal en la carpeta del proyecto (.../TPs-Simulacion)</p>
    </li>
    <li>
        <p>Dentro de la carpeta, correr el comando para crear el entorno virtual</p>
        <code>python -m venv .venv</code>
        <p style="color:gray;">(Puede pedir que lo corramos con python3 en lugar de python)</p>
    </li>
    <li>
        <p>Abrir el entorno creado</p>
        <br>
        <p style="color:red">Para linux/MACos</p>
        <code>source tutorial-env/bin/activate</code>
        <br>
        <p style="color:red">Para Windows</p>
        <code>tutorial-env\Scripts\activate</code>
    </li>
    <li>
        <p>Instalar paquetes necesarios</p>
        <code>pip install -r requirements.txt</code>
    </li>
    
</ol>
<br>
<br>
<h3>Correr tp</h3>
<p>Para correr el tp, debemos usar el comando siguiente</p>
<code>python (nombre_carpeta_tp)/main.py</code>
<p>(Puede pedir que lo corramos en python3 en lugar de python)</p>
