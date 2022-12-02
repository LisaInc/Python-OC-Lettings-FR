## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
  `which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(profiles_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from profiles_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1`
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

# Déploiement continue
Pipeline CI/CD avec CircleCI et Heroku

### Circle CI
Lien vers la pipeline Circle CI : [https://app.circleci.com/pipelines/github/LisaInc/Python-OC-Lettings-FR](https://app.circleci.com/pipelines/github/LisaInc/Python-OC-Lettings-FR)
Etapes du déploiement:
- Tests avec pytest
- Linting avec flake8
- Build d'une image docker
- Push de l'image sur docker hub
- Push du conteuneur sur heroku
### Docker
Lien vers docker hub : [https://hub.docker.com/repository/docker/lisainc/oc_lettings_site](https://hub.docker.com/repository/docker/lisainc/oc_lettings_site)
- Installation de docker : [https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/)
- Pull image : `sudo docker pull lisainc/oc_lettings_site:latest`
- Pour run l’image docker en local et déclarer le port à utiliser pour acceder à l’application :
  - `sudo docker run -d -p 8001:8000 lisainc/oc_lettings_site:latest` 
  -  Lien pour acceder au site : [http://localhost:8001/](http://localhost:8001/) 

### Heroku
Pour installer heroku, la documentation se trouve [ici](https://devcenter.heroku.com/articles/getting-started-with-python#set-up).
Après s'être connecté avec `heroku login`, il faut creer l'application avec `heroku create`.
Pour pousser l'application sur heroku en local :
- `heroku container:push -a lisainc-oc-lettings web`
- `heroku container:release -a lisainc-oc-lettings web`
Lien vers heroku : [https://dashboard.heroku.com/apps/lisainc-oc-lettings/](https://dashboard.heroku.com/apps/lisainc-oc-lettings/)
Lien vers l'application : [https://lisainc-oc-lettings.herokuapp.com/](https://lisainc-oc-lettings.herokuapp.com/)

### Sentry
Sentry permet de vérifier les erreurs que pourrait avoir l'application en production. 
Le dashboard est disponnible [ici](https://sentry.io/organizations/lisainc/projects/oc-lettings/?project=4504100506501120).
Pour tester son fonctionnement, utiliser l'url `/sentry-debug/`.