'''
depends on lib libLogger
'''
import os
import sys
import logging
import glob
import json

logger = logging.getLogger('libConfig')


def folder_exists(folder):
    '''
    check if folder exists
    '''
    present = False
    if os.path.isdir(folder):
        logging.debug(f'folder present: {folder}')
        present = True
    else:
        logging.debug(f'folder not present: {folder}')
    return present


def folder_create(folder):
    res = False
    try:
        if not os.path.exists(folder):
            os.makefolders(folder)
            logger.info(f'folder created: {folder}')
        else:
            logger.info(f'folder created: {folder}')
        res = True
    except:
        logger.critical(
            f'folder {folder} NOT created..?? exception {sys.exc_info()[0]}')
    return res


def folder_listfiles(folder, mask='*'):
    '''
    returns count and filesnames from folder
    filter mask
    '''
    count = 0
    files = None
    if os.path.exists(folder):
        folder_mask = os.path.join(folder, mask)
        files = glob.glob(folder_mask)
        count = len(files)
    else:
        logger.info(f'folder does not exists: {folder}')
    return count, files


def file_exists(file, notexists_is_error=False):
    '''
    check if file exists
    '''
    exists = False
    if os.path.isfile(file):
        logging.debug(f'file present: {file}')
        exists = True
    else:
        if notexists_is_error:
            logging.error(f'file NOT present: {file}')
        else:
            logging.info(f'file NOT present: {file}')
    return exists


def file_getcontent(file):
    '''
    get all the lines of file file_fullname
    argument must be an existing filenaam including full path
    return boolean (result), list
    '''
    lines = None
    result = False
    count = 0
    try:
        if file_exists(file):
            with open(file) as openfile:
                lines = openfile.readlines()
            result = True
    except FileNotFoundError as fnf_error:
        lines = None
        logger.error(f'FileNotFoundError {fnf_error}')
    if result:
        if lines == None:
            logger.info(f'file {file} contents is None')
        else:
            count = len(lines)
            logger.info(f'file {file} contains {count} lines.')
    return result, lines, count


def file_json_getcontent(file):
    with open(file, "r") as read_file:
        json_data = json.load(read_file)
    return json_data
