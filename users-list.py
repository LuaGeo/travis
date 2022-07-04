known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]

print(len(known_users))

while True:
    print("Hi! My name is Travis")
    name=input("What's your name? ").strip().capitalize()
    #.strip() usado por segurança caso o usuario coloque espaço
    #.capitalize() usado para deixar a primeira letra maiuscula caso o usuario digite em minusculo

    if name in known_users:
        print(f"Hello {name}!")
        #alternativa para ("Hello {}".format(name))
        remove=input("Would you like to be removed from the system (y/n)? ").strip().lower()
        #se nao usar o .lower() a proxima linha teria que ser
        #if remove=="y" or remove=="Y"
        if remove=="y":
            known_users.remove(name)
        elif remove=="n":
            print("No problem, I didn't want you leave anyway!")
            
    else:
        print(f"Hmmm, I don't think I have met you yet {name}")
        add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()
        if add_me=="y":
            known_users.append(name)
        elif add_me=="n":
            print("No worries, see you around!")