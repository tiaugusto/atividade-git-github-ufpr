# Publicação final no GitHub (etapa a realizar na sua conta)

O pacote já inclui histórico de commits e duas branches úteis: `main` e `feature/pull-request`. Não há, porém, um repositório GitHub publicado automaticamente nem pull request remoto aberto.

## 1. Criar repositório vazio

No GitHub, crie um repositório **público** com o nome `atividade-git-github-ufpr`, **sem selecionar README, .gitignore ou licença**. O histórico local já inclui esses arquivos.

## 2. Publicar o histórico existente

Abra o terminal **dentro da pasta extraída** (ela deve conter a pasta escondida `.git`) e execute:

```bash
git status
git remote -v
git remote add origin https://github.com/tiaugusto/atividade-git-github-ufpr.git
git push -u origin main
git push -u origin feature/pull-request
git push origin feature/calculadora
```

O endereço acima usa o login GitHub `tiaugusto`. Verifique se está publicando nessa mesma conta. Se o GitHub pedir credenciais, autentique via navegador, Git Credential Manager ou GitHub CLI; senha normal não funciona para operações HTTPS autenticadas.

Se `origin` já existir por algum ajuste anterior, confira a URL com `git remote -v` e altere-a conscientemente com `git remote set-url origin ...`, em vez de adicioná-lo novamente.

**Não** use o botão de upload de arquivos da interface como substituto para `git push`: isso não preserva todos os commits/branches criados no laboratório.

## 3. Abrir um pull request

No GitHub, acesse **Pull requests** → **New pull request**. Selecione:

- **base:** `main`
- **compare:** `feature/pull-request`
- **título sugerido:** `feat: adicionar multiplicação à calculadora`

A branch altera `src/calculadora.py` e amplia `tests/test_calculadora.py`. Ela foi intencionalmente mantida fora da `main`, para que a comparação não fique vazia.

Não precisa realizar merge imediatamente; o PR aberto já demonstra o fluxo de revisão. Se fizer merge, o histórico mostrará essa integração adicional.

## 4. Conferência e entrega

Veja se o projeto está público (ou se a professora recebeu acesso explícito, caso privado), se o histórico tem vários commits, se existem as branches e se `docs/registro-de-comandos.md` é legível. Abra a URL em janela anônima para verificar a permissão de visualização.

Cole no UFPR Virtual:

```
https://github.com/tiaugusto/atividade-git-github-ufpr
```

Opcionalmente inclua também a URL de `pull/1` (ou o número real exibido pelo GitHub após abrir o PR).
