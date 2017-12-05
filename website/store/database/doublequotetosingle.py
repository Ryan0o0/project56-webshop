def toSingleQuotes(txt):
    for i in txt:
        if i == '"':
            txt = txt.replace('"', "'")
    print(txt)

toSingleQuotes("""<tr style="text-align: center;" align="center">
		<td style="text-align: center; border-left-width: 0; border-top-color: #ffffff; border-top-width: 1px; border-top-style: solid; border-bottom-width: 0; border-bottom-style: solid; border-bottom-color: #e0e0e0; border-left-style: solid; border-left-color: #e0e0e0; -moz-border-radius-bottomleft: 3px; -webkit-border-bottom-left-radius: 3px; border-bottom-left-radius: 3px; background-image: -moz-linear-gradient(top,  #fbfbfb,  #fafafa); padding: 18px 18px 18px 20px;" align="center">{{ e.productNum }}</td>
		<td style="text-align: center; border-left-width: 0; border-top-color: #ffffff; border-top-width: 1px; border-top-style: solid; border-bottom-width: 0; border-bottom-style: solid; border-bottom-color: #e0e0e0; border-left-style: solid; border-left-color: #e0e0e0; -moz-border-radius-bottomleft: 3px; -webkit-border-bottom-left-radius: 3px; border-bottom-left-radius: 3px; background-image: -moz-linear-gradient(top,  #fbfbfb,  #fafafa); padding: 18px 18px 18px 20px;" align="center">{{ prodName {{ e.productNum }} }}</td>
		<td style="border-top-color: #ffffff; border-top-width: 1px; border-top-style: solid; border-bottom-width: 0; border-bottom-style: solid; border-bottom-color: #e0e0e0; border-left-width: 1px; border-left-style: solid; border-left-color: #e0e0e0; -moz-border-radius-bottomright: 3px; -webkit-border-bottom-right-radius: 3px; border-bottom-right-radius: 3px; background-image: -moz-linear-gradient(top,  #fbfbfb,  #fafafa); padding: 18px;">{{ e.amount }}</td>
		</tr>""")