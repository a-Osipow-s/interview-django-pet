import asyncio
from aiosmtpd.controller import Controller

class PrintHandler:
    async def handle_DATA(self, server, session, envelope):
        print('----- New Email -----')
        print(f'From: {envelope.mail_from}')
        print(f'To: {envelope.rcpt_tos}')
        print(f'Data:\n{envelope.content.decode("utf8", errors="replace")}')
        print('--------------------\n')
        return '250 Message accepted for delivery'

def run():
    controller = Controller(PrintHandler(), hostname='0.0.0.0', port=1025)
    controller.start()
    print("SMTP server running on port 1025")
    try:
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        controller.stop()

if __name__ == '__main__':
    run()