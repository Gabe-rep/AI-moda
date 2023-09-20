# AI-moda
 
L’intelligenza artificiale (AI) permette ai sistemi di capire il proprio ambiente, mettersi in relazione con quello che percepisce e risolvere problemi, e agire verso un obiettivo specifico.
AI-moda è un'intelligenza artificiale creato per fornire suggerimenti basati sui vestiti.
l'app riceve in input una foto e restitiusce un link con articoli simili alla quelli presenti sulla foto.

## Programmi Usati:
  * microsaoft Azure (vision visual)
  * visual studio

## Step Demo 
  * Analisi dell'imagine : file python imageAnalisi
    * ci collegiamo a Vision Visual
    * facciamo l'estrazione dei tags della foto con Dense Caption

  * Estrazione del prodotto : file python Product
    * salviamo i tags su un file txt
    * estriamo dal file il prodotto (prodotto + filtro, esempio yellow shirt)

  * Restitiure un link Zalando con prodotti similli: file python Response
    * ci colleggiamo a zalando
    * stampiamo prodotti simili
      
