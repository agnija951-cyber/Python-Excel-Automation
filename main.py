import pandas as pd

print("Skriptas pradeda darba")
#Sukuriame paprastus duomenis
duomenys = {
    'Vardas' : ['Jonas', 'Asta', 'Mantas'],
    'Pardavimai' : [100, 250, 150]
}
# Paverčiame juos į lentelę 
df = pd.DataFrame(duomenys)

#Išsaugosime į Excel failą
df.to_excel("pirmas_rezultatas.xlsx",
index=False)

print("Pavyko! failas' pirmas_rezultatas.xlsx' sukurtas.")