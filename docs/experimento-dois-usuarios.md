# Experimento de colaboração: dois usuários

Este experimento **foi executado** com dois clones diferentes (`usuario_a/` e `usuario_b/`) e um repositório bare (`central.git`) funcionando como servidor remoto local. Ambos ficam em pasta temporária, sem interferir nos arquivos do projeto principal. O script recria tudo automaticamente.

```bash
python3 scripts/laboratorio_dois_usuarios.py
```

## O que foi reproduzido

1. Criação de remoto Git local com `git clone --bare`.
2. Clone do mesmo remoto em duas pastas: `usuario_a` e `usuario_b`.
3. Usuário A cria um arquivo, faz `git add`, `git commit` e `git push origin main`.
4. Usuário B executa `git pull --ff-only`, cria outro arquivo e publica com `git push`.
5. Usuário A recebe as alterações com `git pull --ff-only`.
6. Ambos editam a **mesma linha** de `dados/recados.txt` sem atualizar a cópia de B antes de seu próprio commit.
7. Push do usuário B é **rejeitado** (`non-fast-forward`).
8. `git pull --no-rebase origin main` causa conflito de merge esperado.
9. Usuário B resolve a linha manualmente, faz `git add`, `git commit` e `git push`.
10. Usuário A executa `git pull --ff-only` e obtém a solução.

A saída integral dessa simulação foi capturada no arquivo `docs/log-dois-usuarios.txt`. Há um arquivo Git bundle dentro de `arquivos_temporarios/` em cada execução do script, ignorado pelo Git; ele permite auditar o histórico do remoto simulado localmente.

## Observação importante

Esse experimento demonstra **sem usar GitHub** a semântica de `clone`, `push`, `pull`, sincronização de branches e resolução de conflito. Para satisfazer a exigência de um **link público visível**, ainda é necessário publicar este repositório no GitHub.
