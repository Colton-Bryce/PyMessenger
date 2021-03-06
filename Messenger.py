from smtplib import SMTP


class Messenger(object):
    def __init__(self, email_server, account_credentials, port=587):
        self.login = account_credentials
        self.email_server = email_server
        self.port = port

        self.carriers = {'att': '@txt.att.net',  # MMS: @mms.att.net
                         'tmobile': '@tmomail.net',
                         'verizon': '@vtext.com',  # Only SMS, no MMS
                         'sprint': '@pm.sprint.com',
                         'virgin': '@vmobl.com',
                         'tracfone': '@mmst5.tracfone.com',
                         'metropcs': '@mymetropcs.com',
                         'boost': '@myboostmobile.com',
                         'cricket': '@mms.cricketwireless.net',
                         'ptel': '@ptel.com',
                         'republic': '@text.republicwireless.com',
                         'googlefi': '@msg.fi.google.com',
                         'suncom': '@tms.suncom.com',
                         'ting': '@message.ting.com',
                         'uscellular': '@email.uscc.net',
                         'consumer': '@cingularme.com',
                         'cspire': '@cspire1.com',
                         'pageplus': '@vtext.com'}

    def sendtext(self, number, carrier, msg):
        number = str(number)

        # Get carrier from pre-defined list, or ue the one provided
        try:
            carrier = self.carriers[carrier]
        except KeyError:
            pass

        toaddrs = number + carrier

        # The new line is required for it to work
        msg = ('\n' + msg)

        server = SMTP(self.email_server, self.port)
        server.starttls()
        server.login(self.login[0], self.login[1])
        server.sendmail('', toaddrs, msg)
        server.quit()
