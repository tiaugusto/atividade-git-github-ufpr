# Registro real dos comandos executados

Os blocos a seguir foram capturados por execução real de Git no ambiente do laboratório. Saídas compridas podem estar abreviadas. Comandos destrutivos, como `reset --hard`, foram executados **somente em cópia descartável**, jamais no projeto original. O laboratório de dois usuários usa uma central **local** e não um remoto GitHub.

As mensagens de autor nos commits usam identidade demonstrativa, não o e-mail pessoal do aluno. Consulte também `docs/log-dois-usuarios.txt` para a saída completa do cenário de colaboração.

### atividade-git-github-ufpr
```console
$ git init -b main
Initialized empty Git repository in /mnt/data/atividade-git-github-ufpr/.git/
[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git config user.name "Demonstracao Git UFPR"

[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git config user.email demonstracao@example.invalid

[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git status --short
?? README.md
?? app.py
?? dados/
?? src/
[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git add README.md

[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git status --short
A  README.md
?? app.py
?? dados/
?? src/
[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git add .

[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git status --short
A  README.md
A  app.py
A  dados/recados.txt
A  src/__init__.py
[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git commit -m "chore: inicializa o repositorio e programa base"
[main (root-commit) 4907a31] chore: inicializa o repositorio e programa base
 4 files changed, 70 insertions(+)
 create mode 100644 README.md
 create mode 100644 app.py
 create mode 100644 dados/recados.txt
 create mode 100644 src/__init__.py
[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git add src/saudacao.py

[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git commit -m "feat: adiciona saudacao com validacao"
[main 1f83562] feat: adiciona saudacao com validacao
 1 file changed, 5 insertions(+)
 create mode 100644 src/saudacao.py
[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git add .

[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git commit -m "test: inclui testes e roteiro de exercicios"
[main cc0ed5e] test: inclui testes e roteiro de exercicios
 3 files changed, 34 insertions(+)
 create mode 100644 docs/roteiro-do-video.md
 create mode 100644 tests/__init__.py
 create mode 100644 tests/test_saudacao.py
[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git checkout -b feature/calculadora
Switched to a new branch 'feature/calculadora'
[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git add src/calculadora.py

[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git commit -m "feat: implementa funcoes de calculadora em branch"
[feature/calculadora fe81428] feat: implementa funcoes de calculadora em branch
 1 file changed, 6 insertions(+)
 create mode 100644 src/calculadora.py
[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git add .

[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git commit -m "test: valida calculadora antes do merge"
[feature/calculadora 341f548] test: valida calculadora antes do merge
 1 file changed, 14 insertions(+)
 create mode 100644 tests/test_calculadora.py
[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git checkout main
Switched to branch 'main'
[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git merge --no-ff feature/calculadora -m "merge: integra calculadora na main"
Merge made by the 'ort' strategy.
 src/calculadora.py        |  6 ++++++
 tests/test_calculadora.py | 14 ++++++++++++++
 2 files changed, 20 insertions(+)
 create mode 100644 src/calculadora.py
 create mode 100644 tests/test_calculadora.py
[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git checkout -b feature/pull-request
Switched to a new branch 'feature/pull-request'
[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git add .

[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git commit -m "feat: prepara multiplicacao para pull request"
[feature/pull-request f7183ad] feat: prepara multiplicacao para pull request
 2 files changed, 8 insertions(+), 1 deletion(-)
[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ python3 -m unittest discover -s tests -v
test_multiplicar (test_calculadora.TestCalculadora.test_multiplicar) ... ok
test_somar (test_calculadora.TestCalculadora.test_somar) ... ok
test_subtrair (test_calculadora.TestCalculadora.test_subtrair) ... ok
test_nome (test_saudacao.TestSaudacao.test_nome) ... ok
test_vazio (test_saudacao.TestSaudacao.test_vazio) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.002s

OK
[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git checkout main
Switched to branch 'main'
[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git add .gitignore

[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git commit -m "chore: configura gitignore"
[main 8ceee5f] chore: configura gitignore
 1 file changed, 6 insertions(+)
 create mode 100644 .gitignore
[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git status --short

[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git check-ignore -v arquivos_temporarios/senha-local.txt debug.log
.gitignore:6:arquivos_temporarios/	arquivos_temporarios/senha-local.txt
.gitignore:5:*.log	debug.log
[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git add scripts/laboratorio_dois_usuarios.py

[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git commit -m "test: adiciona laboratorio reproduzivel com dois usuarios"
[main ac5be85] test: adiciona laboratorio reproduzivel com dois usuarios
 1 file changed, 98 insertions(+)
 create mode 100644 scripts/laboratorio_dois_usuarios.py
[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git log --oneline --graph --decorate --all
* ac5be85 (HEAD -> main) test: adiciona laboratorio reproduzivel com dois usuarios
* 8ceee5f chore: configura gitignore
| * f7183ad (feature/pull-request) feat: prepara multiplicacao para pull request
|/  
*   3750486 merge: integra calculadora na main
|\  
| * 341f548 (feature/calculadora) test: valida calculadora antes do merge
| * fe81428 feat: implementa funcoes de calculadora em branch
|/  
* cc0ed5e test: inclui testes e roteiro de exercicios
* 1f83562 feat: adiciona saudacao com validacao
* 4907a31 chore: inicializa o repositorio e programa base
[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git branch -a
feature/calculadora
  feature/pull-request
* main
[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ git diff --stat main..feature/pull-request
.gitignore                           |  6 ---
 scripts/laboratorio_dois_usuarios.py | 98 ------------------------------------
 src/calculadora.py                   |  4 ++
 tests/test_calculadora.py            |  5 +-
 4 files changed, 8 insertions(+), 105 deletions(-)
[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ python3 app.py
Ola, UFPR! Bem-vindo ao laboratorio de Git.
[codigo de saida: 0]
```

