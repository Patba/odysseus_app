from app import db
from app.utils.managers import DbManager
import smtplib as smtp
from email.message import EmailMessage
from app.utils.util_methods import get_user_by_group, get_group_name, get_user_details

db_man = DbManager(db)

def send_notification(ticket) -> None:

    email_addr = 'odysseus.app.notification@gmail.com'
    email_passwd = 'you_thought_there_would_be_a_password_huh?'
    smtp_ssl_addr = 'smtp.gmail.com'
    port = 465
    users = get_user_by_group(ticket.group)
    connection = smtp.SMTP_SSL(smtp_ssl_addr, port)
    connection.login(email_addr, email_passwd)
    for user in users:
        recipient = get_user_details(user)
        if recipient.email_not == 1:
            msg = EmailMessage()
            username = recipient.username
            msg['Subject'] = f"Ticket no. {ticket.id} raised by {ticket.owner} for your group {get_group_name(ticket.group)} "
            msg['From'] = email_addr
            msg['To'] = recipient.email
            msg.set_content(f"""\
            Hello there, {username},\n\n
            This email is to inform you that a new ticket has been raised for your group.\n\n
            Kind Regards,\n
            Odysseus Team
            """)

            #
            # This was a test to see if you can send a photo as well, but it's returning with MIME text
            #
            # odysseus_logo_message = make_msgid()
            # msg.add_alternative(f"""\
            # <html>
            #     <head></head>
            #     <body>
            #         <p>Hello there, {username},</p>
            #         <p>This email is to inform you that a new ticket has been raised for your group.
            #         </p>
            #         <p>Kind Regards,\n</p>
            #         <p>Odysseus Team</p>
            #         <img src="cid:{odysseus_logo_message}" />
            #     </body>
            # </html>
            #
            #
            # """.format(odysseus_logo_message=odysseus_logo_message[1:-1]), subtype='html')
            #
            # with open(get_odysseus_img(), 'rb') as img:
            #     msg.get_payload()[1].add_related(img.read(), 'image', 'png', cid=odysseus_logo_message)
            connection.send_message(msg)
    connection.close()

