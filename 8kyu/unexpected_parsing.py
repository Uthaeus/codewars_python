
def get_status(is_busy):
    status = ''
    if is_busy == True:
        status = 'busy'
    else:
        status = 'available'
    return status



print(get_status(False)["status"]) #, "available")