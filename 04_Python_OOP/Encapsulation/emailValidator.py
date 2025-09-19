class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return True if mail in self.mails else False

    def __is_domain_valid(self, domain):
        return True if domain in self.domains else False

    def validate(self, email):
        name, format = email.split("@")
        mail, domain = format.split(".")
        if self.__is_name_valid(name) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain):
            return True
        return False

mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email = EmailValidator(6, mails, domains)
print(email.validate("pe77er@gmail.com"))
print(email.validate("georgios@gmail.net"))
print(email.validate("stamatito@abv.net"))
print(email.validate("abv@softuni.bg"))