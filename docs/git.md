# Git

## Normes syntaxique

|Decription          |Syntaxe          |
|--------------------|-----------------|
|Contenu obligatoire |\[Exemple\]      |
|Contenu optionnel   | \[\<Exemple\>\] |

## Documentation

- [Documentation officielle](https://git-scm.com/docs)
- [Documentation Bitbucket](https://www.atlassian.com/git/tutorials)
- [Documentation GitHub](https://guides.github.com/introduction/git-handbook/#basic-git)

## Configuration

- [git config](#git-config)

### git config

Configurer Git.

|Commande                                     |Utilité                                               |
|---------------------------------------------|------------------------------------------------------|
|``git config --global user.name "[nom]"``    |Nom utilisé lors des actions sur les dépôts           |
|``git config --global user.email "[email]"`` |Adresse mail utilisée lors des actions sur les dépôts |

---

## Utiliser ou créer un projet

- [git init](#git-init)
- [git clone](#git-clone)

### git init

Initialiser un répertoire pour un nouveau projet ou un projet existant.

``git init``

---

### git clone

Copier un dépôt distant en local.

``git clone [url]``

---

## Bases des instantanés

- [git add](#git-add)
- [git status](#git-status)
- [git commit](#git-commit)

### git add

Ajouter le contenu des fichiers dans l'index.

|Commande             |Utilité                                   |
|---------------------|------------------------------------------|
|``git add "[file]"`` |Ajoute le contenu d'un fichier spécifique |
|``git add .``        |Ajoute le contenu de tout les fichiers    |

---

### git status

Afficher le statut de la branche active (fichiers modifiés, etc.).

|Commande                    |Utilité                               |
|----------------------------|--------------------------------------|
|``git status -s``           |Affiche le statut en format court     |
|``git status --show-stash`` |Affiche le nombre de d'entrée cachées |

---

### git commit

Faire un commit du contenu de l'index.

|Commande                      |Utilité                                            |
|------------------------------|---------------------------------------------------|
|``git commit -m "[message]"`` |Lance un commit avec le message renseigné          |
|``git commit --amend``        |Ajoute les modification au dernier commit effectué |

---

## Branches et fusions

- [git push](#git-push)
- [git pull](#git-pull)
- [git branch](#git-branch)
- [git checkout](#git-checkout)
- [git stash](#git-stash)

### git push

Pousser les commit locaux sur le dépôt distant.

---

### git pull

---

### git branch

---

### git checkout

---

### git stash
