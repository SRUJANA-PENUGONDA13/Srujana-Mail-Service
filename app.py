from flask import Flask
import os
from mail.mail import *
  
app = Flask(__name__)
  
@app.route("/")
def home_page():
        msg = "Please go through the below url for sending mail with name, mail and message details"
        url = "https://srujana-mail-service.herokuapp.com/mail/{{toMail}}/{{subject}}/{{message}}"
        instructions = { "toMail" : "Receivers Mail Address", "Subject" : "Subject of mail (plain text format)", "Message" : "Message must be sent in the below dictionary format\n { senderName : name of the sender, receiverName : Receiver name ,mail : senders mail , message : message to receiver }"}
        details = { "URL" : url, "Instructions" : instructions, "Message" : msg}
        return {"Details" : details, "Status" : "Success"}

@app.route("/mail/<toMail>/<subject>/<message>")
def mail(toMail,subject,message):
    try:
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        mail_path = os.path.join(THIS_FOLDER, 'mail')
        os.chdir(mail_path)
        message = generateHtmlMessage(message)
        send_status(toMail,subject,message)
        return {"status" : "Success"}
    except Exception as e:
        error = str(e)
        return {"status" : "Fail",
                "error"  : error }

def generateHtmlMessage(message):
    result = eval(message)
    htmlMessage = "<html><body><h2>Hi "+result.get('receiverName')+",</h2><p>"+result.get('message')+"</p><br><h3>Contact Details:</h3><p>"+result.get('senderName')+"</p><p>"+result.get('mail')+"</p></body></html>"
    return htmlMessage
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

