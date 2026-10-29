# Scroll e retenção

**CIN0055 — Tendências em Mídia e Interação · Movimento 3 · `alpa2`**
Tema: Bem-estar digital e design de fricção

## Como abrir

https://aarthuralvees.github.io/experimento-midias/

Abre no navegador do celular, sem instalar nada e sem login. São cerca de 12 minutos: até 5 de
uso, 3 de perguntas e o resto de conversa. Funciona com qualquer número de pessoas.

---

## 1. O que é

Um feed de posts curtos de curiosidades. Cada pessoa recebe um número, abre a página e rola o
feed por até 5 minutos, do jeito que usaria o seu. Depois responde quatro perguntas rápidas sobre
o que viu.

O número define a versão que ela usa, sem que ela saiba:

| versão | o que acontece |
|---|---|
| **A — scroll livre** | o feed corre sem nenhum aviso |
| **B — com pausas** | a cada 15 posts, uma tela de pausa de 6 segundos antes de continuar |

As perguntas depois do feed são, nesta ordem:

1. Quantos posts você acha que viu?
2. Do que você lembra? (texto livre, até 4 posts)
3. Você ficou mais, igual ou menos tempo do que gostaria?
4. Marque os posts que você viu. A lista mistura 8 posts que a pessoa viu de fato (espalhados ao
   longo da sessão) com 8 que não chegaram a aparecer. Cada opção é só o assunto ("Um post sobre
   polvos"), sem imagem, para que lembrar dependa de ter prestado atenção.

A tela final mostra o resultado (posts vistos, estimativa, reconhecidos e falsos marcados) e
revela qual versão a pessoa teve.

## 2. A pergunta sobre o futuro

Se pausas e limites virarem obrigação legal (ECA Digital, DSA, acordo da Meta) e a métrica de bem-estar deixar de ser o tempo de tela, o que passa a importar é o que a pessoa realmente retém do que consome. Pergunta: uma pausa embutida no feed faz a pessoa reter mais do que o scroll livre, ou ela só espera o contador acabar? Isso toca as disrupções 1 e 3 do meu mapa.

## 3. A tecnologia emergente

Usei IA generativa para produzir 202 posts curtos, numa quantidade e variedade que eu não escreveria à mão a tempo, para que ninguém acabe o feed em 5 minutos. A IA entra na construção, não ao vivo: os posts foram gerados uma vez e estão dentro da página. Um feed real não serve porque eu não saberia o que cada pessoa viu, e sem isso não dá para medir o que ela reteve. Um feed finito e fixo acabaria cedo ou seria igual para todos. O limite é que não testo a geração em tempo real, nem o efeito de vídeo e imagem.

## 4. Como usar

**Sozinho, para entender:** abra a página, digite um número ímpar (versão A) ou par (versão B)
e siga. Depois tente o outro.

**Com um grupo:**

1. Mande o link. **Não explique as versões nem diga que haverá perguntas de memória.**
2. Cada pessoa digita o número que você deu. Qualquer quantidade serve.
3. Diga só: "use como usaria o seu feed. Pode parar quando quiser."
4. Você **observa e não conduz**: quem para cedo, quem dispensa a pausa sem ler, quem olha para
   o celular do colega. Anote.
5. Quando todos tiverem terminado, **revele as duas versões** e abra a conversa:
   - Quem teve pausa? Você leu a tela ou só esperou?
   - Quem lembrou mais do que esperava? E menos?
   - Quantos posts você achou que viu, e quantos a página contou?

**Parâmetros de teste** (opcionais, na URL): `?c=A` ou `?c=B` força a versão, `?t=30` encurta o
feed para 30 s, `?p=5` pausa a cada 5 posts, `?ps=2` pausa de 2 s.

## 5. O que eu espero que aconteça

Espero que a versão com pausas retenha um pouco mais, mas com efeito pequeno, e que várias pessoas só esperem o contador. Espero também que a maioria erre a estimativa de posts vistos e marque alguns que não viu. Se as pausas não mudarem nada, o meu mapa perde força na ideia de que a fricção exigida por lei melhora o uso. O que eu não espero, mas pode acontecer: quem teve pausa lembrar menos.

## O que há neste repositório

| arquivo | o que é |
|---|---|
| `index.html` | o experimento. Página única, os posts estão dentro dela |
| `cards.txt` | os 202 posts (emoji, assunto, título, texto, categoria) |
| `template.html` | a página sem os posts |
| `build.py` | junta `template.html` e `cards.txt` em `index.html` |
| `apps_script.gs` | recebe as respostas numa planilha do Google (opcional) |

## O que este experimento não mede

- Não mede a geração de conteúdo em tempo real (ver seção 3).
- Não é estatística: com cerca de 14 pessoas, serve para observar padrões e surpresas, não para
  concluir.
- Os posts são só texto e emoji, sem vídeo nem imagem. Um feed real prende por outros meios.
- "Visto" significa que o post ficou **pelo menos 0,7 s inteiro na tela**. Passar rápido demais
  por um post não o conta, e ele nem entra na pergunta de reconhecimento.
- Na versão B o tempo das pausas **não conta** nos 5 minutos de uso. As duas versões têm o mesmo
  tempo de feed, mas B dura mais no relógio.
- As iscas da pergunta 4 são posts da própria reserva que a pessoa não chegou a alcançar. Se ela
  viu quase tudo, entram assuntos de uma lista reserva.

## Privacidade

A página não pede nome, e-mail nem qualquer dado pessoal. Registra o número que a pessoa digitou,
a versão, contagens, tempos e as respostas das quatro perguntas (incluindo o texto livre, que pode
ser lido por quem conduz). Nada é enviado a menos que o `ENDPOINT` seja configurado. Sem ele, o
resultado fica só no navegador da pessoa.


## Publicar (GitHub Pages)

1. Crie um repositório **público** no GitHub.
2. Suba `index.html` e `README.md` (e os demais arquivos, se quiser).
3. **Settings → Pages → Build and deployment → Deploy from a branch → `main` / `(root)`.**
4. Em um ou dois minutos o link `https://SEU-USUARIO.github.io/SEU-REPO/` fica no ar. É esse o
   link para colar na página da disciplina e mandar no grupo.
5. Abra o link **no celular** e faça um teste inteiro antes de divulgar.

## `REGISTRO.md`

Três partes, e uma linha final:

1. O que a turma fez que você não esperava.
2. O que você mudou por causa disso.
3. O que decidiu não mudar, e por quê.
4. Uma linha: a pergunta sobre o futuro ficou mais clara, mais confusa, ou mudou?
