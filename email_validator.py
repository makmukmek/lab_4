import re

class EmailValidator:
    """Класс для валидации email-адресов"""
    
    def __init__(self):
        # Простое регулярное выражение для проверки email
        self.pattern = r'^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.[a-zA-Z0-9_.]+$'
    
    def is_valid_email(self, email):
        """Проверяет валидность email-адреса"""
        try:
            if not email or not isinstance(email, str):
                return False
            
            # Проверяем соответствие паттерну
            if not re.match(self.pattern, email):
                return False
            
            # Дополнительные проверки
            parts = email.split('@')
            if len(parts) != 2:
                return False
            
            local_part, domain = parts
            
            # Проверяем, что после @ есть точка
            if '.' not in domain:
                return False
            
            # Проверяем, что доменная часть не начинается или не заканчивается точкой
            domain_parts = domain.split('.')
            if any(not part for part in domain_parts):
                return False
            
            return True
            
        except Exception:
            return False
    
    def filter_valid_emails(self, emails_string):
        """Фильтрует валидные email из строки"""
        try:
            if not emails_string:
                return []
            
            emails = emails_string.split()
            valid_emails = []
            
            for email in emails:
                if self.is_valid_email(email.strip()):
                    valid_emails.append(email.strip())
            
            return valid_emails
            
        except Exception as e:
            print(f"Ошибка при фильтрации email: {e}")
            return []