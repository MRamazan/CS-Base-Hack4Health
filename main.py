import json
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import json
import os 
app = Flask(__name__)
CORS(app)


paragraph_dict = {
    "english": """The nature of human consciousness and the actual existence of free will stands as one of the most complex and controversial topics at the intersection of neuroscience, philosophy, and physics. Benjamin Libet's revolutionary experiments in the 1980s demonstrated that approximately 350 milliseconds before people thought they began making a conscious decision, electrical activity called "readiness potential" had already begun in the brain's motor cortex. This finding suggests that our free will might be merely an illusion, that our decisions may actually be made by unconscious neural processes before our conscious awareness kicks in. However, the situation is even more complex: contemporary neuroscientist Patrick Haggard's research shows that different regions of the brain can manipulate timing perception, meaning that even subjective experiences like "the moment of decision" can be deceptive. The collapse of the free will concept, which forms the foundation of moral responsibility, shakes the very foundations of our social order from justice systems to personal relationships. On the other hand, the uncertainty principle in quantum mechanics has convinced some scientists that non-deterministic processes might play a role in brain functions, but randomness doesn't rescue free will because a random decision cannot be considered free either. Compatibilist philosophers like Daniel Dennett reframe the problem, arguing that a will that is "free enough," even if not completely free, is sufficient for moral agency. Hard determinists like Sam Harris claim that through meditation and introspection, the illusion of selfhood can be dissolved, that the ego is merely a construction, and that real experience is a fluid, non-centered process. This debate is not merely academic; as artificial intelligence develops, practical questions arise about whether machines can gain consciousness, whether conscious experience can emerge from computational processes, and what the moral status of human-like artificial beings would be. What David Chalmers calls the "hard problem" – the subjective quality of conscious experience, the redness of red, the painfulness of pain – still stands as an unexplained mystery of how it emerges from neural activity. Contemporary research in global workspace theory and integrated information theory attempts to quantify consciousness mathematically, yet fails to bridge the explanatory gap between objective neural firing patterns and subjective phenomenological experience. The implications extend beyond theoretical curiosity into practical domains: if consciousness is purely material, can it be uploaded, copied, or transferred between substrates? Would a perfect neural simulation of your brain be you, or merely a copy that thinks it's you? These questions become increasingly urgent as brain-computer interfaces advance and the possibility of mind uploading transitions from science fiction to serious scientific consideration.""",
    "turkish": """İnsan bilincinin doğası ve serbest iradenin gerçek varlığı, nörobilim, felsefe ve fizik alanlarının kesişim noktasında duran en karmaşık ve tartışmalı konulardan biridir. Benjamin Libet'in 1980'lerde yaptığı devrim niteliğindeki deneyler, insanların bilinçli bir karar vermeye başladıklarını düşündükleri andan yaklaşık 350 milisaniye önce, beynin motor korteksinde "hazırlık potansiyeli" adı verilen elektriksel aktivitenin başladığını gösterdi. Bu bulgu, özgür irademizin sadece bir yanılsama olabileceğini, kararlarımızın aslında bilinçli farkındalığımızdan önce bilinçsiz nöral süreçler tarafından alınmış olabileceğini öne sürüyor. Ancak durum bundan da karmaşık: çağdaş nörobilimci Patrick Haggard'ın araştırmaları, beynin farklı bölgelerinin zamanlama algısını manipüle edebildiğini, dolayısıyla "karar verme anı" gibi subjektif deneyimlerin bile yanıltıcı olabileceğini gösteriyor. Ahlaki sorumluluk kavramının temeli olan özgür irade fikrinin çökmesi, adalet sisteminden kişisel ilişkilere kadar toplumsal düzenimizin temellerini sarsar. Öte yandan, kuantum mekaniğindeki belirsizlik ilkesi bazı bilim insanlarını deterministik olmayan süreçlerin beyin fonksiyonlarında rol oynayabileceğine ikna etti, ancak rastgelelik özgür iradeyi kurtarmaz çünkü rastgele olan bir karar da özgür sayılamaz. Daniel Dennett gibi uyumcu filozoflar ise sorunu yeniden çerçeveleyerek, tamamen özgür olmasa bile "yeterince özgür" olan bir iradenin ahlaki eylemlilik için yeterli olduğunu savunuyor. Sam Harris gibi sert deterministler ise meditasyon ve introspeksiyon yoluyla kendilik yanılsamasının çözülebileceğini, ego'nun sadece bir inşa olduğunu ve gerçek deneyimin akışkan, merkezi olmayan bir süreç olduğunu iddia ediyor. Bu tartışma sadece akademik değil; yapay zeka geliştikçe makinelerin bilinç kazanıp kazanamayacağı, bilinçli deneyimin hesaplamalı süreçlerden ortaya çıkıp çıkamayacağı ve insan benzeri yapay varlıkların ahlaki statüsünün ne olacağı gibi pratik sorular gündeme geliyor. David Chalmers'ın "zor problem" dediği bilinçli deneyimin subjektif kalitesi - kırmızının kırmızılığı, acının acılığı - hâlâ nöral aktiviteden nasıl ortaya çıktığı açıklanamayan bir gizem olarak duruyor.""",
    "deutsch": """Die Natur des menschlichen Bewusstseins und die tatsächliche Existenz des freien Willens stehen als eines der komplexesten und kontroversesten Themen am Schnittpunkt von Neurowissenschaft, Philosophie und Physik. Benjamin Libets revolutionäre Experimente in den 1980er Jahren zeigten, dass etwa 350 Millisekunden bevor Menschen dachten, sie würden eine bewusste Entscheidung treffen, bereits elektrische Aktivität namens "Bereitschaftspotential" im motorischen Kortex des Gehirns begonnen hatte. Diese Erkenntnis legt nahe, dass unser freier Wille möglicherweise nur eine Illusion ist, dass unsere Entscheidungen tatsächlich von unbewussten neuralen Prozessen getroffen werden, bevor unser bewusstes Bewusstsein einsetzt. Die Situation ist jedoch noch komplexer: die Forschung des zeitgenössischen Neurowissenschaftlers Patrick Haggard zeigt, dass verschiedene Hirnregionen die Zeitwahrnehmung manipulieren können, was bedeutet, dass selbst subjektive Erfahrungen wie "der Moment der Entscheidung" täuschend sein können. Der Zusammenbruch des Konzepts des freien Willens, das die Grundlage moralischer Verantwortung bildet, erschüttert die Fundamente unserer gesellschaftlichen Ordnung von Justizsystemen bis hin zu persönlichen Beziehungen. Andererseits hat das Unschärfeprinzip in der Quantenmechanik einige Wissenschaftler davon überzeugt, dass nicht-deterministische Prozesse eine Rolle in Gehirnfunktionen spielen könnten, aber Zufälligkeit rettet den freien Willen nicht, weil eine zufällige Entscheidung auch nicht als frei betrachtet werden kann. Kompatibilistische Philosophen wie Daniel Dennett rahmen das Problem neu und argumentieren, dass ein Wille, der "frei genug" ist, auch wenn er nicht vollständig frei ist, für moralische Handlungsfähigkeit ausreicht. Harte Deterministen wie Sam Harris behaupten, dass durch Meditation und Introspektion die Illusion der Selbstheit aufgelöst werden kann, dass das Ego nur eine Konstruktion ist und dass echte Erfahrung ein fließender, nicht-zentrierter Prozess ist. Diese Debatte ist nicht nur akademisch; während sich künstliche Intelligenz entwickelt, entstehen praktische Fragen darüber, ob Maschinen Bewusstsein erlangen können, ob bewusste Erfahrung aus rechnerischen Prozessen entstehen kann und welchen moralischen Status menschenähnliche künstliche Wesen hätten. Was David Chalmers das "schwere Problem" nennt – die subjektive Qualität bewusster Erfahrung, die Röte des Rot, die Schmerzhaftigkeit des Schmerzes – steht immer noch als unerklärtes Mysterium da, wie es aus neuraler Aktivität entsteht. Zeitgenössische Forschung in der Global-Workspace-Theorie und der integrierten Informationstheorie versucht, Bewusstsein mathematisch zu quantifizieren, schafft es jedoch nicht, die Erklärungslücke zwischen objektiven neuralen Feuermustern und subjektiver phänomenologischer Erfahrung zu überbrücken. Die Implikationen erstrecken sich über theoretische Neugier hinaus in praktische Bereiche: wenn Bewusstsein rein materiell ist, kann es hochgeladen, kopiert oder zwischen Substraten übertragen werden? Wäre eine perfekte neurale Simulation Ihres Gehirns Sie selbst oder nur eine Kopie, die denkt, sie wäre Sie? Diese Fragen werden zunehmend dringlicher, während sich Gehirn-Computer-Schnittstellen weiterentwickeln und die Möglichkeit des Mind-Uploading von Science-Fiction zu ernsthafter wissenschaftlicher Betrachtung übergeht.""",
    "japanese": """人間の意識の本質と自由意志の実在は、神経科学、哲学、物理学の交差点に位置する最も複雑で論争的なトピックの一つである。1980年代のベンジャミン・リベットの革命的な実験は、人々が意識的な決定を下し始めたと思う約350ミリ秒前に、脳の運動皮質で「準備電位」と呼ばれる電気活動がすでに始まっていることを示した。この発見は、私たちの自由意志が単なる錯覚である可能性を示唆し、私たちの決定が実際には意識的認識が働く前に無意識の神経プロセスによって行われている可能性があることを示している。しかし、状況はさらに複雑である：現代の神経科学者パトリック・ハガードの研究は、脳の異なる領域が時間知覚を操作できることを示しており、つまり「決定の瞬間」のような主観的体験でさえ欺瞞的である可能性があることを意味している。道徳的責任の基盤を形成する自由意志概念の崩壊は、司法制度から個人的関係まで、私たちの社会秩序の根本を揺るがす。一方で、量子力学の不確定性原理は、非決定論的プロセスが脳機能で役割を果たす可能性があると一部の科学者を確信させたが、ランダム性は自由意志を救わない。なぜなら、ランダムな決定も自由とは考えられないからである。ダニエル・デネットのような両立論者の哲学者は問題を再構成し、完全に自由でなくても「十分に自由な」意志が道徳的主体性には十分であると主張している。サム・ハリスのような強硬な決定論者は、瞑想と内省を通じて自己の錯覚を解消でき、エゴは単なる構築物であり、真の体験は流動的で中心のないプロセスであると主張している。この議論は単に学術的なものではない。人工知能が発展するにつれて、機械が意識を獲得できるか、意識的体験が計算プロセスから生まれることができるか、人間のような人工的存在の道徳的地位がどうなるかという実践的な問題が生じている。デビッド・チャルマーズが「困難な問題」と呼ぶもの—意識的体験の主観的質、赤の赤らしさ、痛みの痛ましさ—は、それが神経活動からどのように生まれるかの未解明の謎として依然として立ちはだかっている。グローバルワークスペース理論と統合情報理論の現代研究は意識を数学的に定量化しようと試みるが、客観的な神経発火パターンと主観的現象学的体験の間の説明ギャップを埋めることには失敗している。その含意は理論的好奇心を超えて実践的領域に及ぶ：もし意識が純粋に物質的なら、それはアップロード、コピー、基質間転送が可能なのか？あなたの脳の完璧な神経シミュレーションはあなた自身なのか、それとも自分がそうだと思っているコピーなのか？これらの質問は、脳コンピューターインターフェースが進歩し、マインドアップロードの可能性がサイエンスフィクションから真剣な科学的考察に移行するにつれて、ますます緊急性を増している。さらに、意識の計算理論は機械的な情報処理と現象的体験の間の根本的な違いを説明できず、哲学的ゾンビの思考実験—物理的に人間と同一だが意識体験を欠く存在—は意識の還元不可能性について深刻な疑問を提起している。""",
    "french": """La nature de la conscience humaine et l'existence réelle du libre arbitre constituent l'un des sujets les plus complexes et controversés à l'intersection des neurosciences, de la philosophie et de la physique. Les expériences révolutionnaires de Benjamin Libet dans les années 1980 ont démontré qu'environ 350 millisecondes avant que les gens pensent commencer à prendre une décision consciente, une activité électrique appelée « potentiel de préparation » avait déjà commencé dans le cortex moteur du cerveau. Cette découverte suggère que notre libre arbitre pourrait n'être qu'une illusion, que nos décisions pourraient en réalité être prises par des processus neuraux inconscients avant que notre conscience ne s'active. Cependant, la situation est encore plus complexe : les recherches du neuroscientifique contemporain Patrick Haggard montrent que différentes régions du cerveau peuvent manipuler la perception temporelle, ce qui signifie que même les expériences subjectives comme « le moment de la décision » peuvent être trompeuses. L'effondrement du concept de libre arbitre, qui forme la base de la responsabilité morale, ébranle les fondements mêmes de notre ordre social, des systèmes judiciaires aux relations personnelles. D'autre part, le principe d'incertitude en mécanique quantique a convaincu certains scientifiques que des processus non-déterministes pourraient jouer un rôle dans les fonctions cérébrales, mais la randomité ne sauve pas le libre arbitre car une décision aléatoire ne peut pas non plus être considérée comme libre. Les philosophes compatibilistes comme Daniel Dennett recadrent le problème en argumentant qu'une volonté « suffisamment libre », même si elle n'est pas complètement libre, est suffisante pour l'agentivité morale. Les déterministes durs comme Sam Harris affirment qu'à travers la méditation et l'introspection, l'illusion de l'individualité peut être dissoute, que l'ego n'est qu'une construction, et que l'expérience réelle est un processus fluide et non-centré. Ce débat n'est pas seulement académique ; alors que l'intelligence artificielle se développe, des questions pratiques émergent sur la possibilité pour les machines d'acquérir une conscience, si l'expérience consciente peut émerger de processus computationnels, et quel serait le statut moral d'êtres artificiels semblables aux humains. Ce que David Chalmers appelle le « problème difficile » – la qualité subjective de l'expérience consciente, la rougeur du rouge, la douleur de la douleur – demeure un mystère inexpliqué de comment cela émerge de l'activité neurale. La recherche contemporaine en théorie de l'espace de travail global et en théorie de l'information intégrée tente de quantifier mathématiquement la conscience, mais échoue à combler le fossé explicatif entre les patterns objectifs de décharge neuronale et l'expérience phénoménologique subjective. Les implications s'étendent au-delà de la curiosité théorique vers des domaines pratiques : si la conscience est purement matérielle, peut-elle être téléchargée, copiée, ou transférée entre substrats ? Une simulation neurale parfaite de votre cerveau serait-elle vous-même, ou simplement une copie qui pense être vous ? Ces questions deviennent de plus en plus urgentes alors que les interfaces cerveau-ordinateur progressent et que la possibilité du téléchargement mental passe de la science-fiction à la considération scientifique sérieuse. De plus, les théories computationnelles de la conscience échouent à expliquer la différence fondamentale entre le traitement mécanique de l'information et l'expérience phénoménale, et l'expérience de pensée du zombie philosophique – un être physiquement identique aux humains mais dépourvu d'expérience consciente – soulève de sérieuses questions sur l'irréductibilité de la conscience.""",
}

