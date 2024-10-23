from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import requests
import os

with sync_playwright() as p: #with garante que o código vai inicializar e encerrar sozinho.
    navegador = p.chromium.launch(headless=False) #headless=False é para o navegador não ficar invisível
    siteLaboratorio = navegador.new_page() #abre uma página em branco no navegador (fecha logo em seguida)
    siteLaboratorio.goto('https://webview.metroex.com.br/login') #.goto = adicionar o link da página que desejamos acessar
    time.sleep(1) #segundos antes de executar a próxima linha de código
    # siteLaboratorio.locator('xpath=//*[@id="mat-input-0"]').click() = .locator e .click seria apenas caso eu quisesse clicar no campo ou input
    siteLaboratorio.fill('xpath=//*[@id="mat-input-0"]', 'kely.pesavento@novus') #.fill = insere o e-mail no input, necessário copiar caminho xpath do "elemento"
    siteLaboratorio.fill('xpath=//*[@id="mat-input-1"]', 'TDzWxV1@by%R02WOjac8ifDVQa') #insere a senha no imput
    siteLaboratorio.locator('xpath=/html/body/app-root/app-login-feed/div/div[2]/form/button').click() #clica no botão, necessário passar o path do elemento que deve ser clicado
    time.sleep(1.5)
    siteLaboratorio.locator('xpath=/html/body/app-root/app-layout-main/mat-sidenav-container/mat-sidenav/app-layout-main-nav/mat-nav-list/a[3]/div').click() #clica no botão relatos
    time.sleep(1.5)
    siteLaboratorio.locator('xpath=/html/body/app-root/app-layout-main/mat-sidenav-container/mat-sidenav-content/div/app-calibration-list/mat-card/div/div[1]/span/mat-form-field[1]/div/div[1]/div/mat-select/div/div[1]').click() #clica no campo mês
    time.sleep(1.5)
    siteLaboratorio.mouse.wheel(0, -500) #scrolla o mouse para cima (valor negativo para cima, valor positivo para baixo)
    time.sleep(0.5)
    siteLaboratorio.locator('xpath=/html/body/div[3]/div[2]/div/div/mat-option[1]/span').click() #clica em "Todos"
    time.sleep(0.5)
    siteLaboratorio.locator('xpath=/html/body/app-root/app-layout-main/mat-sidenav-container/mat-sidenav-content/div/app-calibration-list/mat-card/div/div[1]/span/mat-form-field[2]/div/div[1]/div/mat-select/div/div[1]').click()
    siteLaboratorio.mouse.wheel(0, -500)
    time.sleep(0.5)
    siteLaboratorio.locator('xpath=/html/body/div[3]/div[3]/div/div/mat-option[1]').click()
    time.sleep(0.5)
    siteLaboratorio.fill('xpath=/html/body/app-root/app-layout-main/mat-sidenav-container/mat-sidenav-content/div/app-calibration-list/mat-card/div/div[1]/mat-form-field/div/div[1]/div/input', '552169361DFF')
    time.sleep(1)
    siteLaboratorio.locator('xpath=/html/body/app-root/app-layout-main/mat-sidenav-container/mat-sidenav-content/div/app-calibration-list/mat-card/div/div[1]/span/button[1]/span/mat-icon').click()
    time.sleep(3)
    siteLaboratorio.locator('xpath=/html/body/app-root/app-layout-main/mat-sidenav-container/mat-sidenav-content/div/app-calibration-list/mat-card/div/table/tbody/tr/td[1]/mat-checkbox/label/div').click()
    # # até o momento:
    # - abriu o navegador e acessou o link
    # - preencheu login e senha
    # - selecionou "todos" nos inputs mês e ano
    # - digitou o SN da sonda e clicou no botão de pesquisar
    time.sleep(6)