# Vandewalle_tp1
Exercice 1 : 
Installation de Docker Desktop pour Windows :
    - Installation de wls + sous systeme Linux



Exercice 5 :
    - Mon DockerFile provoque l'erreur python: can't open file '/app/app.py': [Errno 2] No such file or directory". En ajoutant la ligne "COPY . ." sur StackOverflow, cela a pu copier mon app dans mon dockerFile. En réalisant la modification, le conteneur a pu se lancer.



# TP 2

Initialement, l'image pèse 1.88 GB. 

- Etape 1 : Optimisation du poid de l'image -> Dans le DockerFile, nous importons les nodes modules ce qui est inutile sachant qu'ils seront installé dans le npm install. J'ai également supprimer les mises à jours du 'apt update& install'.

Après modification l'image pèse 300 MB.

Etape 2 : Dans le fichier server.js, nous avons un bloc de code (/big) qui n'est pas optimisé. Il est synchrone, c'est à dire que le server attends le traitement du fichier, puis passe au suivant. En asynchronisant, on peut réduire considérablement le temps de traitement et encore plus si on utilise des Threads.

Après modification le build passe à 3,2s.

Etape 3 : Bonne pratique/Securité -> Dans le Dockerfile, nous avons "ENV ENV=development" ce qui n'est pas une bonne pratique (SonarCloud, docker:S4507) car on augmente la surface d'attaque.J'ai donc remplacé cela par un code compliant : ENV APP_DEBUG=false
ENV ENV=production
Toujours dans le dockerfile, le USER en root est une faille de sécurité. En utilisant node, un profil avec un accès limité, cela va limiter le risque. 
Limiter l'exposition des ports à un seul, ici 3000.
Dans le server.js, utilisation de app.disable('x-powered-by'); pour que l'information.

Dans server.js, ligne 2-3, ajout de 'node:js' pour spécifier son usage. 

Suppression de "mongodb":"^6.19.0" dans package.json. Cette dépendance est inutile.