first_question_dict = {
    "english": """What does "readiness potential" refer to in neuroscience?""",
    "turkish": """Nörobilimde "hazırlık potansiyeli" terimi neyi ifade eder?""",
    "deutsch": """Was bezeichnet "Bereitschaftspotential" in der Neurowissenschaft?""",
    "japanese": """神経科学における「準備電位」とは何を指しますか？""",
    "french": """Que désigne le « potentiel de préparation » en neurosciences ?""",
}

second_question_dict = {
    "english": """Why doesn't randomness rescue free will in a deterministic universe?""",
    "turkish": """Deterministik bir evrende rastgelelik neden özgür iradeyi kurtarmaz?""",
    "deutsch": """Warum rettet Zufälligkeit den freien Willen in einem deterministischen Universum nicht?""",
    "japanese": """決定論的宇宙でランダム性が自由意志を救わないのはなぜですか？""",
    "french": """Pourquoi la randomité ne sauve-t-elle pas le libre arbitre dans un univers déterministe ?""",
}

third_question_dict = {
    "english": """Which philosopher advocates for the concept of "free enough" will?""",
    "turkish": """"Yeterince özgür" irade kavramını savunan filozof kimdir?""",
    "deutsch": """Welcher Philosoph vertritt das Konzept des "frei genug" Willens?""",
    "japanese": """「十分に自由な」意志の概念を提唱する哲学者は誰ですか？""",
    "french": """ Quel philosophe défend le concept de volonté « suffisamment libre » ?""",
}

