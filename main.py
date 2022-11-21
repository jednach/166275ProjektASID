class ListaWpis:
    def __init__(self, wart_, lista_, nast_=None):
        self.wart = wart_
        self.lista = lista_
        self.lista.dlugosc += 1
        if self.lista.dlugosc == 1:
            self.lista.element = self
            self.nast = self
        else:
            current = self.lista.element
            while current.nast != nast_:
                current = current.nast
            temp = current.nast
            current.nast = self
            current.nast.nast = temp

    def dodaj_po_nim(self, wart_):
        temp = self.nast
        self.nast = ListaWpis(wart_, self.lista, temp)


class Lista_1k_k:
    def __init__(self):
        self.element = None
        self.dlugosc = 0

    def pobierz_el(self, idx):
        i = 0
        current = self.element
        while i != idx % self.dlugosc:
            current = current.nast
            i += 1
        return current

    def odwroc(self):
        l = Lista_1k_k()
        n = ListaWpis(self.element.wart, l)
        i = 1
        current = self.element.nast
        while i < self.dlugosc:
            n.dodaj_po_nim(current.wart)
            current = current.nast
            i += 1
        l.element = l.element.nast
        return l

    def zlicz_mniejsze(self, prog):
        i = 0
        res = 0
        current = self.element
        while i < self.dlugosc:
            if current.wart < prog:
                res += 1
            i += 1
            current = current.nast
        return res

    def obrob_wartosc(self, funkcja):
        i = 0
        current = self.element
        while i < self.dlugosc:
            funkcja(current.nast.wart)
            current = current.nast
            i += 1

    def przekrec(self):
        self.element = self.element.nast

    def czy_posortowane(self):
        if self.element is None:
            return True
        i = 0
        current = self.element
        while i < self.dlugosc - 1:
            if current.wart > current.nast.wart:
                return False
            i += 1
            current = current.nast
        return True

    def __repr__(self):
        s = ''
        i = 0
        current = self.element
        while i < self.dlugosc:
            s += (str(current.wart) + '->')
            i += 1
            current = current.nast
        return s


def foo(x):
    print(x)


l1 = Lista_1k_k()
n1 = ListaWpis(-0.1, l1)
n2 = ListaWpis(1.3, l1, n1)
n3 = ListaWpis(2.4, l1, n2)
n4 = ListaWpis(3.6, l1, n1)
n3.dodaj_po_nim(4.7)
print(l1)
print(l1.pobierz_el(6).wart)
print(l1.czy_posortowane())
print(l1.zlicz_mniejsze(4))
l2 = l1.odwroc()
print(l2)
print(l2.pobierz_el(0).wart)
print(l2.pobierz_el(4).wart)
l2.przekrec()
print(l2)
print(l2.pobierz_el(4).wart)
print(l2.pobierz_el(3).wart)
l3 = Lista_1k_k()
m1 = ListaWpis(1, l3)
m2 = ListaWpis(2, l3, m1)
m3 = ListaWpis(3, l3, m1)
m4 = ListaWpis(4, l3, m2)
l4 = Lista_1k_k()
print(l4.czy_posortowane())
