import pytest
import random
from generators import NoteGenerator, MultipleOfThreeGenerator
from email_validator import EmailValidator

class TestNoteGenerator:
    """Тесты для генератора нот"""
    
    def setup_method(self):
        self.generator = NoteGenerator()
    
    def test_notes_list(self):
        """Проверка списка нот"""
        expected_notes = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
        assert self.generator.notes == expected_notes
    
    def test_generate_notes_count(self):
        """Проверка количества генерируемых нот"""
        count = 10
        notes = list(self.generator.generate_notes(count))
        assert len(notes) == count
    
    def test_generate_notes_content(self):
        """Проверка содержания генерируемых нот"""
        notes = list(self.generator.generate_notes(100))
        for note in notes:
            assert note in self.generator.notes

class TestMultipleOfThreeGenerator:
    """Тесты для генератора чисел, кратных 3"""
    
    def setup_method(self):
        self.generator = MultipleOfThreeGenerator()
    
    def test_generate_from_positive(self):
        """Проверка генерации из положительного числа"""
        a = 1
        gen = self.generator.generate_multiples(a)
        first_numbers = [next(gen) for _ in range(5)]
        expected = [3, 6, 9, 12, 15]
        assert first_numbers == expected
    
    def test_generate_from_negative(self):
        """Проверка генерации из отрицательного числа"""
        a = -100
        gen = self.generator.generate_multiples(a)
        first_numbers = [next(gen) for _ in range(5)]
        expected = [-99, -96, -93, -90, -87]
        assert first_numbers == expected
    
    def test_generate_from_zero(self):
        """Проверка генерации из нуля"""
        a = 0
        gen = self.generator.generate_multiples(a)
        first_numbers = [next(gen) for _ in range(5)]
        expected = [0, 3, 6, 9, 12]
        assert first_numbers == expected
    
    def test_all_multiples_of_three(self):
        """Проверка, что все числа кратны 3"""
        a = -50
        gen = self.generator.generate_multiples(a)
        for _ in range(100):
            number = next(gen)
            assert number % 3 == 0

class TestEmailValidator:
    """Тесты для валидатора email"""
    
    def setup_method(self):
        self.validator = EmailValidator()
    
    def test_valid_emails(self):
        """Проверка валидных email-адресов"""
        valid_emails = [
            "test@example.com",
            "user_name@domain.org",
            "test123@test.co.uk",
            "a@b.c"
        ]
        
        for email in valid_emails:
            assert self.validator.is_valid_email(email) == True
    
    def test_invalid_emails(self):
        """Проверка невалидных email-адресов"""
        invalid_emails = [
            "invalid-email",
            "no.at.sign",
            "@no.local.part",
            "no.domain@",
            "spaces in@local.com",
            "invalid@char@acters.com",
            "test@domain",  # нет точки после @
            "test@.com",    # точка сразу после @
            "test@domain."  # точка в конце
        ]
        
        for email in invalid_emails:
            assert self.validator.is_valid_email(email) == False
    
    def test_filter_valid_emails(self):
        """Проверка фильтрации email-адресов"""
        input_string = "test@example.com invalid user_name@domain.org no.at.sign"
        valid_emails = self.validator.filter_valid_emails(input_string)
        
        expected = ["test@example.com", "user_name@domain.org"]
        assert valid_emails == expected
    
    def test_empty_input(self):
        """Проверка обработки пустого ввода"""
        assert self.validator.filter_valid_emails("") == []
        assert self.validator.filter_valid_emails(None) == []
    
    def test_edge_cases(self):
        """Проверка граничных случаев"""
        assert self.validator.is_valid_email("") == False
        assert self.validator.is_valid_email(None) == False
        assert self.validator.is_valid_email("   ") == False

if __name__ == "__main__":
    pytest.main([__file__, "-v"])