fourth_question_dict = {
    "english": """What does the "hard problem" regarding consciousness attempt to explain?""",
    "turkish": """Bilinçle ilgili "zor problem" neyi açıklamaya çalışır?""",
    "deutsch": """Was versucht das "schwere Problem" bezüglich des Bewusstseins zu erklären?""",
    "japanese": """意識に関する「困難な問題」は何を説明しようとしますか？""",
    "french": """Que tente d'expliquer le « problème difficile » concernant la conscience ?""",
}

fifth_question_dict = {
    "english": """What is the significance of this topic in the field of artificial intelligence?""",
    "turkish": """Bu konunun yapay zeka alanındaki önemi nedir?""",
    "deutsch": """Was ist die Bedeutung dieses Themas im Bereich der künstlichen Intelligenz?""",
    "japanese": """このトピックの人工知能分野における重要性は何ですか？""",
    "french": """Quelle est la signification de ce sujet dans le domaine de l'intelligence artificielle ?""",
}

first_option_dict = {
    "english": ["The brain's general electrical activity level",
                "Electrical activity in motor cortex that begins before conscious decision",
                "Brain waves during sleep",
                "Neural measurement showing learning capacity"],
    "turkish": ["Beyindeki genel elektriksel aktivite seviyesi",
                "Motor kortekste bilinçli karar öncesinde başlayan elektriksel aktivite",
                "Uyku sırasındaki beyin dalgalar",
                "Öğrenme kapasitesini gösteren nöral ölçüm"],
    "deutsch": ["Das allgemeine elektrische Aktivitätsniveau des Gehirns",
                "Elektrische Aktivität im motorischen Kortex vor bewusster Entscheidung",
                "Gehirnwellen während des Schlafs",
                "Neurale Messung der Lernfähigkeit"],
    "french": ["Le niveau général d'activité électrique du cerveau",
               "L'activité électrique dans le cortex moteur qui commence avant la décision consciente",
               "Les ondes cérébrales pendant le sommeil",
               "Une mesure neurale montrant la capacité d'apprentissage"]
}

