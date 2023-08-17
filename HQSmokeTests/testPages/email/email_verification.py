from imap_tools import MailBox
from imap_tools import AND, OR, NOT
from bs4 import BeautifulSoup
import re

from HQSmokeTests.userInputs.user_inputs import UserData

""""Contains test page elements and functions related to the app installation and form submission on mobile"""


class EmailVerification:

    def __init__(self, settings):
        self.imap_host = "imap.gmail.com"
        self.imap_user = settings['login_username']
        self.imap_pass = settings['imap_password']

    def get_hyperlink_from_latest_email(self, subject):
        with MailBox(self.imap_host).login(self.imap_user, self.imap_pass, 'INBOX') as mailbox:
            bodies = [msg.html for msg in
                      mailbox.fetch(AND(subject=subject))]
        soup = BeautifulSoup(str(bodies), "html.parser")
        links = []
        for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
            links.append(link.get('href'))
            # print("link: ", link)
        # links  # in this you will have to check the link number starting from 0.
        print(len(links))
        print(links[len(links) - 1])
        return str(links[len(links) - 1])
