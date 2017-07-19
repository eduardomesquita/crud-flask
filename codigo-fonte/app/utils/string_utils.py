'''
Classe utilitaria para realizacao dos testes
'''

class StringUtils(object):

    def to_upper(self, string):
        return string.upper()

    def to_lower(self, string):
        return string.lower()

    def is_upper(self, string):
        return string.isupper()

    def join(self, list_object):
        return ','.join(list_object)