second_option_dict = {
    "english": ["Because randomness is physically impossible",
                "Because a random decision also cannot be considered controllable",
                "Because quantum mechanics is a false theory",
                " Because randomness is only an illusion"],
    "turkish": ["Çünkü rastgelelik fiziksel olarak imkansızdır",
                "Çünkü rastgele olan bir karar da kontrol edilebilir sayılamaz",
                "Çünkü kuantum mekaniği yanlış bir teoridir",
                "Çünkü rastgelelik sadece illüzyondur"],
    "deutsch": ["Weil Zufälligkeit physikalisch unmöglich ist",
                "Weil eine zufällige Entscheidung auch nicht als kontrollierbar betrachtet werden kann",
                "Weil die Quantenmechanik eine falsche Theorie ist",
                "Weil Zufälligkeit nur eine Illusion ist"],
    "french": ["Parce que la randomité est physiquement impossible",
               "Parce qu'une décision aléatoire ne peut pas non plus être considérée comme contrôlable",
               "Parce que la mécanique quantique est une théorie fausse",
               "Parce que la randomité n'est qu'une illusion"],
}

third_option_dict = {
    "english": ["Sam Harris", "David Chalmers", "Patrick Haggard", "Daniel Dennett"],
    "turkish": ["Sam Harris", "David Chalmers", "Patrick Haggard", "Daniel Dennett"],
    "deutsch": ["Sam Harris", "David Chalmers", "Patrick Haggard", "Daniel Dennett"],
    "japanese": ["Sam Harris", "David Chalmers", "Patrick Haggard", "Daniel Dennett"],
    "french": ["Sam Harris", "David Chalmers", "Patrick Haggard", "Daniel Dennett"],
}

