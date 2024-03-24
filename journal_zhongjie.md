# Semaine 12/02

Différent des langues européennes telles que l'anglais, le français, l'allemand, etc., les langues chinoises ne disposent pas d'une grammaire riche et rigoureuse, ce qui fait que les relations syntaxiques dans les phrases sont assez difficiles à repérer et à définir.

## verbe1 + nom + verbe2
La première construction syntaxique à aborder est la structure de "verbe1 + nom/pronom + verbe2". Observons les exemples suivants : "帮+他+做事", "看+我+打球", "学+人+说话". Le nom et le verbe2 sont tous les deux compléments du verbe1. De ce fait, il est possible de marquer les relations ainsi : verbe1 -[comp:obj]-> nom ; verbe1 -[comp:obj]-> verb2.

## comp:cleft
La deuxième construction syntaxique est très similaire de la première. Considérons la phrase suivante : "有人在玩手机". Même si cette phrase relève également la structure de "verbe1 + nom/pronom + verbe2", le deuxième verbe n'est pas considéré comme complément d'objet du verbe1. En effet, quand le premier verbe est "有" ou "是", le deuxième verbe est désormais son complément clivé car l'utilisation de "有" ou "是" permet de mettre en avant et d'accentuer le nom. 

## comp:res
L'autre type de complément verbal est complément résultatif. Comme indiqué par le nom, ce genre de complément a pour but d'exprimer le résultat d'une action. La relation complément résultatif se trouve dans les structures de "verbe + verbe" et "verbe + adjectif" telles que "洗好", "看到", "学会", "看懂", etc. Il est possible d'implémenter un modifieur "得" ou "不" au milieu. Le modifieur est dépendant du complément résultatif. 

## compound:svc
En tenant compte de la liberté syntaxique dans les langues chinoises, il est très courant de témoigner la situations où plusieurs verbes sont enchaînés. Prenons les exemples suivants : "我+起床+刷牙+洗脸+吃早饭", "我们去公园玩". Le premier exemple résulte d'une séquence d'actions où chaque action est réalisée l'une après l'autre. Le deuxième exemple évoque une relation où le deuxième verbe "玩" complète l'action "去" en ajoutant le but de cette action. Ces deux cas relèvent la relation "Serial Verbs Construction" (compound:svc). 

## comp:dir
Toutes les séquences d'actions en série ne présentent pas obligatoirement la relation compound:svc. Les verbes directionnels sont considérés comme complément directionnel. "上", "下", "出", "进", "回", "过", "开", "起" sont les huit verbes directionnels les plus utilisés. Dans une construction de "verbe + verbe dir", il y a la relation : verbe -[comp:dir]-> verbe dir. "来" et "去" sont deux verbes qui expriment la motion déictique. Dans une phrase comme "老师正向我们走来", il y a aussi une relation de complément directionnel entre "走" et "来" : 走 -[comp:dir]-> 来. En cas de la combinaison de plusieurs verbes directionnels ou déictiques, la relation entre eux est toujours complément directionnel : 提 -[comp:dir]-> 上 ; 上 -[comp:dir]-> 来.

## parataxis
En chinois, il est courant de trouver deux phrases placées côte à côte mais sans la présence d'une relation explicite de subordination, de coordination ou d'argument entre elles. Dans ce cas, les gouverneurs de deux phrases sont liées avec la relation [parataxis].

## 的 (adjectif)
"的" est un morphème très libre en chinois qui peut être rattaché à des verbes, des noms ou des pronoms de sorte de former un adjectif ou déterminant . Par exemple, il est possible de transformer le nom "学校" en adjectif en ajoutant le suffixe "的", donc "学校的". De la même manière, un verbe comme "注定好" est tranformé en adjectif "注定好的", un pronom comme "我" est transformé en déterminant "我的". Concernant cette construction syntaxique, "的" est considéré comme le gouverneur du groupe adjectif, le dépendant de "的" est complément d'objet : GOV -> "的" ; "的" -[comp:obj]-> DEP.

## Phrase comparative
La phrase comparative pourrait sembler épineuse d'analyser. En réalité, dans une phrase comme "伴娘比新娘美", la racine n'est ni "伴娘" ni "新娘" mais le feature "美". 
GOV -[root]-> "美";
"美" -[subj]-> "伴娘";
"美" -[comp:obl]-> "比";
"比" -[comp:obj]-> "新娘"

## UPOS PART
En chinois, il y a une classe grammaticale qui s'appelle "particule". Les particules sont souvent des caractères ou des mots courts qui sont utilisés pour indiquer la relation entre les mots, les phrases ou les clauses dans une phrase.
Par exemple, la particule "的" est souvent utilisée pour indiquer la possession ou l'attribution, tandis que "了" peut être utilisée pour indiquer un changement d'état ou la fin d'une action. Ces particules sont généralement intégrées dans la structure des phrases chinoises pour transmettre des nuances de sens et de relation.
Il est important de noter que le chinois n'a pas de système grammatical aussi complexe que certaines langues occidentales, comme l'anglais, et utilise plutôt des particules, des mots de fonction et la position des mots dans la phrase pour exprimer les relations grammaticales.

