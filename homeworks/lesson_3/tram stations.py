tram_stations = {
'No.1' : ['Reckovice', 'Semilasso', 'Husitska', 'Jungmannova', 'Kartouzska', 'Sumavska', 'Hrnicrska', 'Pionyrska', 'Antoninska', 'Moravske nam.', 'Malinovske nam', 'Hlavni nadr.', 'Nove sady', 'Hybesova', 'Vaclavska', 'Mendlovo nam.', 'Vystaviste main', 'Vystaviste G2', 'Lipova', 'Pisarky'],
'No.2' : ['Zidenice', 'Kuldova', 'Vojenska nemocnice', 'Tkalcovska', 'Kornerova', 'Malinovske nam.', 'Hlavni nadr.', 'Nove Sady', 'Hybesova', 'Vaclavska', 'Mendlovo nam.', 'Porici', 'Nemocnice UM', 'Celni', 'Hluboka', 'Ustredni hrbitov'],
'No.3' : ['Husovice','Nam. republiky','Vozovna Husovice','Mostecka','Travnickova', 'Tkalcovska', 'Kornerova', 'Malinovske nam.', 'Hlavni nadr.', 'Nove sady', 'Silingrovo nam.', 'Ceska', 'Komenskeho nam.', 'Obilni trh', 'Uvoz']
}

common = set(tram_stations['No.1']) & set(tram_stations['No.2']) & set(tram_stations['No.3'])
print(common)