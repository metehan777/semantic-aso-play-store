import nltk
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# --- Download NLTK resources (if needed) ---
try:
    nltk.data.find('tokenizers/punkt_tab/english')
except LookupError:
    print("Downloading 'punkt_tab'...")
    nltk.download('punkt_tab')

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    print("Downloading 'punkt'...")
    nltk.download('punkt')

nltk.download('wordnet')
nltk.download('omw-1.4')

# Initialize the Sentence Transformer model
model = SentenceTransformer('all-mpnet-base-v2')

def preprocess_text(text):
    """
    Tokenizes and lemmatizes the input text.

    Args:
        text: The input string.

    Returns:
        A list of lemmatized tokens.
    """
    lemmatizer = nltk.stem.WordNetLemmatizer()
    tokens = nltk.word_tokenize(text.lower())
    return [lemmatizer.lemmatize(token) for token in tokens]

def calculate_semantic_score(text, target_keyword):
    """
    Calculates the semantic similarity score between the text and a target keyword.

    Args:
        text: The input text (e.g., app description).
        target_keyword: The keyword to compare against.

    Returns:
        A semantic similarity score between 0 and 1.
    """

    # Preprocess the text and the target keyword
    text_tokens = preprocess_text(text)
    # keyword_tokens = preprocess_text(target_keyword)

    # Generate embeddings for the text and the target keyword
    text_embedding = model.encode(" ".join(text_tokens))
    keyword_embedding = model.encode(target_keyword)

    # Calculate the cosine similarity
    similarity_score = cosine_similarity(
        text_embedding.reshape(1, -1), keyword_embedding.reshape(1, -1)
    )[0][0]

    return similarity_score

def evaluate_play_store_content(app_title, short_description, long_description, target_keyword):
    """
    Evaluates the semantic relevance of a Play Store content to a target keyword.

    Args:
        app_title: The app's title.
        short_description: The app's short description.
        long_description: The app's long description.
        target_keyword: The target keyword or verb for evaluation.

    Returns:
        A dictionary containing the semantic scores for each section and an overall score.
    """
    
    title_score = calculate_semantic_score(app_title, target_keyword)
    short_desc_score = calculate_semantic_score(short_description, target_keyword)
    long_desc_score = calculate_semantic_score(long_description, target_keyword)

    # Weighted average (you can adjust weights based on importance)
    overall_score = (title_score * 0.3) + (short_desc_score * 0.5) + (long_desc_score * 0.2)

    return {
        "title_score": title_score,
        "short_description_score": short_desc_score,
        "long_description_score": long_desc_score,
        "overall_score": overall_score,
    }

# --- Example Usage ---
app_title = "Photo Editor Pro - Filters & Effects"
short_description = "Edit photos with amazing filters, effects, and collage maker. Enhance your images easily!"
long_description = """
Photo Editor Pro is the ultimate photo editing app for everyone! Whether you're a beginner or a pro, you can easily enhance your images with our powerful tools. 

**Key Features:**

*   **Filters:** Apply stunning filters to give your photos a unique look. Choose from vintage, black and white, cinematic, and more!
*   **Effects:** Add cool effects like blur, glitch, light leaks, and overlays.
*   **Collage Maker:** Create beautiful photo collages with various layouts and backgrounds.
*   **Stickers & Text:** Personalize your photos with fun stickers and custom text.
*   **Adjustment Tools:** Fine-tune brightness, contrast, saturation, and more.
*   **Retouching:** Remove blemishes, whiten teeth, and enhance facial features.

Download Photo Editor Pro now and start creating amazing photos!
"""
target_keyword = "edit photos"

scores = evaluate_play_store_content(app_title, short_description, long_description, target_keyword)

print(f"Target Keyword: {target_keyword}")
print(f"Title Score: {scores['title_score']:.3f}")
print(f"Short Description Score: {scores['short_description_score']:.3f}")
print(f"Long Description Score: {scores['long_description_score']:.3f}")
print(f"Overall Score: {scores['overall_score']:.3f}")
