# Prática de Git e GitHub — UFPR

Repositório didático para exercitar os exemplos do vídeo **Curso de Git e Github COMPLETO 2025 [Iniciantes] + Desafios + Muita Prática**, do canal Dev Aprender (Jhonatan de Souza).

**Vídeo:** https://www.youtube.com/watch?v=kB5e-gTAl_s

## Objetivo

Mostrar, com um pequeno projeto Python, a sequência real de comandos Git, commits, branches, merge, histórico, mudança de versão, `.gitignore` e colaboração de dois usuários. O código é propositalmente simples: o foco da atividade é o **controle de versão**.

## Experimentos documentados

| Tempo no vídeo | Tema | Onde está a evidência |
| --- | --- | --- |
| 07:55 | `git init` | `docs/registro-de-comandos.md` |
| 11:00 | `git status`, `git add arquivo`, `git add .` | registro + commits |
| 13:22 | `git commit` | histórico do repositório |
| 15:30 | `git push` | `docs/experimento-dois-usuarios.md` + registro (remoto local) |
| 20:24 | ciclo de alterações | commits e registro |
| 22:32 | `git log` / `git reflog` | registro |
| 23:08 | navegar entre versões / `reset` | registro, em cópia descartável |
| 26:01 | branches / `checkout` | branches `feature/calculadora`, `feature/pull-request` |
| 33:39 | `git merge` | merge registrado no histórico |
| 41:09 | pull request | branch `feature/pull-request`, pronta para PR no GitHub |
| 45:51 | `.gitignore` | `.gitignore` + `git check-ignore` no registro |

**Importante:** push/pull de dois usuários foram executados contra um **repositório remoto Git local** (bare), não contra o GitHub. Para completar a atividade na plataforma, publique o repositório e abra o pull request conforme `docs/publicar-no-github.md`. Não há alegação de que um PR no GitHub já foi criado.

## Testar o programa

```bash
python3 app.py
python3 -m unittest discover -s tests -v
```

## Explorar os comandos

```bash
git status
git log --oneline --graph --decorate --all
git branch -a
git show feature/calculadora
git diff main..feature/pull-request
```

## Estrutura

- `app.py`: pequeno aplicativo demonstrativo.
- `src/`: funções adicionadas e evoluídas via commits e branches.
- `tests/`: testes com biblioteca padrão do Python.
- `dados/`: arquivo usado no laboratório com dois usuários.
- `docs/roteiro-do-video.md`: correspondência entre o curso e a prática.
- `docs/registro-de-comandos.md`: registro de comandos executados e saídas.
- `docs/experimento-dois-usuarios.md`: colaboração, push rejeitado e resolução de conflito.
- `evidencias/historico-dois-usuarios.bundle`: histórico auditável da simulação dos dois colaboradores.
- `docs/publicar-no-github.md`: como publicar e obter o link para a UFPR.
- `scripts/laboratorio_dois_usuarios.py`: script repetível, com dois diretórios.

## Autenticidade das evidências

O histórico Git e os comandos de terminal deste pacote foram **gerados por execução real** no ambiente de preparação. O repositório tem uma identidade Git demonstrativa (`Demonstracao Git UFPR`, `demonstracao@example.invalid`), não a identidade pessoal de quem vai entregar. A publicação no GitHub e o PR remoto precisam ser concluídos na conta do estudante.
