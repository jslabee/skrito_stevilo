print "Dobrodosli v programu seznam opravil"
opravila = {}
while True:
    opravilo = raw_input("prosim vnesite opravilo ki ga je potrebno narediti: ")

    narejeno = raw_input("je to opravilo narejeno ja/ne: ")

    if narejeno == "ja":
        opravila[opravilo] = True
    else:
        opravila[opravilo] = False


    print opravilo
    jane = raw_input("zelite vnesti se kaksno opravilo ja/ne")
    if jane == "ne":

        with open("todo.txt", "w+") as todo_file:
                print "opravljena opravila"
                todo_file.write("dokoncana opravila:\n")
                for opravilo in opravila:
                    if opravila[opravilo] == True:
                        print  opravilo
                        todo_file.write(opravilo + "\n")
                print "neopravljena opravila: "
                todo_file.write("nedokoncana opravila:\n")
                for opravilo in opravila:
                    if opravila[opravilo] == False:
                            print opravilo
                            todo_file.write(opravilo + "\n")


        break
