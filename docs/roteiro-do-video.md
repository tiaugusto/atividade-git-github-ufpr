# Roteiro por capítulo (vídeo Dev Aprender)

Fonte: https://www.youtube.com/watch?v=kB5e-gTAl_s

Os horários abaixo correspondem aos capítulos publicados na descrição do vídeo. São exercícios **equivalentes**, usando nosso próprio miniprojeto, não uma transcrição literal da tela do instrutor.

1. **07:55 — Inicializar repositório:** `git init -b main`, depois `git status`.
2. **11:00 — Arquivos em staging:** `git add README.md`, depois `git add .`.
3. **13:22 — Salvar versão:** `git commit -m "..."`.
4. **15:30 — Repositório remoto:** `git remote`, `git push -u ...` no laboratório local; GitHub em etapa separada.
5. **20:24 — Atualização:** alterar função, `git status`, `git add`, `git commit`, `git push`.
6. **22:32 — Histórico:** `git log --oneline`, `git reflog`.
7. **23:08 — Voltar versões:** `git checkout --detach <commit>`; `git reset --hard HEAD~1` apenas em clone descartável.
8. **26:01 — Branches:** `git branch`, `git checkout -b feature/calculadora`.
9. **33:39 — Merge:** `git merge --no-ff feature/calculadora` na `main`.
10. **41:09 — Pull request:** branch isolada `feature/pull-request`, teste e comparação `git diff`; abrir PR no GitHub após a publicação.
11. **45:51 — `.gitignore`:** criar arquivo e verificar com `git check-ignore -v`.

**Nota sobre `main` versus `master`:** o curso pode usar `master` em exemplos; este projeto usa `main`, nome padrão comum em projetos novos. Os comandos têm a mesma finalidade.
