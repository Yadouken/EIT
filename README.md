# EIT
### Partie II)
cd src/PartieII

python RefToText.py wsj_0010_sample.pos.ref REF.txt

	Creation de référence mot_etiquette
	
python LimaToText.py ExLima.conll LimaTxt.txt

	Lima Conversion Lima en mot_etiquette
	
python evaluate.py LimaTxt.txt REF.txt

	Evaluation de Lima PTB
	
python PTBToUniversal.py Dico.txt REF.txt REFUniv.txt

	Conversion de la référence en universelle
	
python PTBToUniversal.py Dico.txt LimaTxt.txt LimaTxtUniv.txt

	Conversion du texte Lima en universelle
	
python evaluate.py LimaTxtUniv.txt REFUniv.txt

	Evaluation de Lima avec les etiquettes universelles

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
		
python TagsToLabels.py formal-tst.NE.key.04oct95_small.ne REF.txt

		Génère le fichier référence.
		
python evaluate.py LimaUniv.txt REF.txt

		Evaluation du Lima.
		
python evaluate.py StanUniv.txt REF.txt

		Evaluation du Stanford.
