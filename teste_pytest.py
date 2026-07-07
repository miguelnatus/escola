import requests

class TestCursos:
    headers = {
        'Authorization': 'Token 54fd92c6958f119cd11d5c2e5beb70617a77d2e8'
    }
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        cursos = requests.get(self.url_base_cursos, headers=self.headers)
        assert cursos.status_code == 200
        assert len(cursos.json()) > 0

    def test_get_curso(self):
        curso = requests.get(f'{self.url_base_cursos}2/', headers=self.headers)
        assert curso.status_code == 200
        assert curso.json()['id'] == 2

    def test_post_curso(self):
        novo_curso = {
            'titulo': 'Curso de Teste',
            'url': 'http://www.cursodeteste.com/curso-de-teste'
        }
        curso = requests.post(self.url_base_cursos, headers=self.headers, data=novo_curso)
        assert curso.status_code == 201
        assert curso.json()['titulo'] == novo_curso['titulo']

    def test_put_curso(self):
        curso_atualizado = {
            'titulo': 'Curso de Teste Atualizado',
            'url': 'http://www.cursodetesteatualizado.com'
        }
        curso = requests.put(f'{self.url_base_cursos}2/', headers=self.headers, data=curso_atualizado)
        assert curso.status_code == 200
        assert curso.json()['titulo'] == curso_atualizado['titulo'] 

    def test_delete_curso(self):
        curso = requests.delete(f'{self.url_base_cursos}2/', headers=self.headers)
        assert curso.status_code == 204 and len(curso.text) == 0
    