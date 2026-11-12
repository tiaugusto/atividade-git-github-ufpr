#!/usr/bin/env python3
"""Demonstra dois colaboradores com clone, push, pull, conflito e resolucao.

Executa tudo em diretorio temporario; NUNCA altera a working tree original.
Exemplo: python3 scripts/laboratorio_dois_usuarios.py
"""
from pathlib import Path
import subprocess
import tempfile
import shutil
import os
import sys

REPO = Path(__file__).resolve().parents[1]


def run(args, cwd):
    cmd = ' '.join(args)
    print(f'[{cwd.name}]$ {cmd}', flush=True)
    p = subprocess.run(args, cwd=cwd, text=True, stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT, env={**os.environ, 'GIT_TERMINAL_PROMPT': '0'})
    if p.stdout.strip():
        print(p.stdout.strip(), flush=True)
    print(f'[exit={p.returncode}]', flush=True)
    return p.returncode


def need(args, cwd):
    code = run(args, cwd)
    if code != 0:
        raise RuntimeError(f'Comando falhou: {args}')


def put(path, content):
    path.write_text(content, encoding='utf-8')


def main():
    base = Path(tempfile.mkdtemp(prefix='git-ufpr-'))
    print(f'Laboratorio isolado: {base}', flush=True)
    try:
        central = base / 'central.git'
        # Clonar apenas a main preserva o trabalho do projeto principal
        need(['git', 'clone', '--bare', '--single-branch', '--branch', 'main', str(REPO), str(central)], base)
        need(['git', 'clone', str(central), 'usuario_a'], base)
        need(['git', 'clone', str(central), 'usuario_b'], base)
        a, b = base/'usuario_a', base/'usuario_b'
        for path, name, email in [(a, 'Usuario A', 'usuario-a@example.invalid'),
                                   (b, 'Usuario B', 'usuario-b@example.invalid')]:
            need(['git', 'config', 'user.name', name], path)
            need(['git', 'config', 'user.email', email], path)

        # Primeiro ciclo sem conflito: A publica; B atualiza; B publica; A atualiza
        put(a/'dados'/'aviso_a.txt', 'Arquivo criado pelo usuario A\n')
        need(['git', 'add', 'dados/aviso_a.txt'], a)
        need(['git', 'commit', '-m', 'docs: usuario A adiciona aviso'], a)
        need(['git', 'push', 'origin', 'main'], a)
        need(['git', 'pull', '--ff-only', 'origin', 'main'], b)
        put(b/'dados'/'aviso_b.txt', 'Arquivo criado pelo usuario B\n')
        need(['git', 'add', 'dados/aviso_b.txt'], b)
        need(['git', 'commit', '-m', 'docs: usuario B adiciona aviso'], b)
        need(['git', 'push', 'origin', 'main'], b)
        need(['git', 'pull', '--ff-only', 'origin', 'main'], a)

        # Conflito verdadeiro: duas pessoas editam a mesma linha da mesma base
        put(a/'dados'/'recados.txt', 'mensagem=Alteracao do usuario A\n')
        need(['git', 'add', 'dados/recados.txt'], a)
        need(['git', 'commit', '-m', 'docs: usuario A edita recado'], a)
        need(['git', 'push', 'origin', 'main'], a)
        put(b/'dados'/'recados.txt', 'mensagem=Alteracao do usuario B\n')
        need(['git', 'add', 'dados/recados.txt'], b)
        need(['git', 'commit', '-m', 'docs: usuario B edita o mesmo recado'], b)
        code = run(['git', 'push', 'origin', 'main'], b)
        if code == 0:
            raise RuntimeError('Era esperado push rejeitado (non-fast-forward)')
        code = run(['git', 'pull', '--no-rebase', 'origin', 'main'], b)
        if code == 0:
            raise RuntimeError('Era esperado conflito de merge')
        need(['git', 'status', '--short'], b)
        put(b/'dados'/'recados.txt', 'mensagem=Alteracoes conciliadas: usuarios A e B\n')
        need(['git', 'add', 'dados/recados.txt'], b)
        need(['git', 'commit', '-m', 'merge: resolve conflito entre usuarios A e B'], b)
        need(['git', 'push', 'origin', 'main'], b)
        need(['git', 'pull', '--ff-only', 'origin', 'main'], a)
        need(['git', 'log', '--oneline', '--graph', '-8'], a)
        print('RESULTADO: colaboracao e conflito resolvidos com sucesso.', flush=True)
        # Salva um bundle com todos os commits do laboratorio, para auditoria
        bundle = REPO / 'arquivos_temporarios' / 'laboratorio-remoto.bundle'
        bundle.parent.mkdir(exist_ok=True)
        need(['git', 'bundle', 'create', str(bundle), '--all'], b)
        print(f'Bundle de auditoria: {bundle}', flush=True)
        return 0
    finally:
        shutil.rmtree(base)


if __name__ == '__main__':
    sys.exit(main())
