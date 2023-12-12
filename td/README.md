# Le TD 1 s'appuie sur Jupyter Lab/Notebook. Pour y accéder, vous pouvez utiliser : 


- le [lien](https://mybinder.org/v2/gh/fbxyz/ENSG_L1_cartostat/HEAD) pour lancer un Notebook Binder. Ce dernier est temporaire et perdu si vous fermez votre navigateur. Pensez à enregistrer votre Notebook ipynb pour le recharger plus tard. Le premier lancement est parfois long et la machine virtuelle s'arrête en cas d'inactivité.

- Installer [Conda](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html) sur votre ordinateur (Linux, Windows, MacOS). Cloner ensuite le Git du cours. Les packages à installer sont disponibles dans le fichier requirements.txt (cf. section suivante)

- Vous pouvez aussi utiliser après inscription [Google Colaboratory](https://colab.research.google.com/), [Kaggle](https://www.kaggle.com/) ou [CoCalc](https://cocalc.com/features/jupyter-notebook). Ils peuvent directement importer le contenu du Git du cours.

Si vous installez un environnement conda sur votre ordinateur, je vous conseille d'utiliser Jupyter Lab plutôt que Jupyter Notebook.

# Comment cloner le repo Git du cours, créer un environnement Conda, installer les packages et lancer Jupyter Lab
Après avoir installé Git et Conda, lancez un terminal. Placez-vous dans le répertoire qui vous intéresse
```
Linux MacOS : cd mon_repertoire/sous_repertoire
Windows : cd mon_repertoire\sous_repertoire
```

Clone du repo Git. Le répertoire ENSG_L1_cartostat va être créé à la racine du répertoire où vous vous trouvez
```
git clone https://github.com/fbxyz/ENSG_L1_cartostat.git

cd ENSG_L1_cartostat
```

Création d'un nouvel environnement Conda "stat"
```
conda create -n stat
```

Et activaiton de ce nouvel environnement
```
conda activate stat
```

Mise à jour de Conda
```
conda update -n base -c defaults conda
```

Installation des packages python via le fichier requirements.txt 
``` 
conda install jupyterlab seaborn altair statsmodels scipy scikit-learn pandas

ou : 

conda install --yes --file requirements.txt
```

Jupyter lab n'est pas dans le fichier requirements.txt, pour l'installer : 
```
conda install jupyterlab
```

Lancez Jupyter Lab
```
jupyter lab
```


