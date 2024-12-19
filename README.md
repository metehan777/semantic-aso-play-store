## How to Use

This script helps you evaluate the semantic relevance of your Google Play Store app's title, short description, and long description to a target keyword or phrase. It uses Sentence Transformers to generate embeddings and calculates cosine similarity to provide a semantic score.

**Prerequisites:**

1.  **Python:** Make sure you have Python 3 installed on your system.
2.  **Libraries:** Install the required libraries using `pip`:

    ```bash
    pip install nltk numpy scikit-learn sentence-transformers
    ```

3.  **NLTK Resources:** You'll need to download specific NLTK resources. The script will prompt you to download them if they are missing. But, you can also download them manually using:
    ```python
    import nltk
    nltk.download('punkt_tab')
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    ```

**Steps:**

1.  **Clone the Repository (if applicable):** If you have this script in a repository, clone it to your local machine:

    ```bash
    git clone <repository_url>
    ```

2.  **Navigate to the Directory:** Open your terminal or command prompt and navigate to the directory where you saved the script.

3.  **Prepare Your Content:** Gather the following information from your Google Play Store listing:
    *   **`app_title`:** Your app's title.
    *   **`short_description`:** Your app's short description.
    *   **`long_description`:** Your app's long description.
    *   **`target_keyword`:** The keyword or phrase you want to evaluate against (e.g., "photo editor," "meditation app").

4.  **Modify the Script (Optional):**
    *   Open the `aso.py` (or whatever you named the script) file in a text editor.
    *   **Update Placeholders:** Replace the example `app_title`, `short_description`, `long_description`, and `target_keyword` with your app's actual content in the example usage section at the bottom of the script.

    ```python
    # ... (rest of the script) ...

    # --- Example Usage ---
    app_title = "Your App Title Here"  # Replace with your app's title
    short_description = "Your App Short Description Here"  # Replace with your short description
    long_description = """
    Your App Long Description Here
    """  # Replace with your long description
    target_keyword = "your target keyword"  # Replace with your target keyword

    scores = evaluate_play_store_content(app_title, short_description, long_description, target_keyword)

    print(f"Target Keyword: {target_keyword}")
    print(f"Title Score: {scores['title_score']:.3f}")
    print(f"Short Description Score: {scores['short_description_score']:.3f}")
    print(f"Long Description Score: {scores['long_description_score']:.3f}")
    print(f"Overall Score: {scores['overall_score']:.3f}")
    ```

5.  **Run the Script:** Execute the script from your terminal:

    ```bash
    python aso.py
    ```

**Interpreting the Output:**

The script will output the following:

*   **`Target Keyword`:** The keyword you entered for evaluation.
*   **`Title Score`:** A semantic similarity score (between 0 and 1) between your app title and the target keyword.
*   **`Short Description Score`:** A semantic similarity score (between 0 and 1) between your app's short description and the target keyword.
*   **`Long Description Score`:** A semantic similarity score (between 0 and 1) between your app's long description and the target keyword.
*   **`Overall Score`:** A weighted average of the above scores, giving more weight to the short description (you can customize the weights in the `evaluate_play_store_content` function).

**Higher scores indicate greater semantic relevance.** Use these scores to identify areas where you can improve your app's title and descriptions to better align with your target keywords from a semantic perspective.

**Note:** This script provides a simplified model of how Google might evaluate content semantically. The actual Google Play Store algorithm is much more complex and considers many other factors. However, this tool can give you valuable insights into the semantic relevance of your content and help you optimize your ASO strategy.
