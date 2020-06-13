my_str = '''Lorem ipsum dolor sit amet, consectetur adipiscing
        elit. Mauris vulputate lacus id eros consequat tempus.
        Nam viverra velit sit amet lorem lobortis, at tincidunt
        nunc ultricies. Duis facilisis ultrices lacus, id
        tiger123@email.cz auctor massa molestie at. Nunc tristique
        fringilla congue. Donec ante diam cnn@info.com, dapibus
        lacinia vulputate vitae, ullamcorper in justo. Maecenas
        massa purus, ultricies a dictum ut, dapibus vitae massa.
        Cras abc@gmail.com vel libero felis. In augue elit, porttitor
        nec molestie quis, auctor a quam. Quisque b2b@money.fr
        pretium dolor et tempor feugiat. Morbi libero lectus,
        porttitor eu mi sed, luctus lacinia risus. Maecenas posuere
        leo sit amet spam@info.cz. elit tincidunt maximus. Aliquam
        erat volutpat. Donec eleifend felis at leo ullamcorper cursus.
        Pellentesque id dui viverra, auctor enim ut, fringilla est.
        Maecenas gravida turpis nec ultrices aliquet.'''


def main(text):
    text_list = my_str.split(' ')

    mails = extract_mails(text_list)

    numeric = collect_numeric(mails)

    domains = extract_domains(mails)

    result = {'domains': domains, 'emails_with_nums': numeric}

    return result


def extract_mails(text):
    mails = []
    for word in text:
        if '@' in word:
            mails.append(word.strip('.,\n'))
    return mails


def collect_numeric(mails):
    numeric = []
    for mail in mails:
        for char in mail:
            if char.isnumeric():
                numeric.append(mail)
                break

    return numeric


def extract_domains(mails):
    domains = list()
    for mail in mails:
        index = mail.index('@') + 1
        domains.append(mail[index:])

    return domains


print(main(my_str))
