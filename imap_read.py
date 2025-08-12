from imapclient import IMAPClient
import pyzmail

host = 'imap.gmail.com'
username='dataautomation.py@gmail.com'
app_password="bysrdzjryxrlaluo"

with  IMAPClient(host) as client:
    client.login (username,app_password)
    client.select_folder('inbox')
    message=client.search(['UNSEEN'])
    print(f"unread message : {len(message)}")
    for uid in message:
        raw_message= client.fetch([uid],['BODY[]','FLAGS'])
        message = pyzmail.PyzMessage.factory(raw_message[uid][b'BODY[]'])
        subject=message.get_subject()
        from_email=message.get_address('from')
        print("from: ",from_email)
        print("subject: ",subject)
        if message.text_part:
            print("mail:\n",message.text_part.get_payload().decode(message.text_part.charset))
        elif message.html_part :
            print("mail:\n",message.html_part.get_payload().decode(message.html_part.charset))

            print ("="*50)

