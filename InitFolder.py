# import fnmatch
import os
import os.path
# import re
import sys
import json
# import shutil


if __name__ == '__main__':
    with open('settings.json', encoding="utf8") as settigs_file:
        settings = json.load(settigs_file)
        first_path = settings['rules']['firstPath']    # 'DocFlow/Правила конвертации DF2ERPBF/'
        second_path = settings['rules']['secondPath']  # 'ERP BF/Правила конвертации ERPBF2DF/'
        first_zip = settings['rules']['firstZip']      # 'Правила обмена DF2ERPBF.zip'
        second_zip = settings['rules']['secondZip']    # 'Правила обмена ERPBF2DF.zip'

    with open('.gitignore', 'w', encoding="utf8") as gitignore_file:
        gitignore_file.write(
            "*.zip\n"
            "settings.json\n"
            "tests\n"
            "tests/*\n"
            "ServiceData\n"
            "ServiceData/*"
        )
        
    # Строим полные пути от папки запуска
    start_path = os.path.dirname(sys.argv[0])
    os.makedirs(os.path.join(start_path, first_path))
    os.makedirs(os.path.join(start_path, second_path))
    os.makedirs(os.path.join(start_path, "ServiceData"))
    os.makedirs(os.path.join(start_path, "Tests"))

