# Projet 7 du parcours python d'OC : AlgoInvestAndTrade

Ce programme est un ensemble d'algorithmes réalisés dans le cadre d'un projet d'OC

##  Téléchargement et création d'un environnement virtuel

Pour ce programme, vous aurez besoin de Python 3 (réalisé sur Python 3.9.6, car Numpy n'est pas encore disponible sur 3.10, ou vient alors vient tout juste d'être compatible).

Ouvrez un terminal et naviguez dans le dossier dans lequel vous voulez télécharger AlgoInvest. Exécutez ensuite les commandes suivantes : 

* Depuis le dépôt, téléchargez les fichiers et clonez le dossier.
    ```
    $ git clone https://github.com/Mildophin/P7
    $ cd P7
    ```
* Créez un environnement python appelé "env".
    ```
    $ python -m venv env
    ```
* Activez l'environnement.
    ```
    $ source/env/bin/activate #MacOS & linux
    $ source/env/Scripts/activate # Windows
    ```
* Installer les packages a partir de **requirements.txt**.
    ```
    $ pip install -r requirements.txt
    ```

## Comment utiliser le programme

* Une fois que vous avez créé l'environnement et installer les packages du fichier requirements.txt, vous pouvez exécuter le script de cette façon :
    ```
    $ python scripts.py -h
    ```
* Vous avez 1 argument positionnel que vous devez saisir. Choisissez entre '**bruteforce**' ou '**optimized**' : 
    ```
    $ python scripts.py optimized
    ```

Vous avez la possibilité d'ajouter des arguments facultatifs :

* Si vous voulez saisir un fichier, vous pouvez le faire avec un chemin absolu ou relatif de cette façon :
    ```
    $ python scripts.py -f databases/dataset.csv optimized
    ```
* Si vous voulez changer le budget d'un portefeuille, vous pouvez le faire avec l'argument optionnel suivant :
    ```
    $ python scripts.py -f databases/dataset.csv -b 500 optimized
    ```
