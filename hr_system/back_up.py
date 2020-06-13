import sys
import os

import json
import database_data
import time


def backup(args):
    if len(sys.argv) > 1 and sys.argv[1] == 'backup':

        if 'BACKUP' not in os.listdir(os.curdir):
            os.mkdir('BACKUP')

        date = time.strftime('%Y_%m_%d_%H_%M_%S')
        filename = 'BACKUP\\employee' + str(date) + '.json'

        with open(filename, 'w') as f:
            json.dump(database_data.database, f)