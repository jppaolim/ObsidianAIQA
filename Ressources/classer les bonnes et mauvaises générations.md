#mywork 

- il y a plusieurs possibilités :
	- métriques type MAUVE et UNION
	- mon idée qui est de trainer une discriminateur, sur la base du modèle ROBERTA (car utilisé dans le détecteur OpenAI ). On s'aperçoit que les meilleurs discriminateurs sont ceux qui trainent sur le générateur. Par conséquent on doit entrainer sur les phrases produites. L'idée serait d'entraîner sur les phrases produits. quand on arrive plus à entraîner (score F1 ou autre de 50% idem un score random) et bien on a qqs de parfait !
	- Utiliser [[@BARTScore: Evaluating Generated Text as Text Generation]]
	-
	-