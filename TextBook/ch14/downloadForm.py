import ezsheets

ID = '1BbXgy-quD9UEA4LLfAB19TqKi_GNjR1z2IpPfmuOBLQ' 

ss = ezsheets.Spreadsheet(ID)
sheet = ss[0]
for row in range(sheet.rowCount):
    data = sheet.getRow(row + 1)
    print(data)
