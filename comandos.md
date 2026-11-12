# Comandos Git

## Início

```bash
git init
git status
git add .
git commit -m "Primeiro commit"
git remote add origin https://github.com/tiaugusto/atividade-git-github-ufpr.git
git push -u origin main
```

## Histórico

```bash
git log --oneline --graph --all
git reflog
git checkout <hash-do-commit>
git checkout main
git reset --hard HEAD~1
```

## Branches

```bash
git branch exemplo
git checkout exemplo
git add .
git commit -m "Exemplo em outra branch"
git checkout main
git merge exemplo
git branch -d exemplo
```

## Repositório remoto e dois usuários

```bash
git clone https://github.com/tiaugusto/atividade-git-github-ufpr.git usuario_a
git clone https://github.com/tiaugusto/atividade-git-github-ufpr.git usuario_b
git pull origin main
git push origin main
```

## Arquivos ignorados

```bash
git status
git check-ignore -v debug.log
```

Pull requests são criados e revisados na aba **Pull requests** do GitHub.
