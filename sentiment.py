"""
Sentiment Analyzer - محلل المشاعر البسيط
"""

# كلمات إيجابية
POSITIVE_WORDS = [
    'love', 'great', 'awesome', 'amazing', 'good', 'excellent',
    'happy', 'best', 'fantastic', 'wonderful', 'nice', 'perfect',
    'beautiful', 'enjoy', 'like', 'recommend', 'thanks', 'thank'
]

# كلمات سلبية
NEGATIVE_WORDS = [
    'hate', 'bad', 'terrible', 'awful', 'worst', 'horrible',
    'sad', 'angry', 'disappointed', 'poor', 'ugly', 'boring',
    'waste', 'never', 'wrong', 'fail', 'broken', 'useless'
]


def analyze_sentiment(text):
    """
    تحليل مشاعر النص
    
    Args:
        text: النص المراد تحليله
    
    Returns:
        dict: النتيجة (sentiment, score, details)
    """
    # تحويل لحروف صغيرة
    text_lower = text.lower()
    words = text_lower.split()
    
    # عد الكلمات
    positive_count = 0
    negative_count = 0
    found_positive = []
    found_negative = []
    
    for word in words:
        # إزالة علامات الترقيم
        clean_word = ''.join(c for c in word if c.isalpha())
        
        if clean_word in POSITIVE_WORDS:
            positive_count += 1
            found_positive.append(clean_word)
        elif clean_word in NEGATIVE_WORDS:
            negative_count += 1
            found_negative.append(clean_word)
    
    # حساب النتيجة
    total = positive_count + negative_count
    
    if total == 0:
        sentiment = "Neutral 😐"
        score = 0
    elif positive_count > negative_count:
        sentiment = "Positive 😊"
        score = positive_count / total
    elif negative_count > positive_count:
        sentiment = "Negative 😞"
        score = -negative_count / total
    else:
        sentiment = "Mixed 🤔"
        score = 0
    
    return {
        'text': text,
        'sentiment': sentiment,
        'score': round(score, 2),
        'positive_words': found_positive,
        'negative_words': found_negative
    }


def print_result(result):
    """طباعة النتيجة بشكل جميل"""
    print("\n" + "="*50)
    print("📝 Text:", result['text'])
    print("="*50)
    print(f"🎯 Sentiment: {result['sentiment']}")
    print(f"📊 Score: {result['score']}")
    
    if result['positive_words']:
        print(f"✅ Positive words: {', '.join(result['positive_words'])}")
    if result['negative_words']:
        print(f"❌ Negative words: {', '.join(result['negative_words'])}")
    print("="*50)


# ===== تشغيل البرنامج =====
if __name__ == "__main__":
    print("\n🔍 SENTIMENT ANALYZER - محلل المشاعر\n")
    
    # أمثلة للتجربة
    examples = [
        "I love this product! It's amazing and wonderful!",
        "This is terrible and horrible. Worst experience ever.",
        "The weather is okay today.",
        "I love the design but hate the price."
    ]
    
    print("📌 Testing examples:\n")
    for text in examples:
        result = analyze_sentiment(text)
        print_result(result)
    
    # تجربة المستخدم
    print("\n" + "="*50)
    print("💬 Try it yourself! (type 'quit' to exit)")
    print("="*50)
    
    while True:
        user_input = input("\n✏️  Enter text: ")
        if user_input.lower() == 'quit':
            print("\n👋 Goodbye!")
            break
        result = analyze_sentiment(user_input)
        print_result(result)
