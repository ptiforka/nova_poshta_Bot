from consts import TTN_LEN, PHONE_LEN


def unpack(message):
    splitted_message = message.text.split(' ')
    if len(splitted_message) == 2:
        return splitted_message
    else:
        return [*splitted_message, None]


def ttn_validation(ttn):
    return len(ttn) == TTN_LEN and ttn.isdigit()


def phone_validation(phone):
    if phone is not None:
        return len(phone) == PHONE_LEN and phone.isdigit()
    else:
        return True
