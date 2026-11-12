def saudacao(nome: str) -> str:
    """Devolve uma saudação simples para o exemplo do curso."""
    if not nome.strip():
        raise ValueError('O nome nao pode ser vazio')
    return f'Ola, {nome}! Bem-vindo ao laboratorio de Git.'
