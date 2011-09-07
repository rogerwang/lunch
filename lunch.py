import dbus
bus = dbus.SessionBus()

buddies = ['sip:buddy1@yourdomain.com', 'sip:buddy2@yourdomain.com']
 
pidgin = bus.get_object("im.pidgin.purple.PurpleService", "/im/pidgin/purple/PurpleObject")
purple = dbus.Interface(pidgin, "im.pidgin.purple.PurpleInterface")
PURPLE_CONV_TYPE_IM = 1
 
account = purple.PurpleAccountsFind('your.email@yourdomain.com,', 'prpl-sipe')
for b in buddies:
    buddy = purple.PurpleFindBuddy(account, b)

    buddy_name = purple.PurpleBuddyGetName(buddy)
 
    print buddy_name
    im = purple.PurpleConvIm(purple.PurpleConversationNew(PURPLE_CONV_TYPE_IM, account, buddy_name))
    purple.PurpleConvImSend(im, "lunch?")
