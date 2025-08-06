from crew_builder import build_truthscribe_crew
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

if __name__ == "__main__":
    topic = "Introduction to Katseye, Global Girl Group"
    result = build_truthscribe_crew(topic)

    # Print the result (will include final Markdown article)
    print("\n✅ Final Output:\n")
    print(result)