### atividade-git-github-ufpr
```console
$ python3 -m unittest discover -s tests -v
test_somar (test_calculadora.TestCalculadora.test_somar) ... ok
test_subtrair (test_calculadora.TestCalculadora.test_subtrair) ... ok
test_nome (test_saudacao.TestSaudacao.test_nome) ... ok
test_vazio (test_saudacao.TestSaudacao.test_vazio) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
[codigo de saida: 0]
```

### .
```console
$ git clone --branch main /mnt/data/atividade-git-github-ufpr /mnt/data/_temporary_reset_lab
Cloning into '/mnt/data/_temporary_reset_lab'...
done.
[codigo de saida: 0]
```

### _temporary_reset_lab
```console
$ git config user.name "Usuario Teste"

[codigo de saida: 0]
```

### _temporary_reset_lab
```console
$ git config user.email usuario-teste@example.invalid

[codigo de saida: 0]
```

### _temporary_reset_lab
```console
$ git add arquivo_somente_para_reset.txt

[codigo de saida: 0]
```

### _temporary_reset_lab
```console
$ git commit -m "temp: commit descartavel para reset"
[main c761e99] temp: commit descartavel para reset
 1 file changed, 1 insertion(+)
 create mode 100644 arquivo_somente_para_reset.txt
[codigo de saida: 0]
```

### _temporary_reset_lab
```console
$ git log --oneline -3
c761e99 temp: commit descartavel para reset
ac5be85 test: adiciona laboratorio reproduzivel com dois usuarios
8ceee5f chore: configura gitignore
[codigo de saida: 0]
```

### _temporary_reset_lab
```console
$ git checkout --detach HEAD~1
HEAD is now at ac5be85 test: adiciona laboratorio reproduzivel com dois usuarios
[codigo de saida: 0]
```

### _temporary_reset_lab
```console
$ git checkout main
Previous HEAD position was ac5be85 test: adiciona laboratorio reproduzivel com dois usuarios
Switched to branch 'main'
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)
[codigo de saida: 0]
```

### _temporary_reset_lab
```console
$ git reset --hard HEAD~1
HEAD is now at ac5be85 test: adiciona laboratorio reproduzivel com dois usuarios
[codigo de saida: 0]
```

### _temporary_reset_lab
```console
$ git reflog -5
ac5be85 HEAD@{0}: reset: moving to HEAD~1
c761e99 HEAD@{1}: checkout: moving from ac5be8571ebd335422ceddeb028adea81e6e6ebb to main
ac5be85 HEAD@{2}: checkout: moving from main to HEAD~1
c761e99 HEAD@{3}: commit: temp: commit descartavel para reset
ac5be85 HEAD@{4}: clone: from /mnt/data/atividade-git-github-ufpr
[codigo de saida: 0]
```

