from crew_builder import build_truthscribe_crew
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

if __name__ == "__main__":
    topic = "Indonesian Team at Olympics 2024 in Paris"
    result = build_truthscribe_crew(topic)

    # Print the result (will include final Markdown article)
    print("\n✅ Final Output:\n")
    print(result)