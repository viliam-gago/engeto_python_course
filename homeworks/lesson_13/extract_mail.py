text = 'This is some abc@email.com/ example@mail.org, text that contains efg@mail.cz.'

def get_domains(string):
    domains = list(filter(lambda x: '@' in x, text.split(' ')))
    stripped_domains = list(map(lambda x: x[x.index('@') + 1:-1], domains))
    return stripped_domains

print(get_domains(text))