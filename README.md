# Consulta Médica  
````  
  
  
Relatório de produção médica   
  
## Como desenvolver?  
  
1. clone o respositório.  
2. crie um virtualenv com Python 3.6.  
3. Ative o virtualenv.  
4. Instale as dependências.  
5. Configure a instância .env  
6. Execute os testes.  
  
```console  
git clone git@github.com:lffsantos/consulta_medica.git consulta_medica  
cd consulta_medica  
python -m venv .venv 
source .venv/bin/activate  
pip install -r requirements-dev.txt  
cp contrib/env-sample .env  
python manage.py test  
```  