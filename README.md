# Mail
A simple mail service developed using flask and google API, To send mails to anyone from my mail id in particular format.

Service - "https://srujana-mail-service.herokuapp.com/mail/{{toMail}}/{{subject}}/{{message}}

Instructions:

Message: Message must be sent in the below dictionary format <br />
 {  <br />
    senderName : name of the sender, <br />
    receiverName : Receiver name ,<br />
    mail : senders mail , <br />
    message : message to receiver <br />
}<br />
Subject: Subject of mail (plain text format)<br />
toMail: Receivers Mail Address<br />


