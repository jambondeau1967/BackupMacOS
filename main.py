import os
import logging
from datetime import datetime
from libs.libLogger import set_logger
from libs.libCommon import get_date_ccyymmdd
from libs.libFolderAndFiles import *


RSYNC_EXCLUDE = '--exclude-from=''exclude.txt'''
DATETIME_START = datetime.now()
CCYYMMDD = get_date_ccyymmdd(DATETIME_START)

set_logger(dir_logging='logs', filename_datepart=f'{CCYYMMDD}')

logging.info('-+=+-+=+- start -+=+-+=+-')


logging.info('* read config')


configdata = file_json_getcontent("./appconfig.json")
ACCOUNT = configdata["accountname"]
logging.info(f'account: {ACCOUNT}')
BACKUPDESTINATIONS = configdata["backup_destinations"]
RSYNC = configdata["rsync"]
RSYNC_EXCLUDE = RSYNC["excludelist"]


logging.info(f'* section RSYNC - excludelist = {RSYNC_EXCLUDE}')
for bd in BACKUPDESTINATIONS:
    for rf in RSYNC["folders"]:
        logging.info(f'rsyn folder {rf} to host {bd["hostname"]}')
        logging.debug(
            f'folder backup destination {bd["folderrootdestination"]}')

        part1 = f'rsync -avzP {RSYNC_EXCLUDE} --update'
        host_account = f'{ACCOUNT}@{bd["hostname"]}'
        part2 = bd["folderrootdestination"]

        command = f'{part1} ~/{rf}/ {host_account}:{part2}/{rf}/'
        logging.info(f'command = {command}')
        os.system(command)

logging.info('-+=+-+=+- end -+=+-+=+-')