## Aspect accompli
L'accompli s'exprime à l'aide de certains caractères comme les particules "了", "过" ou les verbes comme "完". Ces caractères partagent le point commun qu'ils indiquent tous la fin d'une action.

## Classifieur (clf)
L'une des caractéristiques des langues chinoises est qu'elles possèdent les différents classifieurs tels que "个", "句", "辆". Les classifieurs sont liés avec leurs gouverneurs (souvent les noms) par la relation de [clf] : GOV -[clf]-> classifieur; classifieur -[mod]-> NUM.

## Expression figé
Étant donné l'utilisation courante d'expressions figées (成语) dans les langues chinoises modernes, qui sont héritées du chinois classique, nous allons traiter chaque expression comme un mot entier non segmentable avec une relation de "/m" entre chaque caractère au sein de la même expression.
大快人心 : GOV -> "大" ; "大" -[/m]-> "快", "快" -[/m]-> "人"; "人" -[/m]-> "心".

# Semaine 19/02
## La réunion du lundi 19/02
Nous sommes en vacances scolaires pendant cette semaine, donc le planning de réservation de salles n'est pas comme d'habitude. Notre salle habituelle n'est pas réservée. Avec un retard de 30 minutes, nous avons commencé la réunion dans une salle de groupe au sous sol de la BULAC. 

Pour cette semaine, chacun chacune a reçu 100 phrases à annoter. Moi personnellement, j'assume 100 phrases aléatoires du corpus mandarin. J'ai rencontré du problème lors de l'annotation pour les constructions contenant "才", par exemple, "工 作 要 從 哪 裡 著 手 才 好 ？ ". Ici, "才好" semble avoir un rôle plus éloigné que la racine par rapport à d'autres composants. De ce fait, "才好" entretient en réalité la relation "parataxis" avec la racine. Dans "才好", la tête est "好" et il y a une relation "modifieur" de "好" à "才" : "好" -[mod]-> "才".

Après la réunion, j'ai fini l'annotation sur 50 phrases.
## La réunion du jeudi 22/02
La réunion n'a pas eu lieu. On est restés chacun chez soi. J'ai fini l'annotation sur le reste des phrases. J'ai rencontré deux problèmes que j'ai partagés dans les Issues de Github. 
Voici les liens vers les questions :
- https://github.com/pmagistry/test_arborator/issues/11
- https://github.com/pmagistry/test_arborator/issues/12

# Semaine 26/02
## La réunion du lundi 26/02
Nous nous sommes regroupés dans la salle d'habitude sans la présence du tuteur.
## La réunion du jeudi 29/02
Nous avons traité les questions posés dans "issues" de github. La première question est la relation entre "我们" et "两个" ou entre "我们" et "两个人". Dans le premier cas, nous avons conclut 我们 -[mod]-> 两个 et 我们-[conj:appos]->两个人 pour le deuxième. Concernant les cas comme dans "我们这个月的生产目标要比上个月的数量加倍", "我们" est dislocated de "要".

La question suivante concerne le cas de "我要搭下一班车". Ici, "下" peut être considéré comme un déterminant ou un nom et il est le modifieur de "班".

Ensuite, dans la phrase "有 許 多 過 去 的 事 情 ， 我 都 忘 記 了 。", "有" est le complément clivé de "忘记" parce que le partie de "有" est mise en avant. 

Une autre phrase compliquée est la phrase sent 336 :
https://private-user-images.githubusercontent.com/145543123/309008325-27678cab-4df1-49a7-8c4c-7b39a0cc35ff.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDk0NzkwOTUsIm5iZiI6MTcwOTQ3ODc5NSwicGF0aCI6Ii8xNDU1NDMxMjMvMzA5MDA4MzI1LTI3Njc4Y2FiLTRkZjEtNDlhNy04YzRjLTdiMzlhMGNjMzVmZi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMzAzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDMwM1QxNTEzMTVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hOGRiYTY2OTQ2ODhlNjkwNjQ0OWM2NmYyNTg0Zjc1NWJhODRmN2U1YTBlNGY3YTE0NGM0ZGI1ZTE2NGYzYjFhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.3tYXOb3OXvNyUCRqCeoRmh8HcOVzqEYLTIJQ541qWcQ
Ici, "让" est la racine de la phrase. Dans "让人听", "人" et "听" sont tous compléments d'objet de "让". "舒服" est le compound:svc de 听 parce que ce sont deux actions qui s'enchaîenent. "口气很粗暴" est le parataxis de "让" et "他说话" est le parataxis de "口气很粗暴".

