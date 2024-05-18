import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = "https://www.instagram.com/accounts/login/"

driver.get(url)
time.sleep(2)



username = "g.noffs777"
senha = "remama123"

driver.find_element(By.NAME, "username").send_keys(username)

time.sleep(2)

driver.find_element(By.NAME, "password").send_keys(senha)

time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


time.sleep(5)

pesquisa = "remamadragaorosa"
driver.find_element(By.CSS_SELECTOR, "[aria-label='Pesquisa']").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "[aria-label='Entrada da pesquisa']").send_keys(pesquisa)
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "[href='/remamadragaorosa/']").click()
time.sleep(3)

time.sleep(3)

main_element = driver.find_element(By.CLASS_NAME, "_ac7v.xzboxd6.xras4av.xgc1b0m")
main_element.find_element(By.TAG_NAME, "a").click()
time.sleep(3)
botao = driver.find_element(By.CLASS_NAME, "_abm0")


reels = 0
post = 0
contador = 0

while True:
    contador += 1
    print(f'POSTAGEM {contador}')
    try:
        titulo_postagem = driver.find_elements(By.CLASS_NAME, '_a9zs')[0].text
    except:
        print("nada encontrado")
        pass
    try:
        print(f'Titulo da postagem: {titulo_postagem}')
        data_postagem = driver.find_element(By.CLASS_NAME, 'x1p4m5qa').text
        print(f'Data da postagem: {data_postagem}')
    except NoSuchElementException:
        print("nada encontrado")
    try:
        qtd_curtidas = driver.find_elements(By.CLASS_NAME, '_aauw')[0].text
        print(f'Quantidade de Visualizações no post: {qtd_curtidas}')
    except:
        qtd_curtidas = driver.find_element(By.CSS_SELECTOR, "body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.x15h9jz8.x47corl.xh8yej3.xir0mxb.x1juhsu6 > div > article > div > div.x1qjc9v5.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xdt5ytf.x1iyjqo2.x5wqa0o.xln7xf2.xk390pu.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x65f84u.x1vq45kp.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x11njtxf > div > div > div.x78zum5.xdt5ytf.x1q2y9iw.x1n2onr6.xh8yej3.x9f619.x1iyjqo2.x18l3tf1.x26u7qi.xy80clv.xexx8yu.x4uap5.x18d9i69.xkhd6sd > section.x12nagc.x182iqb8.x1pi30zi.x1swvt13 > div > div > span > a > span").text
        print(f'Quantidade de Curtidas no post: {qtd_curtidas}')
    try:
        rell = driver.find_element(By.TAG_NAME, "video")
        if rell:
            print("tipo de postagem: Reels")
            reels += 1
            print()
            print(50 * "#")
            print()
    except NoSuchElementException:
        print("tipo de postagem: Imagem")
        post += 1
        print()
        print(50*"#")
        print()
    try:
        botao = driver.find_element(By.CSS_SELECTOR, "svg[aria-label='Avançar']")
        if botao:
            botao.click()
            time.sleep(0.3)
    except NoSuchElementException:
        time.sleep(4)
        break


print("rells = ", reels)
print("posts = ", post)


