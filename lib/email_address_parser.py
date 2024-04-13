import re

class EmailAddressParser:
    def __init__(self, addresses=str) -> None:
        self.addresses = addresses

    def parse(self):
        separated_emails = {email for email in re.split(r'[,\s]+', self.addresses)}

        valid_emails = [email for email in separated_emails if re.match(r'^[\w\.-]+@[\w\.-]+$', email)]

        return sorted(valid_emails)