---
layout: post
title: Usando Equações em Markdown
author: Agostinho Brito
tag:
  - equacoes
  - LaTeX
mathjax: true
---
# CSMRD
Contagem de Subconjuntos de Módulos com Restrição de Depencia.

## Contexto Geral
O ERP é uma categoria de software fundamental para todo tipo de organização, pois ele é responsável por gerenciar todas as informações da empresa. Organizações maiores tem recursos financeiros para investir em ERPs customizados para suas atividades, já organizações menores optam por sistemas de partilheira que possuem funcionalidades genéricas do seu ramo de atividade. A customização é uma solução cara tornando o produto não viável para organizações menores, por outro lado, sistemas de partilheira são menos onerosas mas são genéricos e muitas vezes não satisfazem as necessidades específicas dos clientes.
Devido a esse cenário, surgem no mercado sistemas ERPs organizados em módulos. Dessa forma a empresa pode contratar uma consultoria especializada em um desses sistemas, que junto com cliente irá selecionar uma combinação de módulos que melhor se adequa às necessidades do cliente.

## Contexto Específico
O sistema Odoo é uma solução ERP Open Source que possui uma comunidade internacional que desenvolvem módulos para finalidades específicas. Os módulos abertos disponíveis nessa comunidade podem ser usados comercialmente por qualquer pessoa ou empresa para uso próprio ou de seus clientes. Um dos desafios dos desenvolvedores de soluções em Odoo é encontrar uma seleção de módulos que suprem os requisitos cliente, reduzindo o custo de implementação de módulos novos.

## Primeiro Problema:
Atualmente existem centenas de módulos oficiais e milhares de módulos Open Source que podem ser combinados para compor uma solução Odoo. Dado um conjunto de módulos M e o conjunto de dependências D, buscamos todos os subconjuntos válidos V. Um subconjunto válido é o subconjunto em que todas as dependências relacionadas aos seus módulos são satisfeitas dentro do próprio subconjunto. Ou seja, se o módulo m está no subconjunto, as dependências de m também deve estar.

Exemplo:
A notação m : (d1, d2, ...) representa as dependências do módulo m.

$$ D_1 = \emptyset \\
   D_2 = \emptyset \\
   D_3 = \{ m_1, m_2 \} \\
   D_4 = \{ m_4 \} \\
   D_5 = \{ m_2 \} \\
   D_6 = \{ m_5, m_3 \} \\

$$

O conjunto {1, 2, 3} é um subconjunto válido, pois 1 e 2 não tem dependências e as depencias de 3 estão no subconjunto. Já o subconjunto {6, 2} não é válido, pois as dependências do 6 não estão no subconjunto.

## Segundo problema:
Agora podemos chamar cada subconjunto encontrado no problema anterior de template. Cada template satisfaz um conjunto de requisitos. Dado um conjunto de templates T, buscamos uma arvore binária A, em que cada nó possui como valor um requisito r (o mesmo requisito pode estar mais de um nó), e as folhas são templates. Cada nó possui duas sub-árvores filhas. Para cada nó, todos os templates pertencentes à sub-árvore esquerda, são templates que não contém o requisito representado por aquele nó. E os templates da sub-árvore direita são os templates que contém o requisito representado por aquele nó. De todas as árvores factíveis, desejamos encontrar a árvore de menor altura.

Aplicação:
A árvore gerada no segundo problema será usada como uma ferramenta no processo de consultoria e como componente de uma solução SaaS. Os módulos podem a qualquer momento ser atualizados pelos desenvolvedores da comunidade, o que pode modificar as dependências e os requisitos de cada template. Sendo assim é de enorme valor prático, a existência de métodos computacionalmente viáveis, para uso contidiano em empresas de consultoria de sistemas ERPs organizados em módulos.