fourth_option_dict = {
    "english": ["How the brain works",
                "How subjective experience emerges from neural activity",
                "How to develop artificial intelligence",
                "How moral decisions are made"],
    "deutsch": ["Wie das Gehirn funktioniert",
                "Wie subjektive Erfahrung aus neuraler Aktivität entsteht",
                "Wie man künstliche Intelligenz entwickelt",
                "Wie moralische Entscheidungen getroffen werden"],
    "turkish": ["Beynin nasıl çalıştığını",
                "Subjektif deneyimin nöral aktiviteden nasıl ortaya çıktığını",
                "Yapay zekanın nasıl geliştirileceğini",
                "Ahlaki kararların nasıl verildiğini"],
    "french": ["Comment le cerveau fonctionne",
               "Comment l'expérience subjective émerge de l'activité neurale",
               "Comment développer l'intelligence artificielle",
               "Comment les décisions morales sont prises"],
}

fifth_option_dict = {
    "english": ["It is merely a theoretical curiosity",
                "It creates practical questions about machine consciousness and moral status",
                "It is important for increasing computer speed",
                "It is necessary for developing human-machine interfaces"],
    "deutsch": ["Es ist nur theoretische Neugier",
                "Es schafft praktische Fragen über Maschinenbewusstsein und moralischen Status",
                "Es ist wichtig für die Erhöhung der Computergeschwindigkeit",
                "Es ist notwendig für die Entwicklung von Mensch-Maschine-Schnittstellen"],
    "turkish": ["Sadece teorik bir merak konusudur",
                "Makinelerin bilinç kazanması ve ahlaki statüleri konusunda pratik sorular yaratır",
                "Bilgisayar hızını artırmak için önemlidir",
                "İnsan-makine arayüzlerini geliştirmek için gereklidir"],
    "french": ["C'est simplement une curiosité théorique",
               "Cela crée des questions pratiques sur la conscience des machines et le statut moral",
               "C'est important pour augmenter la vitesse des ordinateurs",
               "C'est nécessaire pour développer les interfaces homme-machine"],
}

