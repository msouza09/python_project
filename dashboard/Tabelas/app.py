from rich.table import Table 
from rich.console import Console 

console = Console()
table = Table(title='Filmes Favoritos')

table.add_column('Nome',justify='left', style='red')
table.add_column('Data de lançamento', style='green')
table.add_column('Faturamento', style='purple')

table.add_row('Piratas do Caribe', '2005', '1599999')
table.add_row('Star Wars', '2009', '3412551')
table.add_row('Pica Longa e Perna Pau', '2021', '5215152')
table.add_row('Sonica e Monic', '2022', '2127586')

console.print(table)