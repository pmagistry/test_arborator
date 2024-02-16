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