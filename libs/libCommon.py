

def get_date_ccyymmdd(par_datetime):
    '''
    returns string ccyymmdd
    '''
    mm = par_datetime.month
    if mm < 10:
        mm = '0' + str(mm)
    dd = par_datetime.day
    if dd < 10:
        dd = '0' + str(dd)
    ccyymmdd = f'{par_datetime.year}{mm}{dd}'
    return ccyymmdd
