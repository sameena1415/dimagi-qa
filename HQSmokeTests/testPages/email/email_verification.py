import datetime
import time

from imap_tools import MailBox
from imap_tools import AND, OR, NOT
from bs4 import BeautifulSoup
import re
import pandas as pd

from HQSmokeTests.userInputs.user_inputs import UserData

""""Contains test page elements and functions related to the app installation and form submission on mobile"""


class EmailVerification:

    def __init__(self, settings):
        self.imap_host = "imap.gmail.com"
        self.imap_user = settings['login_username']
        self.imap_pass = settings['imap_password']

    def get_hyperlink_from_latest_email_old(self, subject, url):
        if 'www' in url:
            from_email = UserData.from_email_prod
        elif 'india' in url:
            from_email = UserData.from_email_india
        elif "eu" in url:
            from_email = UserData.from_email_eu
        else:
            from_email = UserData.from_email
        print(f"Subject to be fetched: {subject} from email: {from_email}")
        with MailBox(self.imap_host).login(self.imap_user, self.imap_pass, 'INBOX') as mailbox:
            bodies = list(mailbox.fetch(AND(subject=subject, from_=from_email,
                                        date=datetime.date.today()
                                        ),
                                    reverse=True, limit=2
                                    ))
        if not bodies:
            raise AssertionError("No matching emails found")

        # Sort by date explicitly
        bodies.sort(key=lambda m: m.date, reverse=True)
        latest_msg = str(bodies[0])  # guaranteed newest by timestamp
        print(latest_msg)
        soup = BeautifulSoup(latest_msg, "html.parser")
        # soup = BeautifulSoup(str(bodies[len(bodies) - 1]), "html.parser")
        links = []
        for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
            links.append(link.get('href'))
            # print("link: ", link)
        # links  # in this you will have to check the link number starting from 0.
        print(len(links))
        print(links[0])
        return str(links[0])

    from imap_tools import MailBox, AND
    from bs4 import BeautifulSoup
    import datetime, time, re

    def get_hyperlink_from_latest_email(self, subject, url):
        # --- Determine sender based on environment URL ---
        if 'www' in url:
            from_email = UserData.from_email_prod
        elif 'india' in url:
            from_email = UserData.from_email_india
        elif "eu" in url:
            from_email = UserData.from_email_eu
        else:
            from_email = UserData.from_email

        print(f"📧 Looking for subject: '{subject}' from: {from_email}")

        max_retries = 3
        all_msgs = []
        now = datetime.datetime.now()
        five_min_ago = now - datetime.timedelta(minutes=5)

        for attempt in range(max_retries):
            try:
                # --- Search both Inbox and Spam ---
                for folder in ["INBOX", "[Gmail]/Spam"]:
                    with MailBox(self.imap_host).login(self.imap_user, self.imap_pass, folder) as mailbox:
                        msgs = list(mailbox.fetch(
                            AND(
                                from_=from_email,
                                subject=subject,
                                date=datetime.date.today()
                                ),
                            reverse=True,
                            limit=10
                            )
                            )
                        if msgs:
                            print(f"✅ Found {len(msgs)} message(s) in {folder}")
                            all_msgs.extend(msgs)

                if not all_msgs:
                    print(f"Attempt {attempt + 1}: No matching emails found. Retrying...")
                    time.sleep(5)
                    continue

                # --- Filter to only emails from the last 5 minutes ---
                recent_msgs = [
                    m for m in all_msgs
                    if m.date and (now - m.date.replace(tzinfo=None)) <= datetime.timedelta(minutes=5)
                    ]

                if not recent_msgs:
                    print(f"Attempt {attempt + 1}: Found emails, but none within last 5 minutes. Retrying...")
                    time.sleep(5)
                    continue

                # --- Sort by message date (latest first) ---
                recent_msgs.sort(key=lambda m: m.date, reverse=True)
                latest_msg = recent_msgs[0]

                print(f"✅ Latest message found: {latest_msg.subject}")
                print(f"📅 Received at: {latest_msg.date}")

                # --- Parse HTML body for hyperlinks ---
                soup = BeautifulSoup(latest_msg.html or "", "html.parser")
                links = [
                    link.get('href')
                    for link in soup.find_all('a', attrs={'href': re.compile(r"^https://")})
                    ]

                if links:
                    print(f"✅ Found {len(links)} link(s). First: {links[0]}")
                    return links[0]

                print(f"Attempt {attempt + 1}: No links found in recent email. Retrying...")
                time.sleep(5)

            except Exception as e:
                print(f"⚠️ IMAP error on attempt {attempt + 1}: {e}")
                time.sleep(3)

        raise AssertionError("❌ No recent hyperlink email found (within last 5 minutes, Inbox/Spam).")

    def get_email_body_from_latest_email(self, subject, url):
        if 'www' in url:
            from_email = UserData.from_email_prod
        elif 'india' in url:
            from_email = UserData.from_email_india
        elif "eu" in url:
            from_email = UserData.from_email_eu
        else:
            from_email = UserData.from_email
        print(subject)
        with MailBox(self.imap_host).login(self.imap_user, self.imap_pass, 'INBOX') as mailbox:
            bodies = [msg.html for msg in
                      mailbox.fetch(AND(subject=subject, from_=from_email, date=datetime.date.today()))]
        print(len(bodies))
        n = ''
        end = -1
        if "Worker Activity" in subject or "Case Activity" in subject:
            n = 2
        else:
            n = 1
        if "Application Status" in subject or "Device Log" in subject or "Case List" in subject:
            end = None
        else:
            end = -1
        soup = BeautifulSoup(str(bodies[len(bodies) - 1]), "html.parser")
        tr = []
        table = []

        for row in soup.select("tr")[n:end]:
            for td in row.select("td"):
                td = td.get_text()
                td = str(td).replace("\\r", '')
                td = str(td).replace("\\n", '')
                td = re.sub("\r\n+", "", td)
                tr.append(td.strip())
            table.append(tr)
        print(len(table))
        print(table[-1])
        return table[-1]

    def get_email_body_from_latest_email_proj_perf(self, subject, url):
        if 'www' in url:
            from_email = UserData.from_email_prod
        elif 'india' in url:
            from_email = UserData.from_email_india
        elif "eu" in url:
            from_email = UserData.from_email_eu
        else:
            from_email = UserData.from_email
        print(subject)
        with MailBox(self.imap_host).login(self.imap_user, self.imap_pass, 'INBOX') as mailbox:
            bodies = [msg.html for msg in
                      mailbox.fetch(AND(subject=subject, from_=from_email, date=datetime.date.today()))]
        soup = BeautifulSoup(str(bodies[len(bodies) - 1]), "html.parser")
        tr = []
        td = []
        table = []
        tab_low = []
        tab_inactive = []
        tab_high = []
        for tables in soup.findAll('table'):
            table.append(tables)
        table_low = table[0]
        table_inactive = table[1]
        table_high = table[2]

        if len(table_low.findAll('td')) > 0:
            print(len(table_low.findAll('td')))
            for row in table_low.select("tr"):
                tr = []
                for cells in row.select("td"):
                    td = []
                    text = cells.get_text()
                    text = str(text).replace("\\r", '')
                    text = str(text).replace("\\n", '')
                    text = re.sub("\r\n+", "", text)
                    text = str(text).replace(u'\xa0', u'')
                    text = str(text).strip()
                    text = re.sub(" +", "--", text)
                    if text == '':
                        td.append("No data available in table")
                    else:
                        td.append(text)
                    tr.extend(td)
                if tr == []:
                    print("empty row")
                else:
                    tab_low.extend(tr)
        else:
            tab_low = ['No data available in table']

        print("tab low", tab_low)

        if len(table_inactive.findAll('td')) > 0:
            print(len(table_inactive.findAll('td')))
            for row in table_inactive.select("tr"):
                tr = []
                for cells in row.select("td"):
                    td = []
                    text = cells.get_text()
                    text = str(text).replace("\\r", '')
                    text = str(text).replace("\\n", '')
                    text = re.sub("\r\n+", "", text)
                    text = str(text).replace(u'\xa0', u'')
                    text = str(text).strip()
                    text = re.sub(" +", "--", text)
                    if text == '':
                        td.append("No data available in table")
                    else:
                        td.append(text)
                    tr.extend(td)
                if tr == []:
                    print("empty row")
                else:
                    tab_inactive.extend(tr)
        else:
            tab_inactive = ['No data available in table']

        print("tab inactive", tab_inactive)

        if len(table_high.findAll('td')) > 0:
            print(len(table_high.findAll('td')))
            for row in table_high.select("tr"):
                tr = []
                for cells in row.select("td"):
                    td = []
                    text = cells.get_text()
                    text = str(text).replace("\\r", '')
                    text = str(text).replace("\\n", '')
                    text = re.sub("\r\n+", "", text)
                    text = str(text).replace(u'\xa0', u'')
                    text = str(text).strip()
                    text = re.sub(" +", "--", text)
                    if text == '':
                        td.append("No data available in table")
                    else:
                        td.append(text)
                    tr.extend(td)
                if tr == []:
                    print("empty row")
                else:
                    tab_high.extend(tr)
        else:
            tab_high = ['No data available in table']

        print("tab high", tab_high)
        table_data = [tab_low + tab_inactive + tab_high]
        return table_data

    def verify_email_sent(self, subject, url, sleep = 'NO'):
        if 'www' in url:
            from_email = UserData.from_email_prod
        elif 'india' in url:
            from_email = UserData.from_email_india
        elif "eu" in url:
            from_email = UserData.from_email_eu
        else:
            from_email = UserData.from_email

        print(f"📧 Checking for subject: '{subject}' from email: {from_email}")
        if sleep != 'NO':
            print("Sleeping a couple of minutes for the emails to get triggered")
            time.sleep(120)
        now = datetime.datetime.now()

        # --- Search both Inbox and Spam folders ---
        for folder in ["INBOX", "[Gmail]/Spam"]:
            with MailBox(self.imap_host).login(self.imap_user, self.imap_pass, folder) as mailbox:
                msgs = list(mailbox.fetch(
                    AND(
                        from_=from_email,
                        subject=subject,
                        date=datetime.date.today()
                        ),
                    reverse=True,
                    limit=10
                    )
                    )

                for msg in msgs:
                    msg_time = msg.date.replace(tzinfo=None)
                    time_diff = (now - msg_time).total_seconds() / 60  # minutes

                    if (
                            msg.subject
                            and msg.subject.strip().lower() == subject.strip().lower()
                            and time_diff <= 5  # within last 5 minutes
                    ):
                        print(f"✅ Email received in {folder}")
                        print(f"📅 Received at: {msg.date}")
                        return True

        raise AssertionError("❌ No email received within the last 5 minutes (Inbox/Spam).")

    def verify_email_sent_new(self, subject, url):
        if 'www' in url:
            from_email = UserData.from_email_prod
        elif 'india' in url:
            from_email = UserData.from_email_india
        elif "eu" in url:
            from_email = UserData.from_email_eu
        else:
            from_email = UserData.from_email
        print(f"Subject to be fetched: {subject} from email: {from_email}")
        max_retries = 3
        for attempt in range(max_retries):
            try:
                with MailBox(self.imap_host).login(self.imap_user, self.imap_pass, 'INBOX') as mailbox:
                    # Fetch only recent few (reverse=True gives most recent first)
                    msgs = list(mailbox.fetch(
                        AND(from_=from_email, date=datetime.date.today()),
                        reverse=True,  # newest first
                        limit=5  # fetch only 5 recent emails
                        )
                        )

                    for msg in msgs:
                        if msg.subject.strip() == subject.strip():
                            print("✅ Email is received")
                            return True

                print(f"Attempt {attempt + 1}: Email not found yet. Retrying...")
                time.sleep(5)
            except Exception as e:
                print(f"IMAP error on attempt {attempt + 1}: {e}")
                time.sleep(3)
        raise AssertionError("❌ Email not received after multiple retries")
