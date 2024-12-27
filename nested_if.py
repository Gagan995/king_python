has_ticket = True
has_id = False
is_vip = True

if has_ticket:
    if has_id:
        print("watch the show")
    else:
        print("id is required")

else:
    if is_vip:
        print("watch the show")
    else:
        print("No vip No Ticket")
    print("Please buy a ticket")