import sender

sender1 = sender.Sender("dojin")
sender1 = sender.DiscordSenderDecorator(sender1)

sender2 = sender.Sender("tehun")
sender2 = sender.EmailSenderDecorator(sender2)

sender3 = sender.Sender("suyong")
sender3 = sender.DiscordSenderDecorator(sender3)
sender3 = sender.EmailSenderDecorator(sender3)

sender1.send()
print()
sender2.send()
print()
sender3.send()