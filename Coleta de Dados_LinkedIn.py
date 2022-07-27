# -*- coding: utf-8 -*-
## 1. Todas as importações
from selenium import webdriver
from time import sleep 

## 2. Todos os parâmetros
URL_LINKEDIN_DS = 'https://www.linkedin.com/jobs/ci%C3%AAncia-de-dados-vagas/?originalSubdomain=br'


## 3. Execução do código
if __name__ == '__main__':
    # Criar uma instância do Google Chrome pelo Selenium
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    
    # Acesar a URL do LinkedIn
    driver.get(URL_LINKEDIN_DS)
    
    # Pegar lista de resultados de vagas de DS
    resultados = driver.find_elements_by_class_name('result-card')
    lista_descricao = []    
       
    # Iniciar While loop em cima de todos os resultados
    while True:
        # For loop para coletar descrições de dados 
        for r in resultados[len(lista_descricao):]:
            r.click()  # Clicar na descrição 
            sleep(1)  # Dormir por um minuto após o click
            try:
                # Pegar elemento com a descrição
                descricao = driver.find_element_by_class_name('description')
                # Anexar o texto na lista 
                lista_descricao.append(descricao.text)
            except:
                print('Erro')
                pass
        
        resultados = driver.find_elements_by_class_name('result-card') 
                    
       # Critério de saída do While  
        if len(lista_descricao) > 25:
            break
             
    # Salvar descrições de vagas 
    descricao_salvar = '\n'.join(lista_descricao)
    print(descricao_salvar)
    with open('descricoes_vagas.txt','w', encoding='utf-8') as f:
        f.write(descricao_salvar)
    
    # Fechar o Google Chrome 
    driver.quit()
    

