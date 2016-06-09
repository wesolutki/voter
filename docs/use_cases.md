# Use Cases

{% plantuml %}

@startuml

actor Aktor
actor Zarządca
actor Członek
actor Administrator

Zarządca -up-|> Aktor
Członek -up-|> Aktor
Administrator -up-|> Aktor

Aktor -> (Odzyskanie hasła) : Bo mogę
Aktor -> (Logowanie)
(Logowanie) -> (Wylogowanie)

Zarządca --> (Dodanie,\nusunięcie\ni edycja członka) 
Zarządca --> (Dodanie\nuchwały)
Zarządca --> (Dyskusje\no uchwałach)
Zarządca --> (Zatwierdzenie\nszkicu\nuchwały)

Członek --> (Przeglądanie\nzdarzeń\nzarządcy)
Członek --> (Dodanie\nszkicu\nuchwały)
Członek --> (Przeglądanie\nwirtualnej\ntablicy)
Członek --> (Przeglądanie\nopłat)
Członek --> (Wysłanie\nmaila\ndo zarządcy)
Członek --> (Przeglądanie\nuchwał)
(Przeglądanie\nuchwał) --> (Odrzucone\nuchwały)
(Przeglądanie\nuchwał) --> (Subskrypcja\ndyskusji)
(Przeglądanie\nuchwał) --> (Przyjęte\nuchwały)
(Przeglądanie\nuchwał) --> (Uchwały\nw trakcie\ngłosowania)
(Uchwały\nw trakcie\ngłosowania) --> (Głosowanie)

@enduml

{% endplantuml %}

