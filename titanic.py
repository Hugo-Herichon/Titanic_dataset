import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Titanic_data:
    def __init__(self, file: str):
        self.df = pd.read_csv(file)
        self.men = (self.df['Sex'] == 'male').sum()
        self.women = (self.df['Sex'] == 'female').sum()
        self.alive = (self.df['Survived'] == 1).sum()
        self.dead = (self.df['Survived'] == 0).sum()
        self.stat_men = (self.df['Sex'] == 'male').sum() / len(self.df) * 100
        self.man_age_avg = self.df[self.df['Sex'] == 'male']['Age'].mean(skipna=True)
        self.kids_surv = ((((self.df['Survived'] == 1) & (self.df['Age'] <= 17)).sum()) / (self.df['Age'] <= 17).sum()) * 100
        self.grown_surv = ((((self.df['Survived'] == 1) & (self.df['Age'] >= 18) & (self.df['Age']<= 35)).sum()) / ((self.df['Age'] >= 18) & (self.df['Age']<= 35)).sum()) * 100
        self.par_surv = ((self.df['Age'] >= 36) & (self.df['Age']<= 50)).sum()
        self.old_surv = ((self.df['Age'] >= 51) & (self.df['Age']<= 65)).sum()
        self.retired_surv = ((self.df['Age'] >= 66) & (self.df['Age'] <= 80)).sum()
                
    def bar(self):
        plt.style_use('_mpl-gallery')
        x= 0.5 + np.arange(5)
        pass
        
        
    def show_stats(self):
        print(self.df.columns)
        print(f"{self.men} hommes dans le titanic")
        print(f"{self.women} femmes dans le titanic")
        print(f"{self.stat_men:.2f} % d'hommes sur le bateau")
        print(f"{self.dead} morts pour {self.alive} survivants")
        print(f"La moyenne  d'age des hommes était de {self.man_age_avg:.2f} ans")
        print(self.df.loc[self.df['Age'].idxmax(), 'Name'])
        print(f"{self.kids_surv:.2f} % d'enfants on survécus")
        print(f"{self.grown_surv:.2f} % de personnes entre 18 et 35 ans ont survécu")

        
titanic = Titanic_data('titanic.csv')
titanic.show_stats()
