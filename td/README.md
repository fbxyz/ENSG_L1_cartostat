# Le TD 1 s'appuie sur Jupyter Lab/Notebook. Pour y accéder, vous pouvez utiliser : 


- le [lien](https://mybinder.org/v2/gh/fbxyz/ENSG_L1_cartostat/HEAD) pour lancer un Notebook Binder. Ce dernier est temporaire et perdu si vous fermez votre navigateur. Pensez à enregistrer votre Notebook ipynb pour le recharger plus tard. Le premier lancement est parfois long et la machine virtuelle s'arrête en cas d'inactivité.

- Installer [Conda](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html) sur votre ordinateur (Linux, Windows, MacOS). Cloner ensuite le Git du cours. Les packages à installer sont disponibles dans le fichier requirements.txt (cf. section suivante)

- Vous pouvez aussi utiliser après inscription [Google Colaboratory](https://colab.research.google.com/), [Kaggle](https://www.kaggle.com/) ou [CoCalc](https://cocalc.com/features/jupyter-notebook). Ils peuvent directement importer le contenu du Git du cours.

Si vous installez un environnement conda sur votre ordinateur, je vous conseille d'utiliser Jupyter Lab plutôt que Jupyter Notebook.


# Comment cloner le repo Git du cours, créer un environnement Conda, installer les packages et lancer Jupyter Lab
 lancez un terminal. Placez-vous dans le répertoire qui vous intéresse
```
Linux MacOS : cd mon_repertoire/sous_repertoire
Windows : cd mon_repertoire\sous_repertoire
```

Clone du repo Git. Le répertoire ENSG_L1_cartostat va être créé à la racine du répertoire où vous vous trouvez
```
git clone https://github.com/fbxyz/ENSG_L1_cartostat.git

cd ENSG_L1_cartostat
```

## Installation et utilisation de Conda et JupyterLab

### Étape 1 : Vérifier si Anaconda est installé

**Windows** :
1. Chercher "Anaconda Prompt" dans le menu démarrer
2. **Si "Anaconda Prompt" apparaît** : Anaconda est installé → passer à l'**Étape 2**
3. **Si "Anaconda Prompt" n'existe pas** : Installer Anaconda (voir ci-dessous)

**Installer Anaconda (Windows)** :
1. Télécharger Anaconda : https://repo.anaconda.com/archive/Anaconda3-2025.06-0-Windows-x86_64.exe
2. Lancer l'installateur et suivre les instructions
3. Une fois l'installation terminée, chercher "Anaconda Prompt" dans le menu démarrer pour vérifier que l'installation a réussi


### Étape 2 : Ouvrir Anaconda Prompt

**Windows** :
- Chercher "Anaconda Prompt" dans le menu démarrer et l'ouvrir
- **Important** : Toutes les commandes suivantes doivent être exécutées dans **Anaconda Prompt** (pas PowerShell ou CMD)


### Étape 3 : Créer un environnement conda

Dans **Anaconda Prompt**, créer un environnement isolé pour ce cours :

```bash
conda create -n stat python=3.11
```

Répondre `y` (yes) quand demandé.

Activer l'environnement :

```bash
conda activate stat
```

Vous devriez voir `(stat)` apparaître au début de la ligne de commande.


### Étape 4 : Installer les packages nécessaires

Dans **Anaconda Prompt** avec l'environnement activé, installer les packages :

```bash
conda install -c conda-forge jupyterlab geopandas pandas matplotlib seaborn mapclassify numpy altair statsmodels scipy scikit-learn
```

Répondre `y` (yes) quand demandé. L'installation peut prendre quelques minutes.

> **Note** : Conda gère automatiquement les dépendances système (GDAL, GEOS, PROJ) nécessaires pour GeoPandas, ce qui évite les problèmes d'installation courants sous Windows.

### Étape 5 : Lancement de JupyterLab

Dans **Anaconda Prompt** avec l'environnement activé, naviguer vers le dossier du cours :

**Windows** :
```bash
cd C:\chemin\vers\ENSG_L1_cartostat
```

Exemple : `cd C:\Users\VotreNom\Documents\ENSG_L1_cartostat`

Lancer JupyterLab :
```bash
jupyter lab
```

Le navigateur s'ouvre automatiquement avec l'interface JupyterLab.

### Utilisation

Exécution des cellules :
- `Shift + Entrée` : exécuter et passer à la cellule suivante
- `Ctrl + Entrée` : exécuter et rester sur la cellule
- Bouton Play dans la barre d'outils

Conseils :
- Exécuter les cellules dans l'ordre
- Redémarrer le kernel en cas de problème : Menu `Kernel` → `Restart Kernel...`
- Sauvegarder régulièrement : `Ctrl + S` ou `Cmd + S`




