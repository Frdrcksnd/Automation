import imapclient
import pprint
import imaplib
import time
imaplib._MAXLINE = 10000000


user_name =input("Enter your email address and press enter: ")
password = input("Enter your password and press enter: ")
server = imapclient.IMAPClient('imap.gmail.com', ssl=True)


def main():
    try:
        server.login(user_name, password)
    except Exception as exc:
        print(f"There was an error: {exc}")
    else:
        print(f"Successfully logged in to {user_name}")

    try:
        server.select_folder('INBOX', readonly=False)
        UIDs = server.search(['UNSEEN'])

        num = len(UIDs)
        print(f"You have {num} unread messages")
        time.sleep(2)

    except Exception as exc:
        print(f"There was an error: {exc}")

    try:
        for mssg_ID in UIDs:
            raw_message = server.fetch(mssg_ID, ['BODY[]'])
            pprint.pprint(raw_message)

    except Exception as exc:
        print(f"There was an error: {exc}")

    else:
        print("Done!!!")

        server.logout()

if  __name__ == "__main__" :
    main()
