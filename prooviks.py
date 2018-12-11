fail = open('lehekyljed.txt', "a+")
for rida in fail:
    if rida.split(",")[0] == "Meelelahutus":
        rida.append(","+"midagi")
    else:
        fail.write("\n"+"Meelelahutusmmmm"+","+"midagi")
        break
fail.close()