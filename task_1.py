import re

def email_parse(email_address):
    pattern = re.compile(r"(?P<username>\w+)@(?P<domian>\w+\.\w{2,3}$)")
    r = pattern.finditer(email_address)
    try:
        for i in r:
            result = (i.groupdict())
        return result
    except:
        result = 'wrong email: ' + email_address
        return result


if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'))
