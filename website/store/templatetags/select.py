amount = 4
amounttxt = "<select name='amount'>"
for i in range(12):
    if i == amount:
        amounttxt += "<option selected>" + str(amount) + "</option>"
    else:
        if i == 11:
            amounttxt += "<option>meer..</option>"
        else:
            amounttxt += "<option>" + str(i) + "</option>"
amounttxt += "</select>"

#print(amounttxt)