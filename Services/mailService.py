from flask_mail import Message
from configPack import mail

sender='Contact@carhub.com'
def sendVerificationMail(email, name):
    msg = Message('CarHub Signup Confirmation',
                  sender='Contact@carhub.com', recipients=[email])
    msg.body = "Dear " + name + ":" + \
        "\n Thank you for registering on our website. We're excited to have you as a member of our community! \nYour account has been created and is now active. You can now log in successfully." + \
        "\nAs a member, you have access to exclusive content and features on our website, including parking spots reservation ,  and an exclusive visibility over Gaz stations."+\
            "\nIf you have any questions or concerns, please don't hesitate to contact us at "+sender +\
            "\nThank you for choosing us,"+\
            "\nCarHub Team"

    mail.send(msg)
