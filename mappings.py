import json

# Create a dictionary with unique mappings
hinglish_mappings = {

    "mai": "i",
    "maine": "i have",
    "mera": "my", 
    "mere": "my",
    "aap": "you",
    "apka": "your",
    "apke": "your",
    "uska": "his/her",
    "unka": "their",
    "hum": "we",
    "humko": "to us",

    # Basic Verbs
    "hai": "is",
    "hain": "are", 
    "tha": "was",
    "thi": "was",
    "kar": "do",
    "kiya": "did",
    "karne": "to do",
    "karke": "after doing",
    "raha": "doing",
    "rahe": "doing", 
    "rahi": "doing",
    "bhej": "send",
    "bheja": "sent",
    "bhejne": "to send",
    "diya": "gave",
    "dena": "give", 
    "deke": "after giving",
    "liya": "took",
    "lena": "take",
    "leke": "after taking",
    "gaya": "went",
    "gayi": "went",
    "jana": "go",

    # Question Words
    "kya": "what",
    "kaise": "how",
    "kyun": "why",
    "kyu": "why",
    "kahan": "where",
    "kaha": "where", 
    "kaun": "who",
    "kab": "when",
    "kitna": "how much",

    # Basic Words
    "nahi": "no",
    "nahin": "no",
    "na": "no",
    "mat": "don't",
    "aur": "and",
    "ki": "that",
    "ko": "to",
    "se": "from",
    "par": "on",
    "pe": "on",
    "ke": "of",
    "ka": "of",
    "tak": "until",
    "saath": "with",

    # Time Related
    "din": "day",
    "raat": "night", 
    "subah": "morning",
    "sham": "evening",
    "aaj": "today",
    "kal": "tomorrow/yesterday",
    "parso": "day after/before",
    "abhi": "now",
    "samay": "time",
    "waqt": "time",
    "mahina": "month",
    "saal": "year",
    "hafta": "week",
    "jaldi": "early",
    "der": "late",

    # Financial Terms
    "paise": "money",
    "paisa": "money",
    "pai": "money",
    "rupay": "rupees",
    "rupaye": "rupees",
    "bank": "bank",
    "khata": "account",
    "khaata": "account",
    "jama": "deposit",
    "jamaa": "deposit",
    "nikasi": "withdrawal",
    "byaj": "interest",
    "loan": "loan",
    "karz": "loan",
    "uddhar": "loan",
    "karza": "debt",
    "EMI": "EMI",
    "balance": "balance",
    "amount": "amount",
    "rakam": "amount",
    "rashii": "amount",
    "payment": "payment",
    "bhugtan": "payment",
    "transaction": "transaction",
    "len-den": "transaction",
    "transfer": "transfer",

    # Status Indicators
    "pending": "pending",
    "complete": "complete",
    "poora": "complete",
    "purna": "complete",
    "adhura": "incomplete",
    "cancel": "cancel",
    "processing": "processing",
    "prakriyarat": "processing",
    "failed": "failed",
    "vifal": "failed",
    "asfal": "failed",
    "success": "success", 
    "safal": "successful",
    "band": "closed",
    "khula": "open",
    "chalu": "active",
    "sachiv": "active",
    "nirjiv": "inactive",
    "suspended": "suspended",
    "blocked": "blocked",
    "freeze": "freeze",
    "hold": "hold",

    # Tech Terms
    "mobile": "mobile",
    "phone": "phone",
    "number": "number",
    "whatsapp": "whatsapp",
    "message": "message",
    "sandesh": "message",
    "call": "call",
    "otp": "otp",
    "account": "account",
    "link": "link",
    "password": "password",
    "login": "login",
    "pravesh": "login",
    "logout": "logout",
    "screenshot": "screenshot",
    "profile": "profile",
    "update": "update",
    "download": "download",
    "upload": "upload",
    "website": "website",
    "cyber": "cyber",
    "internet": "internet",
    "data": "data",

    # Document Related
    "dastavej": "document",
    "kagaz": "paper",
    "copy": "copy",
    "form": "form",
    "application": "application",
    "avedan": "application",
    "darkhast": "application",
    "photo": "photo",
    "chitra": "image",
    "proof": "proof",
    "praman": "proof",
    "saboot": "evidence",
    "record": "record",

    # Location Terms
    "jagah": "place",
    "sthan": "location",
    "pata": "address",
    "sheher": "city",
    "shahar": "city",
    "gaon": "village",
    "desh": "country",
    "rajya": "state",
    "zila": "district",
    "kshetra": "area",
    "mohalla": "neighborhood",
    "sadak": "road",
    "ghar": "home",
    "daftar": "office",

    # Legal Terms
    "vakil": "lawyer",
    "kanoon": "law",
    "adalat": "court",
    "nyayalay": "court",
    "police": "police",
    "thana": "police station",
    "fir": "complaint",
    "jurm": "crime",

    # Status Descriptors
    "kharab": "bad",
    "theek": "okay",
    "thik": "okay",
    "sahi": "correct",
    "galat": "wrong",
    "acha": "good",
    "achha": "good",
    "bura": "bad",
    "mushkil": "difficult",
    "aasan": "easy",
    "sambhav": "possible",

    # Communication Terms
    "baat": "talk",
    "soochna": "information",
    "suchna": "information",
    "jankari": "information",
    "sampark": "contact",
    "vishay": "subject",
    "uttar": "reply",
    "javab": "response",
    "samvad": "conversation",
    "topic": "topic",
    "nivedhan": "request",

    # Urgency Indicators
    "jaldi": "quick",
    "shighra": "quick",
    "turant": "immediate",
    "tatkal": "immediate",
    "twarit": "prompt",
    "avashyak": "necessary",
    "mahatvapurn": "important",
    "zaruri": "urgent",
    "abhivilamba": "urgent",

    # Support Related
    "sahayata": "help",
    "sahayta": "assistance",
    "madad": "help",
    "margdarshan": "guidance",
    "salah": "advice",
    "sujhav": "suggestion",
    "samadhan": "solution",

    # Security Terms
    "surakshit": "secure",
    "hack": "hack",
    "virus": "virus",
    "bachav": "protection",
    "khatra": "danger",
    "jokhim": "risk",
    "chetan": "alert",
    "savdhan": "careful",
    "dhyan": "attention",

    # Error Related
    "truti": "error",
    "galti": "mistake",
    "bhool": "mistake",
    "samasya": "problem",
    "gadbad": "problem",
    "kharabi": "fault",
    "dosh": "fault",
    "khami": "defect",
    "nuksan": "damage",

    # Warning Terms
    "chetavni": "warning",
    "khabardar": "beware",
    "ruko": "stop",
    "mana": "forbidden",
    "pratiband": "restriction",
    "rok": "barrier",

    # Authentication Terms
    "pramanit": "verified",
    "satya": "true",
    "asatya": "false",
    "satyapan": "verification",
    "pehchan": "identity",
    "parichay": "introduction",
    "anumati": "permission",
    "swikrit": "approved",

    # Recovery Terms
    "vapasi": "recovery",
    "wapas": "return",
    "prapti": "receipt",
    "praptyankh": "recovery",
    "punah": "again",
    "dobara": "again",
    "punarprapat": "recover",
    "reset": "reset",
    "restore": "restore",


    # Financial Terms
    'upi': 'unified payments interface',
    'kyc': 'know your customer',
    'ifsc': 'indian financial system code',
    'atm': 'automated teller machine',
    'a/c': 'account',
    'acc': 'account',
    'acnt': 'account',
    'amt': 'amount',
    'bal': 'balance',
    'txn': 'transaction',
    'trn': 'transaction',
    'ref': 'reference',

    # Common words
    'mein': 'in',
    'hai': 'is',
    'kya': 'what',
    'aap': 'you',
    'kar': 'do',
    'raha': 'doing',
    'nahi': 'no',
    'kuch': 'some',
    'mere': 'my',
    'mera': 'my',
    'aur': 'and',
    'ko': 'to',

    # Cyber crime related
    'hack': 'hacked',
    'scam': 'scammed', 
    'fraud': 'fraudulent',
    'fake': 'false',
    'cheat': 'cheated',
    'block': 'blocked',
    'complaint': 'complaint',
    'dhoka': 'fraud',
    'chori': 'theft',
    'surakshit': 'secure', 'hack': 'hack', 'virus': 'virus',
    'bachav': 'protection', 'khatra': 'danger', 'jokhim': 'risk',
    'chetan': 'alert', 'savdhan': 'careful', 'dhyan': 'attention',
    
    # Process verbs
    'kholna': 'open', 'khol': 'open', 'khola': 'opened',
    'bandh': 'close', 'rokna': 'stop', 'roka': 'stopped',
    'milna': 'receive', 'mila': 'received', 'mil': 'get',
    
    # Authentication terms
    'pramanit': 'verified', 'satya': 'true', 'asatya': 'false',
    'satyapan': 'verification', 'pehchan': 'identity', 'parichay': 'introduction',
    'pravesh': 'entry', 'anumati': 'permission', 'swikrit': 'approved',
    
    # Error messages
    'truti': 'error', 'galti': 'mistake', 'bhool': 'mistake',
    'samasya': 'problem', 'gadbad': 'problem', 'kharabi': 'fault',
    'dosh': 'fault', 'khami': 'defect', 'nuksan': 'damage',
    
    # Warning terms
    'chetavni': 'warning', 'khabardar': 'beware', 'savdhan': 'alert',
    'ruko': 'stop', 'mat': 'don\'t', 'nahi': 'no',
    'mana': 'forbidden', 'pratiband': 'restriction', 'rok': 'barrier',
    
    # Support related
    'sahayata': 'support', 'madad': 'help', 'sahayta': 'assistance',
    'margdarshan': 'guidance', 'salah': 'advice', 'sujhav': 'suggestion',
    'samadhan': 'solution', 'jawab': 'answer', 'uttar': 'response',
    
    # Account status
    'sachiv': 'active', 'nirjiv': 'inactive', 'suspended': 'suspended',
    'blocked': 'blocked', 'freeze': 'freeze', 'hold': 'hold',
    'regular': 'regular', 'vishesh': 'special', 'sadharan': 'normal',
    
    # Notification terms
    'suchana': 'notification', 'sanket': 'signal', 'ishara': 'indication',
    'jankari': 'information', 'vivaran': 'details', 'bayora': 'description',
    'vishleshan': 'analysis', 'report': 'report', 'ahval': 'status',
    
    # Recovery terms
    'vapasi': 'recovery', 'wapas': 'return', 'prapti': 'receipt',
    'praptyankh': 'recovery', 'punah': 'again', 'dobara': 'again',
    'punarprapat': 'recover', 'reset': 'reset', 'restore': 'restore',
    
    # Transaction status
    'prakriyarat': 'processing', 'pratiksha': 'waiting', 'purna': 'complete',
    'adhura': 'incomplete', 'safal': 'successful', 'asfal': 'failed',
    'praman': 'confirmed', 'anishchit': 'pending', 'nirast': 'cancelled',
    # Common verbs in complaints
    'samajh': 'understand', 'samjho': 'understand', 'samjha': 'understood',
    'batao': 'tell', 'bataya': 'told', 'batane': 'to tell',
    'pucho': 'ask', 'pucha': 'asked', 'puchna': 'to ask',
    'bhejo': 'send', 'bheja': 'sent', 'bhejne': 'to send',
    
    # Transaction terminology
    'khata': 'account', 'rakam': 'amount', 'jama': 'deposit',
    'nikasi': 'withdrawal', 'shulk': 'fee', 'byaj': 'interest',
    'labh': 'profit', 'hani': 'loss', 'len-den': 'transaction',
    
    # Time expressions
    'samay': 'time', 'kal': 'tomorrow', 'parso': 'day after',
    'aaj': 'today', 'abhi': 'now', 'foran': 'immediately',
    'jald': 'soon', 'der': 'late', 'pahle': 'before',
    
    # Banking terms
    'khatadharak': 'account holder', 'rashii': 'amount', 'shakh': 'branch',
    'mudra': 'currency', 'nivesh': 'investment', 'bachat': 'savings',
    'udhar': 'credit', 'karz': 'loan', 'EMI': 'EMI',
    
    # Complaint specific
    'dhokhadhadi': 'fraud', 'shikayat': 'complaint', 'samasya': 'problem',
    'madad': 'help', 'sahayata': 'assistance', 'suraksha': 'security',
    'chori': 'theft', 'hani': 'damage', 'nuksan': 'loss',
    
    # Document related
    'kagaz': 'paper', 'dastavez': 'document', 'praman': 'proof',
    'photo': 'photo', 'chitra': 'image', 'copy': 'copy',
    'form': 'form', 'avedan': 'application', 'suchi': 'list',
    
    # Communication terms
    'baat': 'talk', 'sandesh': 'message', 'soochna': 'information',
    'sampark': 'contact', 'vishay': 'subject', 'uttar': 'reply',
    'javab': 'response', 'nivedhan': 'request', 'suchit': 'inform',
    
    # Status words
    'taiyar': 'ready', 'poora': 'complete', 'adhura': 'incomplete',
    'safal': 'successful', 'asafal': 'unsuccessful', 'jaari': 'ongoing',
    'rukka': 'stopped', 'band': 'closed', 'khula': 'open',
    
    # Location terms
    'jagah': 'place', 'sthan': 'location', 'pata': 'address',
    'ghar': 'home', 'daftar': 'office', 'shahar': 'city',
    'gaon': 'village', 'mohalla': 'neighborhood', 'sadak': 'road',
    
    # Urgency indicators
    'jaldi': 'quick', 'turant': 'immediate', 'avashyak': 'necessary',
    'mahatvapurn': 'important', 'zaruri': 'urgent', 'tatkal': 'immediate',
    'abhivilamba': 'urgent', 'shighra': 'quick', 'twarit': 'prompt',

    # Legal and complaint terms
    'darkhast': 'application', 'vakil': 'lawyer', 'kanoon': 'law',
    'adalat': 'court', 'nyayalay': 'court', 'police': 'police',
    'thana': 'police station', 'fir': 'complaint', 'jurm': 'crime',
    
    # Fraud specific terms
    'chhalava': 'deception', 'dokha': 'cheat', 'chor': 'thief',
    'badmash': 'criminal', 'dhokhebaaz': 'fraudster', 'jaalbaaz': 'scammer',
    'farzi': 'fake', 'nakli': 'duplicate', 'asli': 'genuine',
    
    # Digital terms
    'khata': 'account', 'password': 'password', 'screen': 'screen',
    'mobile': 'mobile', 'sampark': 'contact', 'sandesh': 'message',
    'vishay': 'subject', 'samvad': 'chat', 'pravesh': 'login',
    
    # Action verbs in complaints
    'rukna': 'stop', 'rokna': 'prevent', 'bachana': 'save',
    'madad': 'help', 'sahayata': 'assistance', 'suraksha': 'security',
    'jankari': 'information', 'suchna': 'information', 'pata': 'address',
    
    # Transaction status
    'safal': 'successful', 'vifal': 'failed', 'pending': 'pending',
    'pura': 'complete', 'adhura': 'incomplete', 'ruka': 'stopped',
    'band': 'closed', 'khula': 'open', 'chalu': 'active',
    
    # Threat related
    'dhamki': 'threat', 'dar': 'fear', 'bhay': 'scared',
    'pareshan': 'troubled', 'tang': 'harassed', 'dharmkana': 'threaten',
    'majboor': 'forced', 'dabav': 'pressure', 'jabardasti': 'forcefully',
    
    # Time expressions
    'kal': 'yesterday/tomorrow', 'parso': 'day after/before',
    'agle': 'next', 'pichle': 'last', 'pahle': 'before',
    'baad': 'after', 'abtak': 'until now', 'kabhi': 'sometime',
    
    # Request and urgency
    'jaldi': 'quick', 'turant': 'immediate', 'avashyak': 'necessary',
    'zaruri': 'urgent', 'mauka': 'opportunity', 'samasya': 'problem',
    'kripya': 'please', 'dhanyavad': 'thank you', 'shukriya': 'thanks',
    
    # Document related
    'kagaz': 'paper', 'dastavej': 'document', 'praman': 'proof',
    'saboot': 'evidence', 'copy': 'copy', 'photo': 'photo',
    'chitra': 'image', 'chithi': 'letter', 'form': 'form',
    
    # Status descriptors
    'kharab': 'bad', 'theek': 'okay', 'sahi': 'correct',
    'galat': 'wrong', 'acha': 'good', 'bura': 'bad',
    'mushkil': 'difficult', 'aasan': 'easy', 'sambhav': 'possible',

    # Financial terms
    'khata': 'account', 'passbook': 'passbook', 'atm': 'atm',
    'khaata': 'account', 'balance': 'balance', 'loan': 'loan',
    'byaj': 'interest', 'uddhar': 'loan', 'karza': 'debt',
    'jamaa': 'deposit', 'nikasi': 'withdrawal', 'len-den': 'transaction',
    
    # Cyber terms
    'password': 'password', 'login': 'login', 'logout': 'logout',
    'screenshot': 'screenshot', 'profile': 'profile', 'update': 'update',
    'download': 'download', 'upload': 'upload', 'website': 'website',
    'cyber': 'cyber', 'internet': 'internet', 'data': 'data',
    
    # Action verbs
    'dekho': 'look', 'dekha': 'saw', 'dekhna': 'see',
    'suno': 'listen', 'suna': 'heard', 'sunna': 'hear',
    'bolo': 'speak', 'bola': 'said', 'bolna': 'say',
    'likho': 'write', 'likha': 'wrote', 'likhna': 'write',
    
    # Time expressions
    'pichhla': 'last', 'agla': 'next', 'pehle': 'before',
    'baad': 'after', 'der': 'late', 'jaldi': 'early',
    'mahina': 'month', 'saal': 'year', 'hafta': 'week',
    'samay': 'time', 'waqt': 'time', 'din': 'day',
    
    # Status indicators
    'pending': 'pending', 'complete': 'complete', 'cancel': 'cancel',
    'processing': 'processing', 'failed': 'failed', 'success': 'success',
    'rukna': 'stop', 'ruka': 'stopped', 'rukawat': 'obstruction',
    
    # Complaint related
    'shikayat': 'complaint', 'samasya': 'problem', 'madad': 'help',
    'sahayata': 'assistance', 'jaanch': 'investigation', 'report': 'report',
    'action': 'action', 'karwayi': 'action', 'nyay': 'justice',
    
    # Communication terms
    'sandesh': 'message', 'sampark': 'contact', 'soochna': 'information',
    'javab': 'reply', 'uttar': 'response', 'baat': 'talk',
    'samvad': 'conversation', 'vishay': 'subject', 'topic': 'topic',
    
    # Document related
    'dastavej': 'document', 'kagaz': 'paper', 'copy': 'copy',
    'form': 'form', 'application': 'application', 'photo': 'photo',
    'proof': 'proof', 'sabut': 'evidence', 'record': 'record',
    
    # Fraud related
    'dhokha': 'fraud', 'chori': 'theft', 'fake': 'fake',
    'nakli': 'fake', 'jhuta': 'false', 'galat': 'wrong',
    'dhamki': 'threat', 'chakkar': 'scam', 'chhal': 'deception',
    
    # Process terms
    'prakriya': 'process', 'karyawahi': 'procedure', 'niyam': 'rule',
    'vidhi': 'method', 'tarika': 'way', 'steps': 'steps',
    'adhikar': 'right', 'anumati': 'permission', 'shart': 'condition',
    
    # Location related
    'jagah': 'place', 'sthan': 'location', 'pata': 'address',
    'sheher': 'city', 'gaon': 'village', 'desh': 'country',
    'rajya': 'state', 'zila': 'district', 'kshetra': 'area',

    # Basic verbs and auxiliaries
    'hai': 'is', 'hain': 'are', 'tha': 'was', 'thi': 'was',
    'kar': 'do', 'karo': 'do', 'kiya': 'did', 'karne': 'doing',
    'raha': 'doing', 'rahe': 'doing', 'rahi': 'doing',
    'diya': 'gave', 'dena': 'give', 'de': 'give', 'dey': 'give',
    'liya': 'took', 'lena': 'take', 'lo': 'take',
    'aayi': 'came', 'aaya': 'came', 'jana': 'go',
    
    # Pronouns and possessives
    'mein': 'in', 'mai': 'i', 'mera': 'my', 'mere': 'my',
    'aap': 'you', 'apka': 'your', 'apke': 'your',
    'uska': 'his/her', 'unka': 'their', 'hum': 'we',
    
    # Question words
    'kya': 'what', 'kaise': 'how', 'kyu': 'why',
    'kaha': 'where', 'kab': 'when', 'kaun': 'who',
    
    # Prepositions and conjunctions
    'se': 'from', 'ko': 'to', 'par': 'on', 'me': 'in',
    'ke': 'of', 'ka': 'of', 'ki': 'of', 'aur': 'and',
    
    # Common nouns
    'paisa': 'money', 'pai': 'money', 'paise': 'money',
    'bhai': 'brother', 'bahan': 'sister', 'dost': 'friend',
    'ghar': 'home', 'phone': 'phone', 'number': 'number',
    
    # Negatives and affirmatives
    'nahi': 'no', 'nahin': 'no', 'na': 'no',
    'haan': 'yes', 'achha': 'good', 'thik': 'okay',
    
    # Common adjectives
    'bada': 'big', 'chota': 'small', 'naya': 'new',
    'purana': 'old', 'acha': 'good', 'bura': 'bad',
    
    # Tech-related
    'message': 'message', 'call': 'call', 'phone': 'phone',
    'account': 'account', 'bank': 'bank', 'online': 'online',
    
    # Honorifics and titles
    'sir': 'sir', 'ji': 'sir', 'sahab': 'sir',
    'madam': 'madam', 'babu': 'mister',
    
    # Common verbs in cyber complaints
    'bhej': 'send', 'bheja': 'sent', 'milna': 'receive',
    'block': 'block', 'hack': 'hack', 'delete': 'delete',
    
    # Time-related
    'abhi': 'now', 'kal': 'tomorrow', 'aaj': 'today',
    'subah': 'morning', 'raat': 'night', 'sham': 'evening',
    
    # Quantities
    'kuch': 'some', 'bahut': 'many', 'thoda': 'little',
    'zyada': 'more', 'kam': 'less', 'sab': 'all',
    
    # Common in complaints
    'gali': 'abuse', 'problem': 'problem', 'help': 'help',
    'complaint': 'complaint', 'dhoka': 'fraud', 'galat': 'wrong',
    
    # Transaction related
    'bhugtan': 'payment', 'jama': 'deposit', 'transfer': 'transfer',
    'amount': 'amount', 'rupay': 'rupees'

}

# Remove duplicates by value
seen_values = set()
unique_mappings = {}

for key, value in hinglish_mappings.items():
    if value not in seen_values:
        seen_values.add(value)
        unique_mappings[key] = value

# Save unique mappings to JSON file
with open('hinglish_mappings.json', 'w', encoding='utf-8') as f:
    json.dump(unique_mappings, f, ensure_ascii=False, indent=4, sort_keys=True)

# Verify by reading the file
with open('hinglish_mappings.json', 'r', encoding='utf-8') as f:
    loaded_mappings = json.load(f)

print(f"Original mappings count: {len(hinglish_mappings)}")
print(f"Unique mappings count: {len(loaded_mappings)}")