### laboratorio de dois usuarios (script executado)
```console
$ python3 scripts/laboratorio_dois_usuarios.py
Laboratorio isolado: /tmp/git-ufpr-u9uilk1p
[git-ufpr-u9uilk1p]$ git clone --bare --single-branch --branch main /mnt/data/atividade-git-github-ufpr /tmp/git-ufpr-u9uilk1p/central.git
Cloning into bare repository '/tmp/git-ufpr-u9uilk1p/central.git'...
done.
[exit=0]
[git-ufpr-u9uilk1p]$ git clone /tmp/git-ufpr-u9uilk1p/central.git usuario_a
Cloning into 'usuario_a'...
done.
[exit=0]
[git-ufpr-u9uilk1p]$ git clone /tmp/git-ufpr-u9uilk1p/central.git usuario_b
Cloning into 'usuario_b'...
done.
[exit=0]
[usuario_a]$ git config user.name Usuario A
[exit=0]
[usuario_a]$ git config user.email usuario-a@example.invalid
[exit=0]
[usuario_b]$ git config user.name Usuario B
[exit=0]
[usuario_b]$ git config user.email usuario-b@example.invalid
[exit=0]
[usuario_a]$ git add dados/aviso_a.txt
[exit=0]
[usuario_a]$ git commit -m docs: usuario A adiciona aviso
[main c56e348] docs: usuario A adiciona aviso
 1 file changed, 1 insertion(+)
 create mode 100644 dados/aviso_a.txt
[exit=0]
[usuario_a]$ git push origin main
To /tmp/git-ufpr-u9uilk1p/central.git
   ac5be85..c56e348  main -> main
[exit=0]
[usuario_b]$ git pull --ff-only origin main
From /tmp/git-ufpr-u9uilk1p/central
 * branch            main       -> FETCH_HEAD
   ac5be85..c56e348  main       -> origin/main
Updating ac5be85..c56e348
Fast-forward
 dados/aviso_a.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 dados/aviso_a.txt
[exit=0]
[usuario_b]$ git add dados/aviso_b.txt
[exit=0]
[usuario_b]$ git commit -m docs: usuario B adiciona aviso
[main 0204956] docs: usuario B adiciona aviso
 1 file changed, 1 insertion(+)
 create mode 100644 dados/aviso_b.txt
[exit=0]
[usuario_b]$ git push origin main
To /tmp/git-ufpr-u9uilk1p/central.git
   c56e348..0204956  main -> main
[exit=0]
[usuario_a]$ git pull --ff-only origin main
From /tmp/git-ufpr-u9uilk1p/central
 * branch            main       -> FETCH_HEAD
   c56e348..0204956  main       -> origin/main
Updating c56e348..0204956
Fast-forward
 dados/aviso_b.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 dados/aviso_b.txt
[exit=0]
[usuario_a]$ git add dados/recados.txt
[exit=0]
[usuario_a]$ git commit -m docs: usuario A edita recado
[main f404532] docs: usuario A edita recado
 1 file changed, 1 insertion(+), 1 deletion(-)
[exit=0]
[usuario_a]$ git push origin main
To /tmp/git-ufpr-u9uilk1p/central.git
   0204956..f404532  main -> main
[exit=0]
[usuario_b]$ git add dados/recados.txt
[exit=0]
[usuario_b]$ git commit -m docs: usuario B edita o mesmo recado
[main 0fa0521] docs: usuario B edita o mesmo recado
 1 file changed, 1 insertion(+), 1 deletion(-)
[exit=0]
[usuario_b]$ git push origin main
To /tmp/git-ufpr-u9uilk1p/central.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to '/tmp/git-ufpr-u9uilk1p/central.git'
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
[exit=1]
[usuario_b]$ git pull --no-rebase origin main
From /tmp/git-ufpr-u9uilk1p/central
 * branch            main       -> FETCH_HEAD
   0204956..f404532  main       -> origin/main
Auto-merging dados/recados.txt
CONFLICT (content): Merge conflict in dados/recados.txt
Automatic merge failed; fix conflicts and then commit the result.
[exit=1]
[usuario_b]$ git status --short
UU dados/recados.txt
[exit=0]
[usuario_b]$ git add dados/recados.txt
[exit=0]
[usuario_b]$ git commit -m merge: resolve conflito entre usuarios A e B
[main 8b79536] merge: resolve conflito entre usuarios A e B
[exit=0]
[usuario_b]$ git push origin main
To /tmp/git-ufpr-u9uilk1p/central.git
   f404532..8b79536  main -> main
[exit=0]
[usuario_a]$ git pull --ff-only origin main
From /tmp/git-ufpr-u9uilk1p/central
 * branch            main       -> FETCH_HEAD
   f404532..8b79536  main       -> origin/main
Updating f404532..8b79536
Fast-forward
 dados/recados.txt | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
[exit=0]
[usuario_a]$ git log --oneline --graph -8
*   8b79536 merge: resolve conflito entre usuarios A e B
|\  
| * f404532 docs: usuario A edita recado
* | 0fa0521 docs: usuario B edita o mesmo recado
|/  
* 0204956 docs: usuario B adiciona aviso
* c56e348 docs: usuario A adiciona aviso
* ac5be85 test: adiciona laboratorio reproduzivel com dois usuarios
* 8ceee5f chore: configura gitignore
*   3750486 merge: integra calculadora na main
|\
[exit=0]
RESULTADO: colaboracao e conflito resolvidos com sucesso.
[usuario_b]$ git bundle create /mnt/data/atividade-git-github-ufpr/arquivos_temporarios/laboratorio-remoto.bundle --all
[exit=0]
Bundle de auditoria: /mnt/data/atividade-git-github-ufpr/arquivos_temporarios/laboratorio-remoto.bundle

```
