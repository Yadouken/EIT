

### Partie IV)
cd src/PartieIV
python NERtoOccurences.py outLongStan.txt occurences.txt

### Partie V)
cd src/PartieV
Liste complète des commandes à lancer  pour la partie V) évaluation de l'outil LIMA et de l'outil de Stanford:

python LimaToStanNER.py outLongLima.txt LimaStan.txt
		Conversion du fichier Lima en Stanford.
python StanToUniv.py LimaStan.txt LimaUniv.txt.
		Conversion du fichier en universel.
python StanToUniv.py outLongStan.txt StanUniv.txt
		Conversion du fichier Stanford en universel.
python TagsToLabelsLima.py formal-tst.NE.key.04oct95_small.ne RefLima.txt
		Génère le fichier référence Lima.
python TagsToLabelsStan.py formal-tst.NE.key.04oct95_small.ne RefStan.txt
		Génère le fichier référence Stanford.
python evaluate.py LimaUniv.txt RefLima.txt
		Evaluation du Lima.
python evaluate.py StanUniv.txt RefStan.txt
		Evaluation du Stanford.