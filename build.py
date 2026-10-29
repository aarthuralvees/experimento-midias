"""Monta index.html a partir de template.html e cards.txt.

Uso:  python build.py
Formato de cada linha de cards.txt:  emoji|tema|título|texto|categoria
O "tema" é o rótulo usado nas opções da pergunta de reconhecimento
("Um post sobre <tema>") e precisa ser único.
"""
import json
import pathlib
import sys

AQUI = pathlib.Path(__file__).resolve().parent

# Temas que NÃO aparecem em nenhum card. Só entram como isca se faltarem
# posts não alcançados (caso extremo: a pessoa viu quase tudo).
RESERVA = ["zebras", "girassóis", "aurora boreal", "bambu", "pandas", "iglus", "sorvete",
           "faróis", "pirarucu", "cerâmica", "moinhos de vento", "fósseis", "lagostas",
           "xilofone", "paraquedas", "origami", "mamutes", "tapioca", "cavalos-marinhos",
           "canoas"]


def main():
    cards, vistos = [], set()
    for n, linha in enumerate((AQUI / "cards.txt").read_text(encoding="utf-8").splitlines(), 1):
        if not linha.strip():
            continue
        campos = linha.split("|")
        if len(campos) != 5:
            sys.exit(f"cards.txt linha {n}: esperava 5 campos, achei {len(campos)}")
        e, t, h, b, c = [x.strip() for x in campos]
        if t in vistos:
            sys.exit(f"cards.txt linha {n}: tema repetido: {t}")
        vistos.add(t)
        cards.append({"e": e, "t": t, "h": h, "b": b, "c": c})
    colide = [r for r in RESERVA if r in vistos]
    if colide:
        sys.exit(f"temas da reserva que também são cards: {colide}")
    html = (AQUI / "template.html").read_text(encoding="utf-8")
    html = html.replace("__CARDS__", json.dumps(cards, ensure_ascii=False))
    html = html.replace("__RESERVA__", json.dumps(RESERVA, ensure_ascii=False))
    (AQUI / "index.html").write_text(html, encoding="utf-8")
    print(f"index.html: {len(cards)} cards, {len(html)/1024:.0f} KB")


if __name__ == "__main__":
    main()
