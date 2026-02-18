import random

class NoteGenerator:
    """Класс для генерации случайных нот"""
    
    def __init__(self):
        self.notes = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
    
    def generate_notes(self, count=1000000):
        """Генератор случайных нот"""
        for _ in range(count):
            yield random.choice(self.notes)

#"njn rjl yb hfpe yt cgbp;ty kjk
class MultipleOfThreeGenerator:
    """Класс для генерации чисел, кратных 3"""
    
    def generate_multiples(self, a):
        """Генератор чисел, кратных 3, начиная с a"""
        current = a
        while True:
            if current % 3 == 0:
                yield current
            current += 1
