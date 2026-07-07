import requests

# Teste de requisição GET
avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/') 

# Acessamdpo o status code da resposta
#print(avaliacoes.status_code)

# Acessando o conteúdo da resposta
# print(avaliacoes.json())
# Verificando o tipo do conteúdo da resposta
# print(type(avaliacoes.json())) 
 

# Acessando a quantidade de avaliações retornadas
# print(len(avaliacoes.json()))

headers = {'Authorization': 'Token 954110760c4d8d6259bcce8cac46212f5ebecebd'}

cursos = requests.get('http://localhost:8000/api/v2/cursos/', headers=headers)

print(cursos.status_code)
print(cursos.json())