answers = [1, 1, 3, 1, 1]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/paragraph/<language>')
def get_paragraph(language):
    if language in paragraph_dict:
        return jsonify({
            'success': True,
            'paragraph': paragraph_dict[language]
        })
    else:
        return jsonify({
            'success': False,
            'message': 'Language not found'
        })


@app.route('/api/questions/<language>')
def get_questions(language):
    questions = [
        {
            'question': first_question_dict.get(language, ''),
            'options': first_option_dict.get(language, ['', '', '', ''])
        },
        {
            'question': second_question_dict.get(language, ''),
            'options': second_option_dict.get(language, ['', '', '', ''])
        },
        {
            'question': third_question_dict.get(language, ''),
            'options': third_option_dict.get(language, ['', '', '', ''])
        },
        {
            'question': fourth_question_dict.get(language, ''),
            'options': fourth_option_dict.get(language, ['', '', '', ''])
        },
        {
            'question': fifth_question_dict.get(language, ''),
            'options': fifth_option_dict.get(language, ['', '', '', ''])
        }
    ]

    return jsonify({
        'success': True,
        'questions': questions
    })



score_messages = {
        0: {
            'title': 'No Attention',
            'message': """It looks like you had difficulty focusing or understanding the material — and that's totally okay. These topics are complex and require time. Try reading at a slower pace or breaking the text into smaller parts. Every expert begins somewhere.""",
            "suggestions": [
                "Try limiting social media during focused hours.",
                "Follow a simple, consistent daily routine.",
                "Keep a short log of what pulls your attention away.",
                "Focusing on one task at a time might improve clarity."
            ]
        },
        1: {
            'title': 'Very Weak Attention',
            'message': """You’ve started to pick up a few basic ideas, which is a good start. With just a bit more focus and curiosity, you'll begin to connect the bigger picture. Keep going — progress is happening.""",
            "suggestions": [
                "Reading aloud may help keep your mind active.",
                "Planning your day with a checklist could guide your focus.",
                "Sticking to regular sleep patterns supports concentration.",
                "Lighter meals can help you stay mentally sharp.",
                "Turning off phone notifications might reduce interruptions.",
                "Choosing healthier snacks may support brain function."
            ]
        },
        2: {
            'title': 'Poor Attention',
            'message': """You’ve grasped some key points — that’s a positive sign. While a few details may have been missed, you’re clearly engaging with the content. A second reading or asking follow-up questions might help solidify your understanding.""",
            "suggestions": [
                "Take a quick walk before starting to refresh your mind.",
                "Try avoiding phone use right after waking up.",
                "Taking breaks regularly can help prevent fatigue.",
                "Focusing on one task at a time may boost productivity.",
                "Limit your daily goals to 2–3 key tasks."
            ]
        },
        3: {
            'title': 'Good Attention',
            'message': """Well done! You understood most of the material, which shows solid focus and critical thinking. You're now ready to explore more complex ideas about consciousness and free will. Keep going — you’re growing steadily.""",
            "suggestions": [
                "Keep a bottle of water nearby to stay alert.",
                "Try short memory or focus games to train attention.",
                "Limit passive scrolling when you’re working.",
                "Eating away from your desk can refresh your mental state.",
                "Celebrate small wins to stay motivated."
            ]
        },
        4: {
            'title': 'Advanced Attention',
            'message': """Great work — you demonstrated a clear and thoughtful understanding of the text. You're beginning to notice deeper connections and details. This is a strong level of attention that sets the stage for deep learning.""",
            "suggestions": [
                "Plan your next day the night before for a calm start.",
                "Clarify your goals — clear direction boosts efficiency.",
                "Read regularly to maintain and strengthen focus.",
                "Balance intense work with meaningful rest."
            ]
        },
        5: {
            'title': 'Exceptional Attention',
            'message': """Excellent! Your responses show not only strong attention but genuine insight. You seem to understand the topic at both a scientific and philosophical level. Keep nurturing this rare level of focus — it’s a real strength.""",
            "suggestions": [
                "Keep using the focus methods that work well for you.",
                "Supporting others with their focus can reinforce your own.",
                "Protect your attention — even strong focus needs care.",
                "Try to reduce late-night screen time for better mental clarity."
            ]
        },
    }

@app.route('/api/submit', methods=['POST'])
def submit_answers():
    data = request.get_json()
    user_answers = data.get('answers', [])

    score = 0
    for i, answer in enumerate(user_answers):
        if i < len(answers) and answer == answers[i]:
            score += 1

    score_info = score_messages.get(score, score_messages[0])

    return jsonify({
        'success': True,
        'score': score,
        'total': len(answers),
        'percentage': round((score / len(answers)) * 100, 1),
        'score_title': score_info['title'],
        'score_message': score_info['message'],
        'suggestions': score_info['suggestions'],
        'correct_answers': answers  # Bu satırı ekle
    })

@app.route('/api/languages')
def get_languages():
    return jsonify({
        'success': True,
        'languages': list(paragraph_dict.keys()) if paragraph_dict else ['english', 'turkish', 'deutsch', 'japanese',
                                                                         'french']
    })

def main():
    app.run(debug=True, host='0.0.0.0', port=5000)
    
if __name__ == '__main__':
    main()
