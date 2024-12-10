# Observer_python

## Contexto
O sistema é uma aplicação para envio de notificações de notícias aos usuários que optaram por se inscrever para receber essas atualizações. Cada notícia deve ser enviada apenas aos usuários interessados, garantindo que apenas os destinatários corretos sejam notificados.

## Problema
O desafio principal do sistema é gerenciar a comunicação entre o emissor de notificações (notícias) e os receptores (usuários) de forma eficiente e desacoplada. 

- Os usuários podem se inscrever ou cancelar sua inscrição a qualquer momento.
- Os usuários recebem notificações apenas onde estão inscritos.

## Solução
O padrão Observer resolve esse problema ao introduzir uma abordagem desacoplada para comunicação entre o emissor (Observable) e os receptores (Observers).
 - O emissor (notícias) não precisa saber nada sobre os receptores além de sua capacidade de "ouvir" notificações.
 - Os usuários podem ser adicionados ou removidos dinamicamente da lista de inscritos sem afetar o restante do sistema.
 - A lista de observadores (usuários) pode crescer ou encolher sem que o emissor precise alterar sua lógica principal. Além disso, o padrão facilita a extensão do sistema para incluir outros tipos de observadores.
 - Ao seguir os princípios de orientação a objetos e design patterns, o sistema é modular e mais fácil de modificar ou estender.
