#  Pipeline de Testes no GitHub Actions  

```yaml
name: Run Selenium Tests  
on: [push]  
jobs:  
  test:  
    runs-on: ubuntu-latest  
    steps:  
      - uses: actions/checkout@v2  
      - name: Run Python Script  
        run: python projetos-automacao/selenium-python/test_login.py  
