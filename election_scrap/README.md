# Scrapping project: Results of particular district in Czech Republic (Parlament 2017)

Election scrap project provides a look into election results of each municipality in desired district. Results are total number of votes per each political party.
Main tool used for the task above was Python Beautiful Soup library. Votes of each municipality are saved into .csv files and then utilized to visually more convenient shape
by using Pandas and Matplotlib libraries

[web source](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)

At this page, you first have to choose the district by the X key in the column Výber obce (on the right). So for when you choose i.e. district Příbram you then have to choose the municipality. This time you choose by the number of the municipality (column číslo on the left). So, i.e. Dobříš will have the number 540111.
