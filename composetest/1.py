import wget

print('Beginning file download with wget module')

url = 'https://static.raycars.ru/img/favicon/apple-icon-57x57.png'
wget.download(url, '/app/static/1.png')
