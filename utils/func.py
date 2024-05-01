import os
import patoolib


async def create_rar():
    DIR = "utils/sessions"
    prev_cwd = os.getcwd()
    os.chdir(DIR)
    files = os.listdir('.')
    patoolib.create_archive('../' + 'sessions' + '.rar', files)
    os.chdir(prev_cwd)


async def delete_rar():
    os.remove('utils/sessions.rar')