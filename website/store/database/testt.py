import math

counter = 10
rowscounter = counter
columncounter = counter
cnt = 0
txt = ""
if counter < 4:
  rowscounter = 1
  columncounter = counter
else:
  if counter % 3 != 0:
      rowscounter= math.ceil(counter / 3)
  else:
      rowscounter = int(counter / 3)
  columncounter = 3

for i in range(rowscounter):
    txt += "<ul class='list'>"
    if counter % 3 != 0 and i == (rowscounter - 1):
        columncounter = counter % 3
    for x in range(columncounter):
        txt += "x "
        cnt += 1
    txt += "</ul> \n"
print(txt)
print("counter: ", counter)
print("rowscounter: ", rowscounter)
print("columncounter: ", columncounter)