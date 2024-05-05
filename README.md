# Atom_Auto_Design_Project
 I-II 2024 project

# про структуру API и DEVOPS
## немного про env
проект содежит только один env файл в корне, для модулей подключается он же, причем не только для dockerfile модулей но и для например питоновского конфига. Поэтому если нужно добавить какую либо перемную в env нужно ее сначала добаить в .env.example а после в .env в корне проекта
## про https коды
Тк вся дока по рукам будет в свагере то приветсвуется использование кодов отличных от 200 и 500, где это необходимо.
```
200 OK
201 Created
202 Accepted
400 Bad Request
401 Unauthorized
404 Not Found
409 Conflict
415 Unsupported Media Type
500 Internal Server Error
501 Not Implemented
```

# stanza description
### Pipline discription 

| ***Processor*** | ***Package***      |
|-----------------|--------------------|
| tokenize        | syntagrus          |
| pos             | syntagrus_charlm   |
| lemma           | syntagrus_nocharlm |
| depparse        | syntagrus_charlm   |
| ner             | wikiner            |

### CoNLL-U Format no AutoReviewData:
#### deprel:
1. punct: знак препинания. Метка punct используется для представления знаков препинания в предложении.
2. case: предлог или постпозиция. Метка case обычно относится к предлогам или постпозициям, которые управляют падежом или формой слова.
3. obl: обязательный аргумент или обстоятельство. Метка obl обычно относится к фразам, которые указывают на обязательные аргументы или обстоятельства глагола.
4. advmod: наречие-модификатор. Метка advmod обозначает наречие, которое модифицирует глагол, прилагательное, другое наречие или целое предложение.
5. conj: соединительная конструкция. Метка conj обозначает слова или фразы, соединенные союзами или соединительными элементами.
6. nsubj: подлежащее. Метка nsubj обозначает подлежащее в предложении, т.е. существительное или местоимение, которое выполняет действие глагола.
7. root: корень предложения. Метка root обозначает корень или главное слово предложения.
8. nmod: модификатор имени. Метка nmod обычно относится к модификаторам имен, таким как предложения, выраженные существительными, наречиями или прилагательными.
9. amod: определение. Метка amod обозначает прилагательное, которое является определением существительного.
10. cc: соединительный элемент. Метка cc обозначает соединительный элемент, обычно союз, который связывает два или более слова или фразы.
11. obj: прямое дополнение. Метка obj обозначает прямое дополнение глагола, т.е. существительное или фразу, которая является объектом действия глагола.
12. mark: маркер вводной группы или подчинительного союза. Метка mark обозначает маркер или вводное слово, которое связывает подчинительную клаузу с главным предложением.
13. parataxis: параллельный элемент синтаксической структуры. Метка parataxis используется для обозначения параллельных элементов синтаксической структуры, например, несвязанных фраз или предложений.
14. det: определитель. Метка det обозначает определитель, который модифицирует существительное.
nummod: числовое модифицированное. Метка nummod обозначает числовое модифицированное существительное или прилагательное.
15. advcl: наречие клаузы. Метка advcl обозначает клаузу, которая является наречием, т.е. действие происходит во времени, месте или обстоятельствах, указанных в клаузе.
16. csubj: субъективное зависимое дополнение. Метка csubj обозначает субъективное зависимое дополнение, т.е. клаузу, которая выражает субъект глагола.
17. xcomp: расширенное зависимое дополнение. Метка xcomp обозначает зависимое дополнение, которое является частью основного глагола, но не управляется им.
18. fixed: фиксированное группирование. Метка fixed обозначает фиксированное группирование слов или фраз в предложении.
19. ccomp: составной объект. Метка ccomp обозначает составной объект, т.е. клаузу, которая выражает субъект глагола.
20. flat:foreign: соединенные компоненты иностранных слов. Метка flat:foreign используется для обозначения соединенных компонентов иностранных слов.
21. nsubj:pass: подлежащее пассивного залога. Метка nsubj:pass обозначает подлежащее в пассивном залоге.
22. aux: вспомогательный глагол. Метка aux обозначает вспомогательный глагол.
23. nummod:entity: числовой модификатор-сущность. Метка nummod:entity обозначает числовой модификатор-сущность.
24. appos: пояснение. Метка appos обозначает пояснение, которое является частью или описывает другой элемент в предложении.
25. cop: глагол-копула. Метка cop обозначает глагол-копула, который связывает предикат с его субъектом.
26. iobj: косвенное дополнение. Метка iobj обозначает косвенное дополнение глагола.
27. acl:relcl: относительная клауза. Метка acl:relcl обозначает относительную

