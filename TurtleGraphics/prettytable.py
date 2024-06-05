from prettytable import PrettyTable
# Way 1 - Row by row
table = PrettyTable()
table.add_column("Music name", "Artist")
table.add_row(["We love your name", "Jaye Thomas"])
table.add_row(["Spread the Opps", "Lecrae"])
table.add_row(["Throne", "KB"])

print(table)

# Way 2 - Column by column
table2 = PrettyTable()
table2.add_column("Programming languages", ["Python", "Javascript", "React"])
table2.add_column("Years of experience", [4, 2, 1])

print(table2)

# Attributes
table.align = 'l'
table.border = True