# Semaine 04/03
Cette semaine, nous avons surout discutés des questions posées sur "Les Issues" ou par les collègues pendant les réunions. J'ai remarqué que la plurpart des questions proviennent de la flexibilité et de la liberté syntaxique de la langue chinoise. Par exemple, on peut renforcer l'idéé de totalité en utilisant deux mots qui portent tous ce sens. Dans la phrase 104, "這 些 剩 菜 全 部 都 打 包 起 來 。 ", "全部" et "都" désignent tous la totalité, qui sont tous considérés comme modifieurs de "打". Il faut noter que "全部" ne rejoins pas "剩菜" d'ici. Un autre exemple est "我 沒 帶 雨 傘 ， 還 好 下 毛 毛 雨 而 已 。", dans la phrase 177. Cette phrase a provoqué un débat entre les collègues. L'un considère que "还好" est le gouverneur de la partie "還 好 下 毛 毛 雨 而 已", et que "下 毛 毛 雨 而 已" est son subordonnée. L'autre pense que le gouverneur de cette partie est l'état de "下 毛 毛 雨" et que "還 好" est son modifieur. Personnellement, je suis plutôt d'accord avec ce dernier parce qu'ici, "还好" qualifie le retour de l'état "下 毛 毛 雨 而 已" sur "我". Un dernier exemple est à propos de la combinaison de plusieurs "sous-phrases" plutôt independantes avec des relations de "parataxis" entre elles. Dans la phrase 105 "沒 有 排 骨 要 怎 麼 熬 湯 ？", même s'il n'y a pas de virgule, "没有排骨" et "要怎么熬汤" sont en réalité deux parties liées avec la relation parataxis parce que "没有排骨" exprime un prétexte, une cause, un état et que "要怎么熬汤" est une question générée en raison de ce prétexte.

# Semaine 11/03
Comme d'habitude, chacun travaille de son côté et met à jours les issues s'il y a des questions ou des doutes. Lundi, la réunion n'était pas maintenue parce que Mr. Magistry n'est pas venu. Mais je suis quand même venu pour travailler. Jeudi, nous avons repris les questions posées dans "Issues". 

La première question traitée concerne la phrase 285, "你 不 要 這 麼 嘴 饞 ， 看 到 東 西 就 想 吃 。", on a proposé deux versions d'annotation pour "看到东西" et "就想吃". Soit "就想吃" est parataxis de "看到东西", c'est-à-dire qu'il n'y a pas une dépendance explicite entre ces deux unités et que "就" est modifieur de "想". Sinon, "就想吃" est conj de "看到东西", c'est-à-dire que "想吃" est une action due à la cause "看到东西" et que "就" est le connecteur avec l'upos SCONJ. Les deux façons d'annotation sont possibles mais je trouve celui du dernier est vraisemblable parce que j'ai l'impression que la phrase met un accent sur "看到东西", qui est considéré comme un déclencheur sous-jacent de "想吃". La deuxième question traitée est sur la phrase 185 "用 牙 籤 剔 牙 齒 。". J'avais proposé d'annoter une relation de comp:obj entre "用" et "剔", mais le compteur propose la relation compound:svc à la place. Une astuce pour distinguer si c'est un complément ou un compound:svc est de mettre à la fois soit l'aspect soit l'auxiliare aux deux verbes et de voir s'il y a des problèmes sémantiques. Si aucun problème se relève, il s'agit de compounds:svc. Sinon le verbe qui pose problème est le complément. Donc ici, on peut bel et bien ajouter l'aspect "了" par exemple ou l'auxiliare "在" à ces deux verbes. Ils occupent donc un status sémantique relativement égale. La troisième question porte sur la phrase 419 "你 如 果 要 斜 躺 著 看 電 視 ， 早 晚 會 近 視 。". Je n'arrivais pas à trouver le complément de "要". En réalité, son complément est "看电视". "斜躺着" est une manière particulière de "看电视", donc modifieur de ce dernier. La quatrième question concerne une phrase complexe, n° 235 "農 事 必 須 的 牛 、 犁 、 耙 ， 沒 有 一 樣 會 。 比 喻 對 農 事 一 竅 不 通 。 ". Ici, "農 事 必 須 的 牛 、 犁 、 耙" est mis en avant, donc un dislocated de la racine "会". "没有一样会" relève la construction syntaxique "有 + nom + verbe". Conventionnellement, le verbe "会" est comp:cleft de "有" et le nom "一样" est le comp:obj.

Comme j'ai déjà fini les annotations de Siman, je vais désormais recueillir les Issues intéressants et les mettre sur Wiki.

# Semaine 18/03
À la fin de la réunion du jeudi, nous avons essayé de traiter ma question posée dans "Issues", la phrase 364 : "體 型 較 大 的 雞 會 比 其 他 的 雞 來 得 晚 發 聲 啼 叫". Malheureusement, "來 得 晚 發 聲 啼 叫" est trop difficile à analyser. Donc, nous avons décidé de le laisser à la semaine prochaine.

Sinon, j'ai commencé à rédiger la page wiki. J'ai créé une section pour le mandarin et un autre pour le teochew. Dans le section du mandarin, j'ai ajouté des Issues intéressants vus dans l'historique, tels que l'annotation de chengyu, la relation comp:cleft, compound:svc, l'annotation de 才 et la liste des auxiliaires. Dans chque article, j'ai d'abord expliqué les règles d'annotation, puis les expliciter en s'appuyant sur un exemple. Si l'annotation d'une relation syntaxique réfère à plusieurs types de construction syntaxique, je vais expliquer les règles cas par cas. En tout cas, j'essaie de donner des explications simples, concises et claires.
