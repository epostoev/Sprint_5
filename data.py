import uuid

def generate_email():
    email = f"user_{uuid.uuid4().hex[:8]}@testmail.com"
    return email

BASE_URL = "https://qa-desk.education-services.ru/"
DEFAULT_PASSWORD = "TestPassword123!"
