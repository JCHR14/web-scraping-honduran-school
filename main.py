import pandas as pd

URL_FILE = r'C:\Users\Usuario\OneDrive\Documentos\projects\personal\web-scraping-honduran-school\data.csv'


def start_scraping():
    URL_BASE = 'http://estadisticas.se.gob.hn/see/busqueda.php?pagina='
    for page_number in range(1, 1749):
        url = f'{URL_BASE}{page_number}'
        table = get_data(url)
        table.to_csv(URL_FILE, mode='a', index=False, header=False, encoding='utf-16')
        print(f'Pagina numero: {page_number}')
    print('END!')


def get_data(url):
    tables = pd.read_html(url, attrs={'class': 'listado'})
    table = tables[1]
    table = table.loc[:, ~table.columns.str.contains('^Unnamed')]
    return table


if __name__ == "__main__":
    start_scraping()
