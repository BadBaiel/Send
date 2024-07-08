import vonage

client = vonage.Client(application_id='ваш_application_id', private_key='путь_к_вашему_private_key')
whatsapp = vonage.WhatsApp(client)

responseData = whatsapp.send_message({
    "from": "+996707663085",  # Номер, предоставленный Vonage для WhatsApp
    "to": "+996999188836",          # Номер получателя в формате WhatsApp
    "text": "Э чо там"
})

print(responseData)