примеры:
1. punct frequncey:0.187 
+ exmple upos: ['PROPN -> PUNCT', 'ADV -> PUNCT', 'PUNCT -> PUNCT', 'PART -> PUNCT', 'X -> PUNCT', 'SCONJ -> PUNCT', 'INTJ -> PUNCT', 'AUX -> PUNCT', 'NUM -> SYM', 'PRON -> PUNCT', 'DET -> PUNCT', 'CCONJ -> PUNCT', 'NUM -> PUNCT', 'ADJ -> PUNCT', 'NOUN -> PUNCT', 'VERB -> PUNCT', 'SYM -> PUNCT'] 
+ exmple values: {'контроль->,', 'автомобиль->.', 'опыт->,', 'цены->,', 'вызывает->.', 'автомобиль->:', 'Нет->.', 'убедился->.', 'удержания->,', 'отделка->,', 'Тем->,', 'пользовании->)', 'пользовании->(', 'раздумывает->,', 'предотвращение->,', 'имеет->.', 'включая->,', 'купил->!', 'упрощает->,'}
2. case frequncey:0.094 
+ exmple upos: ['VERB -> ADP', 'NOUN -> SYM', 'PROPN -> ADP', 'ADJ -> ADP', 'SYM -> ADP', 'PUNCT -> ADP', 'NOUN -> PUNCT', 'PRON -> ADV or ADP', 'NOUN -> ADV', 'ADV -> ADP', 'SYM -> ADV', 'ADJ -> ADV', 'ADP -> ADP', 'DET -> ADP', 'NUM -> ADP', 'NOUN -> ADP'] 
+ exmple values: {'расходники->НА', 'надежности->В', 'которого->ОТ', 'время->В', 'стекло->НА', 'время->ЗА', 'рынке->НА', 'пользовании->В', 'морозе->НА', 'полосе->В', 'комплектации->В', 'приобретения->НАСЧЕТ', 'этого->ДО', 'ней->НА', 'появлении->ПРИ', 'моменту->К', 'автомобиле->В', 'брелока->СО', 'обслуживанием->С'}
3. obl frequncey:0.087 
+ exmple upos: ['SYM -> NOUN', 'NOUN -> ADV', 'DET -> PRON', 'VERB -> NUM', 'ADV -> NUM', 'AUX -> PROPN', 'VERB -> ADJ or SYM', 'NOUN -> NOUN', 'ADJ -> PROPN', 'PRON -> ADV', 'ADJ -> ADV', 'NOUN -> PRON', 'PRON -> NOUN', 'NUM -> NOUN', 'ADJ -> NOUN', 'AUX -> NOUN', 'PROPN -> PROPN', 'VERB -> PROPN', 'NOUN -> VERB', 'VERB -> ADV', 'ADV -> PROPN', 'NUM -> PRON', 'ADJ -> PRON', 'AUX -> PRON', 'NOUN -> ADJ', 'VERB -> INTJ or NOUN', 'DET -> ADV', 'NOUN -> SCONJ', 'ADV -> NOUN', 'ADJ -> NUM', 'VERB -> PRON', 'DET -> NOUN', 'VERB -> PUNCT', 'ADJ -> ADJ', 'ADV -> PRON'] 
+ exmple values: {'убедился->ВРЕМЯ', 'таких->ПРОЕКЦИЯ', 'доставлял->ВРЕМЯ', 'надежный->ОЧЕНЬ', 'положительные->ДЕЙСТВИТЕЛЬНО', 'убедился->НАДЕЖНОСТИ', 'сказка->ВООБЩЕ', 'удобный->ОЧЕНЬ', 'вызывает->ВОПРОСОВ', 'ездить->НЕЙ', 'сказать->ОДНО', 'вызывает->ВРЕМЯ', 'предусмотрен->АВТОМОБИЛЕ', 'купил->ПОЯВЛЕНИИ', 'заметил->НЕДОСТАТКА', 'проехала->МОМЕНТУ', 'просторный->ОЧЕНЬ', 'раздумывает->ПРИОБРЕТЕНИЯ', 'вызывает->СЛОЖНОСТЕЙ', 'проехала->КМ'}
4. conj frequncey:0.078 
+ exmple upos: ['ADJ -> SYM', 'NOUN -> ADV', 'VERB -> VERB', 'PROPN -> VERB', 'VERB -> NUM', 'PROPN -> NUM', 'ADV -> NUM or VERB', 'NUM -> PROPN', 'PROPN -> ADJ', 'VERB -> ADJ', 'NOUN -> NOUN', 'PROPN -> SYM', 'ADV -> ADJ', 'NUM -> ADV or DET', 'X -> X', 'ADJ -> ADV', 'SYM -> VERB', 'DET -> ADJ', 'NOUN -> PRON', 'PRON -> NOUN', 'PART -> VERB', 'VERB -> PART', 'NUM -> NOUN', 'ADJ -> NOUN', 'PROPN -> PROPN', 'VERB -> PROPN', 'NOUN -> VERB', 'VERB -> ADV', 'ADV -> PROPN', 'VERB -> DET', 'PROPN -> ADV', 'NOUN -> NUM', 'PRON -> PRON', 'ADJ -> PRON or AUX', 'NOUN -> ADJ', 'ADV -> ADV', 'VERB -> INTJ or CCONJ or NOUN', 'PROPN -> NOUN', 'PRON -> VERB', 'ADJ -> VERB', 'ADV -> NOUN', 'AUX -> VERB', 'NUM -> VERB or NUM or ADJ', 'VERB -> PRON', 'AUX -> ADJ', 'VERB -> AUX', 'DET -> NOUN', 'ADJ -> ADJ', 'NOUN -> PROPN'] 
+ exmple values: {'проекция->КОНТРОЛЬ', 'проехала->МЕНЯЮТСЯ', 'проблем->ЦЕНЫ', 'просторный->ЭРГОНОМИЧНЫЙ', 'проекция->ТД', 'салон->ОТДЕЛКА', 'Крассивый->КОМФОРТНЫЙ', 'упрощает->ПОЛУЧАЕШЬ', 'столкновения->УДЕРЖАНИЯ', 'пользовании->ПРОЕХАЛА', 'проекция->ПРЕДОТВРАЩЕНИЕ', 'вызывает->ОТТАИВАЕТ', 'вызывает->ПРОГРЕВАЕТСЯ', 'вызывает->ПРЕДУСМОТРЕН', 'надежности->КАЧЕСТВЕ', 'пользовании->ПРОДОЛЖАЕТ', 'расходники->СТРАХОВКИ', 'салон->СБОРКА', 'отличная->ВЕЛИКОЛЕПНАЯ', 'надежный->НЕПРИХОТЛИВЫЙ'}
5. advmod frequncey:0.077 
+ exmple upos: ['VERB -> ADP', 'NOUN -> ADV', 'VERB -> VERB', 'DET -> PRON', 'VERB -> NUM', 'PRON -> PART', 'NUM -> PART', 'ADJ -> PART', 'AUX -> PART', 'VERB -> ADJ', 'NOUN -> CCONJ', 'NUM -> ADV', 'VERB -> SCONJ', 'AUX -> ADV', 'PRON -> ADV', 'PROPN -> SCONJ', 'ADJ -> ADV', 'ADV -> SCONJ', 'NOUN -> PRON', 'PRON -> CCONJ', 'PROPN -> PART', 'VERB -> PART', 'ADJ -> CCONJ', 'ADV -> PART', 'SCONJ -> PART', 'VERB -> ADV', 'DET -> PART', 'PROPN -> ADV', 'ADJ -> PRON', 'ADV -> ADV', 'ADJ -> ADP', 'DET -> ADV', 'PART -> PART or ADV', 'ADV -> CCONJ', 'NOUN -> SCONJ', 'VERB -> PRON', 'NOUN -> PART', 'ADV -> PRON'] 
+ exmple values: {'упрощает->ЗНАЧИТЕЛЬНО', 'продолжает->СЕЙЧАС', 'единого->НИ', 'только->ИСКЛЮЧИТЕЛЬНО', 'поднимался->ВЫШЕ', 'первый->НЕ', 'раздумывая->НЕ', 'порадовал->ВООБЩЕ', 'страховки->ВКЛЮЧАЯ', 'поднимался->НЕ', 'расходник->ТОЛЬКО', 'грустно(->РЕАЛЬНО', 'откидываются->УДОБНО', 'прогревается->ПОЛНОСТЬЮ', 'вызывает->НЕ', 'км->БОЛЕЕ', 'ломалось->НЕ', 'заметил->НЕ', 'простояла->ДАЖЕ'}
6. nsubj frequncey:0.074 
+ exmple upos: ['VERB -> X', 'SYM -> NOUN', 'PART -> NOUN', 'VERB -> VERB', 'DET -> PRON', 'VERB -> NUM', 'PROPN -> NUM', 'ADV -> NUM', 'AUX -> PROPN', 'NOUN -> PROPN', 'VERB -> ADJ', 'NOUN -> NOUN', 'VERB -> SYM', 'ADJ -> PROPN', 'ADV -> ADJ', 'ADJ -> ADV', 'NOUN -> PRON', 'PRON -> NOUN', 'NUM -> NOUN', 'ADJ -> NOUN', 'AUX -> NOUN', 'VERB -> PROPN or ADV', 'ADV -> PROPN', 'VERB -> DET', 'PROPN -> ADV', 'NOUN -> NUM', 'NUM -> PRON', 'ADJ -> PRON', 'PRON -> PRON', 'AUX -> PRON', 'DET -> PROPN', 'NOUN -> ADJ', 'VERB -> INTJ', 'NOUN -> SYM', 'VERB -> NOUN', 'PROPN -> NOUN', 'PRON -> NUM', 'ADV -> NOUN', 'ADJ -> NUM', 'AUX -> ADJ', 'VERB -> PRON', 'PROPN -> PRON', 'DET -> NOUN', 'ADJ -> ADJ', 'ADV -> PRON'] 
+ exmple values: {'Нет->ПРОБЛЕМ', 'вызывает->ЭКСПЛУАТАЦИЯ', 'простояла->НОЧЬ', 'вызывает->САЛОН', 'имеет->АВТОМОБИЛЬ', 'великолепная->ЭРГОНОМИКА', 'упрощает->ЧТО', 'ломалось->НИЧЕГО', 'меняются->РАСХОДНИК', 'прогревается->МАШИНА', 'автомобиль->ЭТО', 'пользовании->ОПТИМА', 'отличная->ДИНАМИКА', 'сказка->СИСТЕМА', 'продолжает->ДРУГ', 'раздумывает->КТО', 'опыт->ЭТО', 'удобный->САЛОН', 'удобные->СИДЕНЬЯ', 'проехала->МАШИНА'}
7. root frequncey:0.072 
+ exmple upos: [] 
+ exmple values: {'НЕТ', 'МОГУ', 'ДОСТАТОЧНО', 'ПОДНИМАЛСЯ', 'УДОБНЫЙ', 'ИМЕЕТ', 'ЛОМАЛОСЬ', 'УДОБНО', 'ОТЛИЧНАЯ', 'РАСХОД', 'ДОСТАВЛЯЛ', 'АВТОМОБИЛЬ', 'ЗАМЕТИЛ', 'КУПИЛ', 'ВЫЗЫВАЕТ', 'СКАЗКА', 'УДОБНЫЕ', 'УБЕДИЛСЯ'}
8. nmod frequncey:0.063 
+ exmple upos: ['SYM -> NOUN', 'NOUN -> NOUN or PRON', 'PRON -> NOUN', 'NUM -> NOUN', 'ADJ -> NOUN', 'NOUN -> ADP', 'PROPN -> PROPN', 'NOUN -> VERB or NUM', 'PRON -> PRON', 'ADJ -> PRON', 'NOUN -> ADJ or SYM', 'PROPN -> NOUN', 'NUM -> NUM', 'ADJ -> NUM', 'NUM -> ADJ', 'PROPN -> PRON', 'DET -> NOUN', 'NOUN -> PROPN'] 
+ exmple values: {'Автомобиль->КОМПЛЕКТАЦИИ', 'множество->ФУНКЦИЙ', 'вождения->КОТОРОГО', 'предотвращение->СТОЛКНОВЕНИЯ', 'процесс->ВОЖДЕНИЯ', 'Оптима->КОМПЛЕКТАЦИИ', 'опыт->ВЛАДЕНИЯ', 'проблем->ОБСЛУЖИВАНИЕМ', 'моменту->ВРЕМЕНИ', 'удержания->ПОЛОСЕ', 'пользовании->ЭТОГО', 'проекция->СТЕКЛО', 'пользования->АВТОМОБИЛЕМ', 'появлении->РЫНКЕ', 'цены->РАСХОДНИКИ', 'появлении->К5', 'качестве->МАТЕРИАЛОВ', 'контроль->ЗОН', 'время->ПОЛЬЗОВАНИЯ', 'владения->АВТОМОБИЛЕМ'}
9. amod frequncey:0.055 
+ exmple upos: ['NOUN -> NOUN', 'ADV -> ADJ', 'PRON -> VERB', 'NOUN -> VERB or DET', 'ADJ -> NUM', 'PROPN -> VERB', 'NOUN -> NUM', 'DET -> ADJ', 'NUM -> ADJ', 'PRON -> ADJ', 'PROPN -> NUM', 'NOUN -> ADJ', 'NUM -> ADP', 'PROPN -> ADJ', 'ADJ -> ADJ'] 
+ exmple values: {'салон->ПРОСТОРНЫЙ', 'морозе->СИЛЬНОМ', 'багажник->БОЛЬШОЙ', 'удовольствие->ОГРОМНОЕ', 'моменту->НАСТОЯЩЕМУ', 'время->ЗИМНЕЕ', 'стекло->ЛОБОВОЕ', 'автомобиль->КРАССИВЫЙ', 'автомобиль->НАДЕЖНЫЙ', 'сиденья->ЗАДНИЕ', 'брелока->ШТАТНОГО', 'недостатка->ЕДИНОГО', 'функций->ПОЛЕЗНЫХ', 'автомобилем->ПОДОБНЫМ', 'эмоции->ПОЛОЖИТЕЛЬНЫЕ', 'зон->СЛЕПЫХ', 'опыт->ПЕРВЫЙ', 'цены->ПРИЕМЛЕМЫЕ', 'вещей->ДЛИННЫХ', 'автомобиль->КРУТОЙ'}
10. cc frequncey:0.04 
+ exmple upos: ['NOUN -> PART', 'X -> CCONJ', 'PART -> CCONJ', 'NOUN -> ADV or CCONJ', 'ADP -> CCONJ', 'ADJ -> ADV', 'PRON -> CCONJ', 'AUX -> CCONJ', 'NUM -> CCONJ', 'VERB -> PART', 'ADJ -> CCONJ', 'VERB -> ADV', 'INTJ -> CCONJ', 'ADJ -> PRON', 'ADV -> ADV', 'PROPN -> CCONJ', 'VERB -> CCONJ', 'NOUN -> SCONJ', 'ADV -> CCONJ', 'VERB -> PRON', 'DET -> CCONJ', 'VERB -> PUNCT', 'ADV -> PRON'] 
+ exmple values: {'скрипело->НИ', 'крассивый->И', 'страшнее->И', 'получаешь->И', 'понятно->И', 'эргономичный->И', 'прогревается->И', 'продолжает->И', 'оттаивает->И', 'сборка->И', 'обдув->И', 'неприхотливый->И', 'бряцало->НИ', 'тд->И', 'качестве->И', 'откидываются->И', 'протирай->А', 'меняются->И', 'страховки->И', 'начинает->А'}
11. obj frequncey:0.028 
+ exmple upos: ['VERB -> ADJ', 'NOUN -> NOUN', 'VERB -> NOUN or PROPN', 'ADV -> NOUN', 'VERB -> VERB', 'ADV -> PROPN', 'VERB -> NUM or PRON'] 
+ exmple values: {'поймать->МОМЕНТ', 'поменять->ФИЛЬТР', 'включая->КАСКО', 'открой->ОКНО', 'доставлял->УДОВОЛЬСТВИЕ', 'протирай->СТЕКЛО', 'купил->ЕЕ', 'шевелиться->КАПОТ(', 'регулировать->ЕЁ', 'Назвать->АВТОМОБИЛЬ', 'заснять->ОШИБКУ', 'провёл->ДИАГНОСТИКУ', 'Соблюдать->РЕЖИМПРИ', 'жалею->ОПРЕДЕЛЕНГО', 'выбрал->АВТО', 'получаешь->ПРОЦЕСС', 'получаешь->ЭМОЦИИ', 'Знал->ЧТО', 'сделать->ЧТО', 'имеет->МНОЖЕСТВО'}
12. det frequncey:0.02 
+ exmple upos: ['INTJ -> DET', 'DET -> DET', 'NUM -> DET', 'ADJ -> DET', 'PRON -> DET', 'NOUN -> DET', 'VERB -> DET', 'PROPN -> DET', 'SYM -> DET', 'PRON -> ADJ'] 
+ exmple values: {'функций->ТАКИХ', 'момент->ЭТОТ', 'пойми->КАКИЕ', 'кнопки->ВСЕ', 'автомобиль->ЭТОТ', 'машина->ТАКАЯ', 'надежности->ЕГО', 'время->ВСЁ', 'проблемы->ВСЕ', 'могу->ТЕМ', 'сложностей->НИКАКИХ', 'комплекцию->ЛЮБУЮ', 'объёма->ТАКОГО', 'косяки->ВСЕ', 'звона->НИКАКОГО', 'проблем->НИКАКИХ', 'годом->КАЖДЫМ', 'проблемы->ЭТИ', 'авто->ЭТИМ', 'фишки->ТАКОЙ'}
13. nummod frequncey:0.018 
+ exmple upos: ['NOUN -> NOUN', 'NUM -> NUM', 'ADJ -> NUM', 'NOUN -> NUM', 'PUNCT -> NUM', 'VERB -> NUM', 'PROPN -> NUM', 'SYM -> NUM', 'NOUN -> ADJ', 'NUM -> NOUN'] 
+ exmple values: {'литров->8', 'л.->9,3', 'тысячах->25', 'км/->100', 'л.->2.5', 'годаГод->21', 'динамика->2,5', 'тыс.км->5', 'ребенком->1', 'литра->2', 'л.->194', 'дней->10', 'км->130 000', 'года->21', 'месяцев->4', 'года->ПОЛ', 'минус->ОДИН', 'фото->23', '150->ТЫСЯЧ', 'фото->12'}
14. mark frequncey:0.018 
+ exmple upos: ['DET -> SCONJ', 'NUM -> SCONJ', 'ADJ -> SCONJ', 'PRON -> SCONJ', 'NOUN -> SCONJ', 'VERB -> SCONJ', 'NUM -> ADV', 'AUX -> SCONJ', 'VERB -> ADV', 'PROPN -> SCONJ', 'SYM -> SCONJ', 'NOUN -> ADV', 'ADJ -> ADV', 'ADV -> SCONJ', 'NOUN -> PRON', 'VERB -> PRON', 'ADV -> ADV'] 
+ exmple values: {'можно->ЧТО', 'проекция->КАК', 'красивая->ЧТО', 'покупайте->ТАК', 'езжу->КАК', 'хочу->ЧТО', 'опыт->ПОСКОЛЬКУ', 'отрегулировал->ЧТО', 'простояла->ЕСЛИ', 'едешь->ЧЕМ', 'резвая->ЧТО', 'управление->КАК', 'выбрал->ЧТО', 'хотят->КОГДА', 'вибрирует->ТЕМ', 'протирай->ПОКА', 'страшнее->ТЕМ', 'устранены->КОГДА', 'жарко->ЕСЛИ'}
15. parataxis frequncey:0.017 
+ exmple upos: ['INTJ -> VERB', 'SYM -> NOUN', 'INTJ -> NUM', 'NOUN -> ADV', 'VERB -> VERB', 'PROPN -> VERB', 'VERB -> NUM', 'PROPN -> NUM', 'ADJ -> PART', 'ADV -> VERB or NUM', 'PROPN -> ADJ', 'VERB -> ADJ', 'NOUN -> NOUN', 'DET -> VERB', 'AUX -> ADV', 'ADV -> ADJ', 'VERB -> SCONJ', 'PUNCT -> VERB', 'PRON -> ADV', 'INTJ -> PART', 'ADJ -> ADV', 'PRON -> INTJ', 'NOUN -> PRON', 'PRON -> NOUN', 'VERB -> PART', 'NUM -> NOUN', 'ADJ -> NOUN', 'ADV -> PART', 'NOUN -> VERB', 'VERB -> ADV', 'ADV -> PROPN', 'VERB -> DET', 'PROPN -> ADV', 'NOUN -> NUM', 'ADJ -> PRON', 'NOUN -> ADJ', 'CCONJ -> NOUN', 'ADV -> ADV', 'VERB -> INTJ or NOUN', 'PROPN -> NOUN', 'PRON -> VERB', 'ADJ -> VERB', 'ADV -> NOUN', 'NUM -> VERB or NUM', 'ADJ -> NUM', 'NUM -> ADJ', 'NOUN -> PART', 'ADJ -> ADJ', 'NOUN -> PROPN'] 
+ exmple values: {'ошибки->ВИДИТ', 'тд->УПРОЩАЕТ', 'располагает->НАОБОРОТ', 'пойми->ВЕРНЕЕ', 'заржавел->ПОКРАШЕН', 'одно->АВТОМОБИЛЬ', 'так->ДИНАМИКА', 'забронированы->ДОПОМ', 'грех->НУ', 'Комплектация->ПРОБЕГА', 'нечему->АКПП', 'шевелиться->ДРЫГАТЬСЯ', 'долили->УДАЛОСЬ', 'начинает->СТРАШНО', 'автомобилем->ПОЛЬЗОВАНИИ', 'комфортная->МЕНЯ', 'момент->ЗАРЖАВЕЛ', 'так->УЖАС', 'сиденья->ПОЙМИ', 'Комплектация->ОКНОМ'}
16. advcl frequncey:0.01 
+ exmple upos: ['VERB -> VERB', 'PROPN -> VERB', 'VERB -> NUM', 'ADV -> NUM or VERB', 'PROPN -> ADJ', 'VERB -> ADJ', 'DET -> VERB', 'ADV -> ADJ', 'ADJ -> ADV or NOUN', 'NOUN -> VERB', 'VERB -> ADV', 'ADV -> PROPN', 'VERB -> DET', 'ADV -> DET', 'NOUN -> ADJ', 'VERB -> NOUN', 'PRON -> VERB', 'ADJ -> VERB', 'ADV -> NOUN', 'VERB -> PRON', 'ADJ -> ADJ'] 
+ exmple values: {'выехал->ЗАЕЗЖАЯ', 'сделали->ЕСТЬ', 'скрипит->ЕДЕШЬ', 'жрать->ЖИВЕМ', 'нет->ВАЛКАЯ', 'Достаточно->СТУКНУЛИ', 'дополнение->ПОМНИТЬ', 'горят->ХОТЯТ', 'оттаивает->ПРОСТОЯЛА', 'так->ОТХОДЯТ', 'открой->ЖАРКО', 'дополнять->МЕНЯТЬСЯ', 'начинает->ОТКРОЙ', 'купил->ОПЫТ', 'мелочи->ПОКУПАЙТЕ', 'прошло->ЕЗЖУ', 'начинает->ЕДЕШЬ', 'едешь->ВИБРИРУЕТ', 'купил->РАЗДУМЫВАЯ', 'закрыта->ЗАКРЫТА'}
17. fixed frequncey:0.008 
+ exmple upos: ['SCONJ -> PRON', 'PART -> NOUN', 'ADV -> ADP', 'PRON -> PART', 'ADP -> DET', 'PRON -> ADV', 'INTJ -> PART', 'CCONJ -> PART', 'ADV -> SCONJ', 'PRON -> INTJ', 'ADP -> NOUN', 'SCONJ -> SCONJ', 'DET -> SCONJ', 'ADV -> PART', 'CCONJ -> ADV', 'SCONJ -> PART', 'ADP -> PRON', 'DET -> PART', 'PRON -> PRON', 'ADJ -> PRON', 'ADP -> ADP', 'PART -> SCONJ', 'PRON -> ADP', 'ADV -> ADV', 'PART -> PART', 'NOUN -> SCONJ', 'SCONJ -> NOUN', 'ADP -> ADJ', 'PRON -> ADJ', 'ADV -> PRON'] 
+ exmple values: {'как->МИНИМУМ', 'так->КАК', 'значит->И', 'но->И', 'со->СТОРОНЫ', 'как->РАЗ', 'т.->К.', 'т.->П.', 'как->ТО', 'так->И', 'так->ЧТО', 'все->ЖЕ', 'ни->РАЗУ', 'да->И'}
18. xcomp frequncey:0.008 
+ exmple upos: ['ADJ -> VERB', 'VERB -> VERB'] 
+ exmple values: {'начал->ПЕРЕГРЕВАТЬСЯ', 'заставляет->ОГЛЯДЫВАТЬСЯ', 'хочу->СКАЗАТЬ', 'сможет->ОЦЕНИТЬ', 'смог->СКАЗАТЬ', 'начинает->ПЛЯСАТЬ', 'надумает->БРАТЬ', 'могу->СРАВНИТЬ', 'хочу->КОММЕНТИРОВАТЬ', 'могу->СКАЗАТЬ', 'может->ГЛЮЧИТЬ', 'берите->ПОЖАЛЕЕТЕ', 'продолжает->ЕЗДИТЬ', 'смогли->ПОМЕНЯТЬ', 'начал->СТИРАТЬСЯ', 'хотел->УЗНАТЬ', 'начинает->ШЕВЕЛИТЬСЯ', 'начала->ВЕРЕЩАТЬ'}
19. csubj frequncey:0.006 
+ exmple upos: ['PRON -> VERB', 'ADJ -> VERB', 'ADV -> ADJ', 'NOUN -> VERB', 'VERB -> VERB', 'ADV -> VERB'] 
+ exmple values: {'интересно->ТЫКАТЬ', 'лучше->НАЗВАТЬ', 'Рекомендации->СОБЛЮДАТЬ', 'грустно(->РАССТАВАТЬСЯ', 'надо->СМАЗЫВАТЬ', 'нечему->ЛОМАТЬСЯ', 'надо->ДЕЛАТЬ', 'удобно->ПАРКОВАТЬСЯ', 'Маст->РАЗБИРАТЬ', 'легко->ПОДСТРОИТЬ', 'страшнее->СМОТРЕТЬ', 'можно->РЕГУЛИРОВАТЬ', 'удалось->СДЕЛАТЬ', 'представляется->ПОЙМАТЬ', 'грех->УПОМЯНУТЬ', 'надо->МЕНЯТЬ', 'приходится->ЕХАТЬ', 'приходится->ПОДДЕРЖИВАТЬ', 'можно->СНИМАТЬ'}
20. iobj frequncey:0.005 
+ exmple upos: ['ADJ -> NOUN', 'VERB -> ADJ', 'NOUN -> NOUN', 'VERB -> NOUN', 'ADJ -> PROPN', 'ADV -> NOUN or PROPN', 'VERB -> NUM', 'ADJ -> PRON', 'NOUN -> PRON', 'VERB -> PRON', 'ADV -> PRON'] 
+ exmple values: {'надо->МНЕ', 'удивляться->ЭТОМУ', 'СОВЕТУЮ->ВСЕМ', 'времени->ВСЕМ', 'нравится->МНЕ', 'придает->АВТОМОБИЛЮ', 'Владею->ИМ', 'кажется->МНЕ', 'далеко->ИМ', 'сделать->МАШИНЕ', 'Рекомендую->ЛЮБИТЕЛЯМ', 'нет->СОСЕДУ', 'так->СЕБЕ', 'знаком->МНЕ', 'хватило->МНЕ', 'напомнила->МНЕ', 'повезло->МНЕ', 'думаю->ПАРТИТЕ', 'понравился->МНЕ'}
21. ccomp frequncey:0.005 
+ exmple upos: ['VERB -> ADJ or NOUN', 'PRON -> VERB', 'ADJ -> VERB', 'NOUN -> VERB', 'VERB -> ADV or VERB', 'DET -> ADJ', 'VERB -> PRON', 'ADJ -> ADJ'] 
+ exmple values: {'сказали->НОРМ', 'сказал->ИЗМЕНИЛОСЬ', 'жалею->ВЛАДЕЛЬЦЕМ', 'думаю->МОЖНО', 'сказать->РЕЗВАЯ', 'другое->ПОЕЗДИШЬ', 'верещать->ЗАКРЫТА', 'дело->ЕСТЬ', 'логично->ДОЛЖНЫ', 'считаю->ВЫСОКАЯ', 'сказал->ТАМ', 'сказал->ОТРЕГУЛИРОВАЛ', 'забываешь->СИДИШЬ', 'покупал->ХОЧУ', 'думаю->СОХРАНИТ', 'Оказалось->ПРОБЛЕМА', 'Брать->УСТРАНЕНЫ', 'узнать->СТОЯТ', 'Возможно->ПАДАТЬ', 'жалею->ВЫБРАЛ'}
22. cop frequncey:0.005 
+ exmple upos: ['ADV -> AUX', 'PRON -> VERB', 'ADJ -> VERB', 'PROPN -> AUX', 'NOUN -> VERB', 'PRON -> AUX', 'PROPN -> VERB', 'DET -> AUX', 'NUM -> AUX', 'ADJ -> AUX', 'NOUN -> AUX', 'VERB -> AUX', 'ADV -> VERB'] 
+ exmple values: {'лучшей->БЫЛА', 'панорамными->БЫЛИ', 'мониторе->БУДЕТ', 'интересно->БЫЛО', 'пользовании->БЫЛА', 'комплектации->ЕСТЬ', 'прекрасен->БЫЛ', 'предложение->БЫЛО', 'потоке->БЫТЬ', 'многих->ЕСТЬ', 'руле->ЕСТЬ', 'автомобиле->ЕСТЬ', 'дешевле->БУДЕТ', 'владельцем->БЫЛ', 'нужен->БЫЛ', 'больше->БУДЕТ', 'этого->БЫЛ', 'допом->БЫЛА', 'знаком->БЫЛ', 'неё->БЫЛА'}
23. appos frequncey:0.005 
+ exmple upos: ['NOUN -> NOUN', 'PROPN -> PROPN or NOUN', 'NOUN -> VERB or NUM', 'PROPN -> NUM', 'PRON -> PROPN', 'NOUN -> PROPN'] 
+ exmple values: {'3литра(->2013ГВ', 'КИА->К5', 'Маст->ХЭВ', 'Форд->ЭКСПЛОРЕР', 'пропан->БУТАН', 'Киа->К5', 'Мультимедиа->ЗВУК', 'ГАЗ->53', 'авто->ПУШКА', 'Тачка->ОГОНЬ', 'поездки->ПИТЕР', 'комплектации->ПРЕСТИЖ', 'климат->КОНТРОЛЬ', 'ЗиЛ->130', 'бмв->2012ГВ', 'Габариты->АВТОМОБИЛЬ', 'БМВ->Х6', 'бизнес->СЕДАН', 'резина->ЗИМА'}
24. flat:foreign frequncey:0.004 
+ exmple upos: ['PROPN -> PROPN', 'ADJ -> PROPN', 'NOUN -> X', 'PROPN -> NOUN', 'VERB -> PROPN', 'PROPN -> X', 'SYM -> X', 'X -> X', 'NOUN -> PROPN'] 
+ exmple values: {'комплектации->LINE+', 'воспользоваться->USB', 'пересесть->CHANGAN', 'ездила->ACCENT', 'телефона->BLUETOOTH', 'комплектации->GT', 'подключении->USB(A', 'авто->KIA', 'Комплектация->GT', 'авто->SEED', 'авто->SW', 'подключение->BLUETOOTH', 'Aplle->PLAY', 'Комплектация->LINE', 'ездила->HYUNDAI', 'Aplle->CAR', 'сабвуфер->BOSE'}
25. nummod:entity frequncey:0.004 
+ exmple upos: ['NOUN -> SYM or NOUN', 'PROPN -> SYM or NOUN', 'INTJ -> NUM', 'NOUN -> NUM', 'PROPN -> NUM', 'SYM -> NUM', 'X -> NUM'] 
+ exmple values: {'пользу->К5', '2л->2020Г', 'правилам->7.2Л', 'почтение->2', 'скорости->150КМ', 'Мазда->2Л', 'колёса->18', 'экто->2', 'ТО(->15000КМ', 'камри->2.', 'камри->4', 'салоне->27.04.21', 'качество->0', 'мае->2021', '~->14500', 'радиус->17', 'ТО->15', 'Движка->2.5', 'апреля->2021', '2.->4'}
26. acl frequncey:0.003 
+ exmple upos: ['NOUN -> NOUN', 'PRON -> NUM or ADV or VERB', 'NOUN -> VERB', 'PRON -> AUX or ADJ or NOUN', 'NOUN -> ADJ'] 
+ exmple values: {'Расход->ЕХАВ', 'тому->СТОЯТЬ', 'Музыка->ЗАЛЕ', 'багажник->ОТКРЫВАЮЩИЙСЯ', 'слухи->НЕТ', 'того->УБИВАЮТ', 'фастбек->НАПОМИНАЮЩИЙ', 'ощущение->САЛОН', 'тому->12', 'тем->ОБСЛУЖИВАЛ', 'то->БЫЛО', 'щелчок->ВЫРАЖЕННЫЙ', 'мысли->ВЕРНУТЬСЯ', 'багажник->СПРОЕКТИРОВАННЫЙ', 'том->МОЖНО', 'то->РЕШИЛ', 'версия->ПОЛНОПРИВОДНАЯ', 'того->БЫЛО', 'автомобилем->ИДУЩИМ', 'приборов->ОТОБРАЖАЮЩИХСЯ'}
27. aux frequncey:0.003 
+ exmple upos: ['VERB -> VERB', 'PRON -> AUX', 'AUX -> AUX', 'ADJ -> AUX', 'VERB -> AUX'] 
+ exmple values: {'брать->БУДУ', 'оставалась->БЫ', 'получил->БЫ', 'помнить->БЫЛО', 'стоять->БУДЕТ', 'заезжая->БЫЛА', 'меняться->БУДЕТ', 'удивляться->БУДУ', 'нужен->БЫ', 'дополнять->БУДУ', 'купил->БЫ', 'работать->БУДЕТ', 'просить->БУДЕТ', 'пересела->БЫ', 'жрать->БУДЕТ', 'неё->БЫ', 'подключаться->БУДЕТ', 'падать->БУДЕТ', 'ездит->БУДЕТ', 'Знал->БЫ'}
28. nsubj:pass frequncey:0.003 
+ exmple upos: ['VERB -> NOUN or PROPN or PRON'] 
+ exmple values: {'устранены->КОСЯКИ', 'предусмотрен->АВТОЗАПУСК', 'наблюдалось->НИЧЕГО', 'Установлена->ЗАЩИТА', 'предписано->ТОПЛИВО', 'Сделано->ТО0', 'чищены->ДОРОГИ', 'выставляется->ДИСТАНЦИЯ', 'выявлено->НЕДОСТАТКОВ', 'куплен->АВТО', 'затонирована->ЧАСТЬ', 'включается->ПАРКТРОНИК', 'поставлен->САБВУФЕР', 'включаются->КАМЕРЫ', 'сделано->ВСЁ', 'закрыта->ДВЕРЬ', 'компенсируется->ЭТО', 'переделано->ВСЕ', 'закрыта->ОНА', 'куплен->АВТОМОБИЛЬ'}
29. acl:relcl frequncey:0.003 
+ exmple upos: ['NOUN -> NOUN', 'DET -> VERB', 'PRON -> VERB', 'ADJ -> VERB', 'NOUN -> VERB or ADV', 'PROPN -> VERB or ADV', 'NOUN -> ADJ'] 
+ exmple values: {'функционал->СМОГ', 'авто->ПРОЕДЕТ', 'Мастер->СМОТРЕЛ', 'деньги->ОТДАЛ', 'машина->ТРЕБУЕТ', 'место->НЕТ', 'машину->ТЫСЯЧ', 'диагностику->ВЫЯВЛЕНО', 'вмятины->ПРИХОДИТСЯ', 'салона->БЛЕСТИТ', 'все->ПРОЛЕЗЕТ', 'Тем->РАЗДУМЫВАЕТ', 'гонщиков->ЛЮБЯТ', 'мнение->ОСНОВЫВАЕТСЯ', 'опции->НУЖНО', 'устройство->ПОДКЛЮЧАТЬСЯ', 'скорость->ВЕДЕТ', 'шумоизояцию->НЕТ', 'Kia->ЧУВСТВОВАЛ', 'того->ВИДЕЛ'}
30. nummod:gov frequncey:0.001 
+ exmple upos: ['NOUN -> NOUN', 'PRON -> ADV', 'NOUN -> ADV or NUM', 'PROPN -> NUM'] 
+ exmple values: {'тысяч->СЕМНАДЦАТЬ', 'км->ТРИ', 'груз->2-Х', 'лет->ДЕСЯТЬ', 'времени->СКОЛЬКО', 'лет->МНОГО', 'тысяч->ДЕСЯТЬ', 'камеры->МНОГО', 'Камри->НЕСКОЛЬКО', 'ряда->ТРИ', 'всего->БОЛЬШЕ', 'проблем->МЕНЬШЕ', 'отзывов->МНОГО', 'км.->ТЫСЯЧАХ', 'высоты->НЕМНОГО', 'опций->МНОГО', 'места->МНОГО', 'раз->МНОГО', 'режима->ТРИ', 'чемодана->ДВА'}
31. discourse frequncey:0.001 
+ exmple upos: ['ADV -> PART', 'PART -> PART', 'NOUN -> ADV', 'VERB -> ADV', 'PRON -> PART', 'VERB -> PRON', 'NUM -> ADP', 'NOUN -> PART', 'VERB -> PART', 'NOUN -> ADP'] 
+ exmple values: {'падает->ТЕМ', 'момент->ЗНАЧИТ', 'комфорт->В', 'машины->НУ', 'один->МЕЖДУ', 'впечатления->НУ', 'ломаться->ЗНАЧИТ', 'умеют->НУ', 'ездил->ЗНАЧИТ', 'пожелел->НУ', 'надо->НУ', 'так->НУ', 'мелочи->НУ', 'давайте->НУ', 'вот->НУ', 'это->НУ'}
32. flat:name frequncey:0.001 
+ exmple upos: ['PROPN -> PROPN', 'PRON -> PROPN'] 
+ exmple values: {'Питер->МОСКВА', 'Форд->МОНДЕО', 'Ниссан->АЛЬМЕРА', 'Ниссан->ТЕАНА', 'Тойота->КАМРИ', 'Рендж->РОВЕР', 'Хундай->АКЦЕНТ,', 'Хундай->ХЁНДЭ', 'Хундай->СОНАТА', 'Шевроле->АВЕО', 'Хёндэ->ТУССАН,', 'Форд->ЭСКЕЙП', 'Тойоту->КАМРИ', 'Шкода->ОКТАВИА', 'я->ТОМСКЕ', 'Шкода->РАПИД'}
33. orphan frequncey:0.001 
+ exmple upos: ['NOUN -> NOUN', 'PROPN -> NOUN', 'NOUN -> NUM', 'NUM -> ADJ', 'PROPN -> NUM', 'PRON -> NOUN', 'NOUN -> ADJ', 'ADV -> ADV'] 
+ exmple values: {'я->РУЛЬ', 'динамика->УДОВОЛЬСТВИЕ', '2023Недоработки->23', 'качества->23', '2023Заключение->23', 'Эльбрус->РУКИ', 'катализатор->ТЫС', 'я->ПЛАСТИК', 'почему->ТАК', 'расход->100', 'оно->ЗАПАХОМ', 'тормоза->КИВКА', 'А-92->50', 'ремонт->НЕДОРОГОЙ'}
34. expl frequncey:0.001 
+ exmple upos: ['ADJ -> PRON', 'NOUN -> PRON'] 
+ exmple values: {'выполнима->ЭТО', 'позор->ЭТО', 'дооснащение->ЭТО', 'безопасность->ЭТО', 'типа->ЭТО', 'хорошо->ВСЕ', 'минус->ЭТО', 'плюс->ЭТО', 'псевдопроходимость->ЭТО', 'ракета->ЭТО', 'гимнастика->ЭТО', 'потери->ЭТО', 'слова->ЭТО'}
35. compound frequncey:0.0 
+ exmple upos: ['NOUN -> NOUN', 'ADJ -> NUM', 'NUM -> SYM', 'ADJ -> ADJ', 'NOUN -> PROPN'] 
+ exmple values: {'точки->ЗРЕНИЯ', 'норм->РОК', '8->1.', 'красном->ОГНЕННО', 'ступенчатая->6-ТИ', 'торможения->ЭКСТРА', 'класс->БИЗНЕС', 'контроль->КЛИМАТ', 'мелких->СРЕДНЕ'}
36. flat frequncey:0.0 
+ exmple upos: ['ADJ -> NOUN', 'NUM -> PROPN or NOUN'] 
+ exmple values: {'9->ЯНВАРЯ', '21099,Тойота->КАЛДИНА', '23->ЯНВАРЯ'}
37. aux:pass frequncey:0.0 
+ exmple upos: ['VERB -> AUX'] 
+ exmple values: {'убита->БЫЛА', 'переделано->БЫЛО', 'лимитирован->БЫЛ', 'выставлен->БЫЛ', 'заменены->БЫЛИ'}
38. obl:tmod frequncey:0.0 
+ exmple upos: ['ADJ -> NOUN', 'VERB -> NOUN'] 
+ exmple values: {'подкрутил->РАЗ', 'охлаждается->ЛЕТОМ', 'нужно->ЗИМОЙ', 'диагностировалли->НЕДЕЛЮ', 'вела->ЗИМОЙ'}
39. vocative frequncey:0.0 
+ exmple upos: ['VERB -> NOUN', 'PART -> NOUN'] 
+ exmple values: {'приксуели->.РЕБАТКИ', 'попадаешь->САЛОН', 'вот->ГОСПОДА'}
40. csubj:pass frequncey:0.0 
+ exmple upos: ['VERB -> VERB'] 
+ exmple values: {'называемы->ВЕСТИ'}



#### UPOS:
* ADJ: adjective - прилагательное
* ADP: adposition - предлог
* ADV: adverb - наречие
* AUX: auxiliary - вспомогательный глагол
* CCONJ: coordinating conjunction - союз
* DET: determiner - определительное местоимение
* INTJ: interjection - междометие
* NOUN: noun - существительное
* NUM: numeral - числительное
* PART: particle - частица
* PRON: pronoun - местоимение
* PROPN: proper noun - собственное имя
* PUNCT: punctuation - знак препинания
* SCONJ: subordinating conjunction - подчинительный союз
* SYM: symbol - символ
* VERB: verb - глагол
* X: other - другое



### Реализация парсинга
#### Парсинг описания
* если встречаем связь amod то проверяем что head это существительное а само слово имеет upos ADJ то добавляем это как  (head, current_word)
* если встречаем nsubj проверяем что слово NOUN а head ADJ и добавляем  (current_word, head)
