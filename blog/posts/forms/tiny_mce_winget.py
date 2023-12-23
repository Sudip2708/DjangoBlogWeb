### Definuje formuláře (na webu) pro aplikaci.


from tinymce.widgets import TinyMCE


class TinyMCEWidget(TinyMCE):
    '''Definice vlastního widgetu pro TinyMCE editor'''
    def use_required_attribute(self, *args):
        '''
        Metoda umožňuje ovlivnit chování povinných atributů pro pole widgetu
        :param args: funkce může přijmout libovolný počet argumentů a tyto argumenty budou předávány jako n-tice (tuple)
        :return:  Vrací False, což znamená, že nevyžaduje atribut required (povinné pole) pro toto pole. Tato metoda umožňuje ovlivnit chování povinných atributů pro pole widgetu.
        '''
        return False