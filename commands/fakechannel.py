class FakeChannel(object):
    def send_message(self, message):
        print(message)
