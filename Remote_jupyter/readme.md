# Conectar na VM usando o Spark e jupyter notebook.

1. Primeiro precisa gerar uma cfg file do jupyter na VM Linux, no meu caso foi o CentOS
```
$ jupyter notebook --generate-config
```
2. edita o arquivo com o vi e acrescenta 2 linhas:
c.NotebookApp.allow_origin = '*'
c.NotebookApp.ip = '0.0.0.0'
3. cria uma senha pro jupyter
```
$ jupyter notebook password
```
4. abre a porta no firewall
```
$ sudo ufw allow 8888
```
ou
```
$sudo firewall-cmd --zone=public --permanent --add-port=8888/tcp
```
5. vai na pasta do spark ( no meu caso foi /opt/spark) digita esse comando:
```
$ PYSPARK_DRIVER_PYTHON=jupyter PYSPARK_DRIVER_PYTHON_OPTS=notebook ./bin/pyspark
```
6. abre o browser e digita seuip:8888 (meu caso foi 192.168.1.5:888)

e poe a senha que você criou no Jupiter notebook.
