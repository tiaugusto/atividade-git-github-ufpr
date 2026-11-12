# Comandos utilizados

## Repositório e commits

```bash
git init -b main
git status
git add README.md
git add .
git commit -m "chore: inicializa o repositorio e programa base"
git remote add origin https://github.com/tiaugusto/atividade-git-github-ufpr.git
git push -u origin main
```

## Histórico e versões

```bash
git log --oneline --graph --decorate --all
git reflog -5
git checkout --detach HEAD~1
git checkout main
git reset --hard HEAD~1
```

O `reset --hard` foi feito em uma cópia temporária.

## Branches e merge

```bash
git checkout -b feature/calculadora
git add .
git commit -m "feat: implementa funcoes de calculadora em branch"
git checkout main
git merge --no-ff feature/calculadora
git checkout -b feature/pull-request
git add .
git commit -m "feat: prepara multiplicacao para pull request"
git push -u origin feature/pull-request
```

[Pull request #1](https://github.com/tiaugusto/atividade-git-github-ufpr/pull/1)

## Dois usuários

O exercício foi feito com dois clones locais de um repositório remoto.

```bash
git clone central.git usuario_a
git clone central.git usuario_b
git pull --ff-only origin main
git push origin main
git pull --no-rebase origin main
git status
git add dados/recados.txt
git commit -m "merge: resolve conflito entre usuarios A e B"
git push origin main
```

## .gitignore

```bash
git check-ignore -v arquivos_temporarios/senha-local.txt debug.log
```
