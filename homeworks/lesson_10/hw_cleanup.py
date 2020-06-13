# funkce bere argument cestu do slozky.
# v teto slozce najde soubory ruznych koncovek(txt,png...) a roztridi je do slozek, ktere pripadne vytvori
import os

#-------------------MAIN FUNCTION ------------------------------
def clean(path):
    paths = []
    try:
        for file in os.listdir(path):
            if os.path.isfile(path + '\\' + file):
                paths.append(path + '\\' + file)
    except:
        print('Inserted path does not exist !')
        quit()

    folds = create_folders()
    moved_files = move(paths, folds)
    print_result(moved_files)


def create_folders():
    folders = ['Images', 'Docs', 'Tables', 'Presentations']
    dont_move = {'Images': 0, 'Docs': 0, 'Tables': 0, 'Presentations': 0}

    for folder in folders:
        try:
            os.mkdir(os.getcwd() + '\\' + folder)
        except:
            print('Folder', folder, 'already exists.')
            choice = input('Do you want to move handled files into it ? y/n')

            while True:
                if choice == 'y':
                    break
                elif choice == 'n':
                    dont_move[folder] = 1
                    break
    return dont_move


def move(paths, dont_move):
    images = 0
    tables = 0
    docs = 0
    pres = 0

    while paths:
        file = paths.pop(0)

        if os.path.splitext(file)[1] in ['.doc', '.docx', '.odt', '.txt', '.pdf'] and dont_move['Docs'] == 0:
            os.rename(file, os.getcwd() + '\\' + 'Docs' + '\\' + os.path.basename(file))
            docs += 1
        elif os.path.splitext(file)[1] in ['.png', '.jpg', '.jpeg', '.tiff', '.gif'] and dont_move['Images'] == 0:
            os.rename(file, os.getcwd() + '\\' + 'Images' + '\\' + os.path.basename(file))
            images += 1
        elif os.path.splitext(file)[1] in ['.xls', '.xlsx'] and dont_move['Tables'] == 0:
            os.rename(file, os.getcwd() + '\\' + 'Tables' + '\\' + os.path.basename(file))
            tables += 1
        elif os.path.splitext(file)[1] in ['.ppt', '.pptx'] and dont_move['Presentations'] == 0:
            os.rename(file, os.getcwd() + '\\' + 'Presentations' + '\\' + os.path.basename(file))
            pres += 1

    return images, tables, docs, pres
        # print(os.path.splitext(file))


def print_result(moved_files):
    print('MOVED')
    print(21*'=')
    folders = ['Images', 'Tables', 'Docs', 'Presentations']

    for count, folder in zip(moved_files, folders):
        print('{:20s}{:>}'.format(folder, count))


clean('TestDir')