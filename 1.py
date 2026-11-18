import qrcode

while True:
    print("\nQR CODE GENERATOR\n")
    print("1. Link or text")
    print("2. Contact card")
    print("3. WiFi")
    print("4. Exit")
    choice = input("Choose above option: ")

    if choice == "1":
      text = input("Enter the text or link: ")
      file = input("Enter file name: ")
      img = qrcode.make(text)
      img.save(file + ".png")
      print("QR Code generated:", file + ".png")

    elif choice == "2":
      name = input("Enter Name: ")
      phone = input("Enter Phone Number: ")
      card = ["BEGIN:VCARD","VERSION:3.0",f"FN:{name}",f"TEL:{phone}","END:VCARD"]
      contact_info = "\n".join(card)
      img = qrcode.make(contact_info)
      img.save("Contact.png")
      print("QR Code generated: Contact.png")

    elif choice == "3":
      ssid = input("WiFi SSID: ")
      password = input("WiFi Password: ")
      wifi = f"WIFI:T:WPA;S:{ssid};P:{password};;"
      img = qrcode.make(wifi)
      img.save("WiFi.png")
      print("QR Code generated: WiFi.png")

    elif choice == "4":
      print("Bye!")
      break

    else:
      print("Wrong Choice!")