# 30/01/2024

## Remarques : 
- Regarder les compléments résultatifs *对应着中文句法的补语*
- global {sent_id = ""} pour localiser une phrase
- Consulter https://guidelines.surfacesyntacticud.org/docs/language/
- 现代汉语 (黄伯荣、廖序东：2017)
- 现代汉语语法研究教程 (陆俭明: 2019)

## Issues :

- 50 你 是 真 不 知 道 ， 還 是 假 不 知 道 ？

  927 [3/3]你是不是生气了？

  Q : 是 + verb，complément prédicatif ?

- 51 我 還 沒 說 完 ， 你 先 別 插 嘴 好 嗎 ？ 

  1852 你先看完再说。

  Entre 看 et 完，comp:res n'existe pas sur arborator complément résultatif

  551 别说话！

Q: 别 + verb，complément auxiliaire ? Pourquoi différent de 是 + verb ?

- 53 心 事 沒 有 人 知 道 ， 我 壓 抑 得 很 難 過 。  *C'est une clivée*

  3808 他是老板，却没有人听他的。

- 56 雖 然 你 們 是 好 朋 友 ， 也 不 能 太 隨 便 。 

  pattern { N [form="虽"] ; M [form="然"] }

  Q: Comment définir la racine ? C'est quoi la fonction synatxique de 虽然 ？虽然 est plutôt cc et non pas modifieur.

- 60 我 替 他 煩 惱 得 要 死 ， 他 卻 不 當 一 回 事 。 

  Q: 烦恼 c'est verb ou adj ?  Tous ceux qui sont verbes statifs sont adj. Si on peut ajouter

  “xx得要死”，“很xx”，一般是形容词。

## À faire :
Commencer à annoter les premières phrases

# 08/02/2024

## Remarques : 
- Créer des issues pour préparer des discussions.
- conj:redup是reduplication
- clf是classifieur（量词）。数字是量词的mod。

## Issues :
- 4 他 的 度 量 很 狹 小 。

  Q : “他的”和“度量”之间是mod没有问题（定语中心语关系）。但为什么“的”是“他”的racine？（grewmatch上也是这样的）

- 5 伴 娘 比 新 娘 美 。 比 喻 喧 賓 奪 主 。

  Q : parataxis的关系就很奇怪，这里似乎整个前句是后句的主语。“喧宾夺主”作为成语我倾向于把它当作一个词，虽然成语内部也有句法关系。

- 7 你 媽 媽 正 想 到 你 而 提 起 你 。

  Q : “妈妈”之间，没有conj:redup/m。只有conj:red。

- 12 他 幫 別 人 照 顧 小 孩 。

  Q : 这里应该有个从句。我们可以把它当作个从句典范。
