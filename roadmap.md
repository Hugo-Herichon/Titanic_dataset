x🔹 Semaine 1 – Python & Manipulation de données

Objectif : Être à l’aise avec Python, Pandas, Numpy.

Réviser : boucles, fonctions, imports, gestion de fichiers.

Apprendre : pandas pour lire CSV, numpy pour manipuler des tableaux.

👉 Défis :

Charger un CSV (ex. Titanic dataset).

Compter le nombre de passagers par sexe.

Calculer la moyenne d’âge.

Tracer un histogramme des âges.

📌 Mini-projet : Faire un mini rapport sur le Titanic (3 graphiques + 3 stats).

🔹 Semaine 2 – Bases du Machine Learning

Objectif : Comprendre l’apprentissage supervisé.

Concepts : train/test split, features vs labels, sur-apprentissage.

Découvrir scikit-learn.

👉 Défis :

Créer un dataset jouet (make_classification) et entraîner un modèle de classification.

Visualiser la frontière de décision.

Évaluer avec accuracy_score.

📌 Mini-projet : Prédire si un passager du Titanic survit (classification binaire).

🔹 Semaine 3 – Projet 1 : Prédire le prix d’une maison 🏠

Objectif : Régression linéaire.

Dataset : Boston Housing (ou California Housing).

Notions : MSE, R², normalisation.

👉 Défis :

Visualiser la corrélation entre taille du logement et prix.

Créer une régression linéaire simple (1 variable).

Étendre à plusieurs variables (régression multiple).

📌 Projet : Construis un modèle qui prédit le prix d’une maison → compare les performances avec plusieurs modèles (LinearRegression, RandomForestRegressor).

🔹 Semaine 4 – Introduction au NLP

Objectif : Comprendre le traitement du texte.

Notions : tokenisation, stopwords, TF-IDF.

Outils : nltk, sklearn.feature_extraction.text.

👉 Défis :

Nettoyer une phrase ("Ceci est un TEST !!!") → tokens en minuscules, sans ponctuation.

Comparer deux phrases avec la similarité cosinus.

Transformer une liste de phrases en matrice TF-IDF.

📌 Mini-projet : Classer des SMS en spam ou non spam.

🔹 Semaine 5 – Projet 2 : Chatbot simple 💬

Objectif : Créer un bot FAQ avec NLP.

Dataset : FAQ maison ou SMS Spam.

Modèle : Naïve Bayes ou Logistic Regression.

👉 Défis :

Construire une fonction qui répond "Je n’ai pas compris" si la confiance est trop faible.

Ajouter une interface simple (CLI → tu écris, le bot répond).

📌 Projet : Ton premier chatbot qui répond à quelques questions (ex. "Bonjour", "Quels sont les horaires ?", "Merci").

🔹 Semaine 6 – Bases des systèmes de recommandation

Objectif : Comprendre les types de recommandation.

Filtrage collaboratif : basé sur utilisateurs similaires.

Content-based : basé sur caractéristiques des films.

👉 Défis :

Charger MovieLens 100k.

Construire une matrice user x movie.

Calculer similarité cosinus entre 2 utilisateurs.

📌 Mini-projet : Recommander 3 films à un utilisateur en fonction de ses notes.

🔹 Semaine 7 – Projet 3 : Recommandation type Netflix 🎬

Objectif : Construire un vrai système de reco.

Approche 1 : filtrage collaboratif (user-based).

Approche 2 : content-based (descriptions de films).

👉 Défis :

Comparer les deux approches.

Mesurer la précision avec RMSE (prédiction des notes).

Ajouter une fonction : "Si tu as aimé X, regarde Y".

📌 Projet : Un petit "Netflix maison" → tu choisis un film, le système en propose 5 similaires.

🔹 Semaine 8 – Consolidation & Améliorations

Objectif : Revoir et améliorer les projets.

Améliorer le modèle de prédiction de prix avec un Random Forest.

Améliorer ton chatbot avec TF-IDF + SVM.

Ajouter une interface web simple (Flask ou Streamlit) pour ton système de reco.

📌 Projet final :
Un portfolio IA avec 3 notebooks + 1 mini app Streamlit :

Prédiction de prix

Chatbot

Reco Netflix
