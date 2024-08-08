customers = [
   {
      "name":"Customer1","phone":"09111111111","email":"customer1@email.com","township":"Hlaing"
   },
   {
      "name":"Customer2","phone":"09222222222","email":"customer1@email.com","township":"Alone"
   },
   {
      "name":"Customer3","phone":"09333333333","email":"customer3@email.com","township":"South Okkalar"
   },
   {
      "name":"Customer4","phone":"09444444444","email":"customer4@email.com","township":"Sanchaung"
   }
]
unique_emails = set()
for customer in customers:
    unique_emails.add(customer["email"])

for email in sorted(unique_emails):
    print(email)
